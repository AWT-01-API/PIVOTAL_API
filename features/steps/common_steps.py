
from behave import given, step, use_step_matcher
from src.api.request_manager import RequestManager
from src.util.ReadCfg import ReadCfg

use_step_matcher("re")


@given('I login as "user1"')
def step_impl(context):
    key = ReadCfg.get_value("apiToken")
    context.req_helper = RequestManager(ReadCfg.get_value("url") + "/services/v5", "", "")
    context.req_helper.set_token(key)
    context.last_response = context.req_helper.get_request("/me")


@given('I send a basic auth get request \"([^\"]*)\"')
def step_impl(context, endpoint):
    context.req_helper = RequestManager(ReadCfg.get_value("url") + ":/services/v5",
                                        ReadCfg.get_value("user3"), ReadCfg.get_value("password3"))
    context.last_response = context.req_helper.get_request_basic_auth(endpoint)


@step('I save the response as \"([^\"]*)\"')
def step_impl(context, resp_name):
    context.response_map = {resp_name: context.last_response}


@step('I set the api token as \"([^\"]*)\"')
def step_impl(context, key):
    spliced_keys = key.split(".", 1)
    if len(spliced_keys) > 1:
        namekey = spliced_keys[0]
        jsonkey = spliced_keys[1]
        token = context.response_map[namekey].json()[jsonkey]
        context.req_helper.set_token(str(token))
    else:
        # log message "key must have 2 keys: "Example.name""
        return None



@step('I send a post request \"([^\"]*)\" with')
def step_impl(context, endpoint):
    body = {}
    for row in context.table:
        body = {row["field"]: row["content"]}
    context.last_response = context.req_helper.post_request(endpoint, body)
