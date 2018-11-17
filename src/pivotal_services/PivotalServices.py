from abc import ABCMeta
from src.api.RequestManager import RequestManager


class PivotalServices(object):
    __metaclass__ = ABCMeta

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def create(self, body):
        return RequestManager.instance.post_request(self.endpoint, body)

    def edit(self, body):
        return RequestManager.instance.put_request(self.endpoint, body)

    def delete(self, body):
        return RequestManager.instance.delete_request(self.endpoint, body)

    def get(self, id):
        return RequestManager.instance.get_request(self, id)

