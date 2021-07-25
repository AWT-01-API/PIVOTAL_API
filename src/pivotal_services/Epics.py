import datetime

from src.pivotal_services.PivotalServices import PivotalServices
from src.util.LoggerHandler import LoggerHandler

log = LoggerHandler.get_instance()


class Epics(PivotalServices):

    def __init__(self, project_id, epic_id=None):
        if epic_id is not None:
            epic_id = '/' + epic_id
        else:
            epic_id = ''
        super(Epics, self).__init__("/projects/" + project_id + "/epics" + epic_id)

    def create_new_epic(self, body):
        body['name'] = body['name'] + str(datetime.datetime.now())
        response = self.create(body)
        log.info(response.status_code)
        log.info(response.json())
        return response
