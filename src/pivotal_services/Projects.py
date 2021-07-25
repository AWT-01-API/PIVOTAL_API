from src.pivotal_services.PivotalServices import PivotalServices
from src.util.LoggerHandler import LoggerHandler

log = LoggerHandler.get_instance()


class Projects(PivotalServices):

    def __init__(self, project_id=None):
        super(Projects, self).__init__("/projects", project_id)

    def create_a_new_project(self, body):
        response = self.create(body)
        log.info(response.status_code)
        log.info(response.json())
        if (response.status_code == 400 and response.json()["general_problem"].__contains__(
                "The project name you entered is already taken.")):
            log.info("Project is %s already exists" % body["name"])
            response = self.get_project_info_by_name(body["name"])
        return response

    def get_project_info_by_name(self, project_name):
        projects = self.get("").json()
        log.info("Projects:\n %s" % projects)
        for project in projects:
            if (project['name'].__contains__(project_name)):
                return project
        return None
