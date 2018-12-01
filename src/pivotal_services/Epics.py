from src.pivotal_services.PivotalServices import PivotalServices


class Epics(PivotalServices):

    def __init__(self, project_id, epic_id=None):
        if epic_id is not None:
            epic_id = '/' + epic_id
        else:
            epic_id = ''
        super(Epics, self).__init__("/projects/" + project_id + "/epics" + epic_id)
