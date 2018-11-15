from behave import *
from src.api.request_manager import RequestManager

@given(u'I')
def step_impl(context):
    print("a")