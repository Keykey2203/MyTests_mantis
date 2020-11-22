from model.project import Project
import random


def test_delete_some_project(app):
    old_items = app.projects.get_projects_list()
    if len(old_items) == 0:
        app.projects.create(Project(name="llll"))
        old_items = app.projects.get_projects_list()
    item = random.choice(old_items)
    app.projects.delete_by_name(item.name)
    new_items = app.projects.get_projects_list()
    assert len(old_items) - 1 == len(new_items)
    old_items.remove(item)
    assert old_items == new_items
    assert sorted(new_items, key=Project.sort_by_name) == sorted(old_items, key=Project.sort_by_name)