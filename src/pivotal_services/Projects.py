from src.pivotal_services.PivotalServices import PivotalServices


class Projects(PivotalServices):

    def __init__(self, project_id=None):
        super(Projects, self).__init__("/projects", project_id)
