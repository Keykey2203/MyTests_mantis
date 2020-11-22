from model.project import Project
import random
import string


def test_add_blank_project(app):
    items = app.projects.get_projects_list()
    new_item = Project(name="", status="development", inherit_global=1, view_state="public", desc="", enabled=1)
    app.projects.create(new_item)
    new_items = app.projects.get_projects_list()
    assert len(items) == len(new_items)
    assert sorted(items, key=Project.id_or_max) == sorted(new_items, key=Project.id_or_max)

def test_add_project(app, json_projects):
    items = app.projects.get_projects_list()
    new_item = json_projects
    if is_in_list(new_item.name, items):
        new_item.name = random_string(new_item.name, 10)
    app.projects.create(new_item)
    new_items = app.projects.get_projects_list()
    items.append(new_item)
    assert len(items) == len(new_items)
    assert sorted(items, key=Project.sort_by_name) == sorted(new_items, key=Project.sort_by_name)

def is_in_list(text, list):
    for i in list:
        if i.name == text:
            return True
    return False

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



