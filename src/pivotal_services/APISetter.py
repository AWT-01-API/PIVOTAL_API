from src.pivotal_services.PivotalServices import PivotalServices
from src.api.RequestManager import RequestManager
from src.util.ReadCfg import ReadCfg
from src.util.LoggerHandler import LoggerHandler


class APISetter(PivotalServices):

    def __init__(self, user):
        super(APISetter, self).__init__("me")
        api_token = user.replace('user', 'apiToken')
        RequestManager(ReadCfg.get_value('apiUrl'))
        token = ReadCfg.get_value(api_token)
        RequestManager.instance.session.headers.update({"X-TrackerToken": token})
        LoggerHandler.get_instance().info(user + ", " + token + " token set")
