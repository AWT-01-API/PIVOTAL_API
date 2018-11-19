from src.pivotal_services.PivotalServices import PivotalServices


class Workspaces(PivotalServices):

    def __init__(self, workspace_id=None):
        if workspace_id is not None:
            workspace_id = '/' + workspace_id
        else:
            workspace_id = ''
        super(Workspaces, self).__init__("/workspaces" + workspace_id)
