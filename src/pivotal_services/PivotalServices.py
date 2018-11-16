from abc import ABCMeta, abstractmethod
from src.api.request_manager import RequestManager
from src.util.ReadCfg import ReadCfg


class PivotalServices(object):
    __metaclass__ = ABCMeta

    def __init__(self, endpoint):
        self.endpoint = endpoint
        RequestManager.instance(ReadCfg.get_value("url"))

    def create(self, body):
        return RequestManager.instance.post_request(self.endpoint, body)

    def edit(self, body):
        return RequestManager.instance.put_request(self.endpoint, body)

    def delete(self, body):
        return RequestManager.instance.delete_request(self.endpoint, body)

    def get(self, id):
        return RequestManager.instance.get_request(self, id)
