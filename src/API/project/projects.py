"""project rest api requests"""
import requests
from src.api.request_manager import RequestManager
from src.util.ReadCfg import ReadCfg


class Projects(object):
    """manager of rest api requests to projects"""

    def __init__(self):
        pass

    def create_project(self, data_name):
        """Create projet"""
        url = ReadCfg.get_value("apiURL")
        request_manager = RequestManager(url, "", "")
        res = request_manager.post_request("/projects", data_name)
        return res

    def delete_project(id):
        """delete project"""
        url = ReadCfg.get_value("apiURL")
        request = RequestManager(url, "", "")
        res = request.delete_request('/projects/' + str(id))
        return res
