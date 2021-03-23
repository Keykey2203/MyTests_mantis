from model.project import Project
from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app, config):
        self.app = app
        self.config = config

    def can_login(self, username, password):
        client = Client(self.config["mantis"]["url"])

        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self, username, password):
        client = Client(self.config["mantis"]["url"])
        items = []
        # try:
        soap_items = client.service.mc_projects_get_user_accessible(username, password)
        for soap_item in list(soap_items):
            name = soap_item.name
            items.append(Project(name=name))
        return list(items)
        # except WebFault:
        #     return False
