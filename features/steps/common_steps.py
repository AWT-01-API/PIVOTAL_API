from behave import given, step, use_step_matcher
from src.api.request_manager import RequestManager

use_step_matcher("re")


@given('I send a basic auth get request \"([^\"]*)\"')
def step_impl(context, endpoint):
    context.req_helper = RequestManager("https://www.pivotaltracker.com/services/v5", "kevinherrera2", "70723844")
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
        map = context.response_map[namekey]
        token = map.json()[jsonkey]
        context.req_helper.set_token(str(token))
        print str(token)
    else:
        ## log message "key must have 2 keys: "Example.name""
        return None



@step('I send a post request \"([^\"]*)\" with')
def step_impl(context, endpoint):
    body = {}
    for row in context.table:
        body = {row["field"]: row["content"]}
    context.last_response = context.req_helper.post_request(endpoint, body)
