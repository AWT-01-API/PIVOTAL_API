from behave import *
from src.API.request_manager import RequestManager

@given(u'I')
def step_impl(context):
    print("a")