from behave import *
from src.API.request_manager import RequestManager

use_step_matcher("re")


@given('I send a basic auth get request \"([^\"]*)\"')
def step_impl(context, endpoint):
    request_manager = RequestManager()
    context.req_helper = request_manager.get_request("/me")
    context.last_response = context.req_helper.get_request_basic_auth(endpoint)


@step('I save the response as \"([^\"]*)\"')
def step_impl(context, resp_name):
    if context.responseMap is None:
        context.responseMap = {}
    context.responseMap[resp_name] = context.last_response

