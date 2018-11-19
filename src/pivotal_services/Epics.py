from src.pivotal_services.PivotalServices import PivotalServices


class Epics(PivotalServices):

    def __init__(self, project_id, epic_id=None):
        super(Epics, self).__init__('/' + project_id + "/epics", epic_id)
