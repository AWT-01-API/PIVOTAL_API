from src.pivotal_services.PivotalServices import PivotalServices


class Workspaces(PivotalServices):

    def __init__(self):
        super(Workspaces, self).__init__("workspaces")
