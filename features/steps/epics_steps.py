from behave import given, when, step
from features.steps.common_steps import responses
from src.api.request_manager import RequestManager


@when(u'I get the response of the past project')
def step_impl(context):
    print ("wntro")

