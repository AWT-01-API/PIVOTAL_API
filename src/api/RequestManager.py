"""manage rest api requests"""
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class RequestManager:
    class __RequestManager:
        def __init__(self, main_url):
            self.main_url = main_url
            self.session = requests.Session()

        def get_request(self, endpoint):
            """used to get request from api"""
            # endpoint: api request endpoint as string
            response = self.requests_retry_session(session=self.session).get(self.main_url + endpoint)
            return response

        def post_request(self, endpoint, body):
            """used to get request from api"""
            # endpoint: api request endpoint as string
            # body: body for post as dictionary of strings {"example":"data",}
            response = self.requests_retry_session(session=self.session).post(self.main_url + endpoint, body)
            return response

        def put_request(self, endpoint, body):
            """used to get request from api"""
            # endpoint: api request endpoint as string
            # body: body for post as dictionary of strings {"example":"data",}
            response = self.requests_retry_session(session=self.session).put(self.main_url + endpoint, body)
            return response

        def delete_request(self, endpoint):
            """used to get request from api"""
            # endpoint: api request endpoint as string
            response = self.requests_retry_session(session=self.session).delete(self.main_url + endpoint)
            return response

        @staticmethod
        def requests_retry_session(
                retries=3,
                backoff_factor=0.3,
                status_forcelist=(500, 502, 504),
                session=None):
            """used to process a request retry if their response is 500, 502, or 504 """
            session = session or requests.Session()
            retry = Retry(
                total=retries,
                read=retries,
                connect=retries,
                backoff_factor=backoff_factor,
                status_forcelist=status_forcelist,
            )
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            return session

    instance = None

    def __init__(self, main_url):
        if not RequestManager.instance:
            RequestManager.instance = RequestManager.__RequestManager(main_url)
        else:
            RequestManager.instance.main_url = main_url

    def __getattr__(self, name):
        return getattr(self.instance, name)
