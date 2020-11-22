from selenium.webdriver.support.ui import Select
from model.project import Project

class ProjectsHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        self.app.wd.find_element_by_link_text("Manage").click()

    def open_projects_page(self):
        self.open_manage_page()
        self.app.wd.find_element_by_link_text("Manage Projects").click()

    def open_new_project_page(self):
        self.open_projects_page()
        self.app.wd.find_element_by_css_selector("input[value='Create New Project']").click()

    def fill_project(self, project):
        self.change_field_value("name", project.name)
        self.change_select_value("status", project.status)
        self.change_select_value("view_state", project.view_state)
        self.change_field_value("description", project.desc)
        if project.inherit_global == 0:
            self.app.wd.find_element_by_css_selector("input[name='inherit_global']").click()


    def change_select_value(self, select_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(select_name).click()
            Select(wd.find_element_by_name(select_name)).select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, project):
        self.open_new_project_page()
        self.fill_project(project)
        self.app.wd.find_element_by_css_selector("input[value='Add Project']").click()

    def get_projects_list(self):
        wd = self.app.wd
        self.open_projects_page()
        items = []
        table = wd.find_elements_by_css_selector("table")[2]
        rows_cnt = len(table.find_elements_by_css_selector("tr"))
        index = 3
        while index <= rows_cnt:
            row = table.find_element_by_css_selector("tr:nth-child(%s)" % index)
            name = row.find_element_by_css_selector("td:nth-child(1) a").text.strip()
            status = row.find_element_by_css_selector("td:nth-child(2)").text.strip()
            enabled = 0
            if row.find_element_by_css_selector("td:nth-child(3)").text.strip() == "X":
                enabled = 1
            view_state = row.find_element_by_css_selector("td:nth-child(4)").text.strip()
            desc = row.find_element_by_css_selector("td:nth-child(5)").text.strip()
            items.append(Project(name=name, status=status, enabled=enabled, view_state=view_state, desc=desc))
            index += 1
        return list(items)

    def delete_by_name(self, name):
        wd = self.app.wd
        self.open_projects_page()
        table = wd.find_elements_by_css_selector("table")[2]
        links = table.find_elements_by_css_selector("tr:not(.row-category) a")
        for link in links:
            if link.text.strip() == name:
                link.click()
                wd.find_element_by_css_selector("input[value='Delete Project']").click()
                wd.find_element_by_css_selector("input[value='Delete Project']").click()
                break








