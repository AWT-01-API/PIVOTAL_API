from src.api.RequestManager import RequestManager
from src.util.ReadCfg import ReadCfg

def before_all(context):
    url = ReadCfg.get_value("apiURL")
    token = context.config.userdata.get("apitoken")
    print ("setting token =" + str(token))
    RequestManager(url)
    RequestManager.instance.session.headers.update({"X-TrackerToken": str(token)})
