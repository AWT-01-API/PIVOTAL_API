from abc import ABCMeta
from src.api.RequestManager import RequestManager
from src.util.Logger import Logger

class PivotalServices(object):
    __metaclass__ = ABCMeta

    def __init__(self, endpoint, o_id=None):
        if o_id is None:
            o_id = ''
        else:
            o_id = '/' + o_id
        self.endpoint = endpoint + o_id

    def create(self, body):
        Logger.info("Create-Post request with endpoint: " + self.endpoint + " and body:" + str(body))
        return RequestManager.instance.post_request(self.endpoint, body)

    def edit(self, body):
        Logger.info("Edit-Put request with endpoint: " + self.endpoint + " and body:" + str(body))
        return RequestManager.instance.put_request(self.endpoint, body)

    def delete(self, body):
        Logger.info("Delete request with endpoint: " + self.endpoint + " and body:" + str(body))
        return RequestManager.instance.delete_request(self.endpoint, body)

    def get(self, id):
        Logger.info("Get request with endpoint: " + self.endpoint + " for the id: " + str(id))
        return RequestManager.instance.get_request(self.endpoint + '/' + str(id))

