from src.pivotal_services import PivotalServices
from src.api.request_manager import RequestManager
from src.util.ReadCfg import ReadCfg


class Workspaces(PivotalServices):

    def __init__(self):
        self.endpoint = "workspaces"
        RequestManager.instance(ReadCfg.get_value("url"))

    def create_workspace(self, body):
        return self.create(body)

    def edit_workspace(self, body):
        return self.edit(body)

    def delete_workspace(self, w_id):
        return self.delete(w_id)

    def get_workspace(self, w_id):
        return self.get(w_id)
