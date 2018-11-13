import requests


class RequestManager:

    def __init__(self):
        self.main_url = "https://www.pivotaltracker.com/services/v5"
        self.username = "kevinherrera2"
        self.password = "70723844"
        self.token = "f89634fa55d2cb80fee84fd0d6a9fd2a"
        self.header = {"X-TrackerToken": self.token}
        pass

    def get_request_basic_auth(self, endpoint):
        """used to get user token"""
        response = requests.get(self.main_url + endpoint, auth={self.username: self.password})
        if response.status_code == 200:
            return response

    def get_request(self, endpoint):
        """used to get request from api"""
        # endpoint: api request endpoint as string
        response = requests.get(self.main_url + endpoint, headers=self.header)
        if response.status_code == 200:
            return response

    def post_request(self, endpoint, body):
        """used to get request from api"""
        # endpoint: api request endpoint as string
        # body: body for post as dictionary of strings {"example":"data",}
        response = requests.post(self.main_url + endpoint, body, headers=self.header)
        if response.status_code == 200:
            return response

    def put_request(self, endpoint, body):
        """used to get request from api"""
        # endpoint: api request endpoint as string
        # body: body for post as dictionary of strings {"example":"data",}
        response = requests.put(self.main_url + endpoint, body, headers=self.header)
        if response.status_code == 200:
            return response

    def del_request(self, endpoint):
        """used to get request from api"""
        # endpoint: api request endpoint as string
        response = requests.delete(self.main_url + endpoint, headers=self.header)
        return response.status_code
