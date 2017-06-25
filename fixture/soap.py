from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapFixture:

    def __init__(self, user, password, soapUrl):
        self.user = user
        self.password = password
        self.soapUrl = soapUrl
        self.client = Client(soapUrl)

    def can_login(self):
        try:
            self.client.service.mc_login(self.user, self.password)
            return True
        except WebFault:
            return False

    def get_list(self):
        projects_list = []
        try:
            projects = list(self.client.service.mc_projects_get_user_accessible(self.user, self.password))
            for element in projects:
                projects_list.append(Project(element['name'], element['description']))
            return projects_list
        except WebFault as ex:
            print(ex)
            return False
