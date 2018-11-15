from behave import given, step, use_step_matcher
from src.API.request_manager import RequestManager

use_step_matcher("re")

@given('I send a basic auth get request \"([^\"]*)\"')
def step_impl(context, endpoint):
    context.req_helper = RequestManager("https://www.pivotaltracker.com/services/v5", "", "")
    context.last_response = context.req_helper.get_request_basic_auth(endpoint)

@step('I save the response as \"([^\"]*)\"')
def step_impl(context, resp_name):
    if context.responseMap is None:
        context.responseMap = {}
    context.responseMap[resp_name] = context.last_response

