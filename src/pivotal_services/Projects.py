from src.pivotal_services.PivotalServices import PivotalServices


class Projects(PivotalServices):

    def __init__(self):
        super(Projects, self).__init__("projects")
