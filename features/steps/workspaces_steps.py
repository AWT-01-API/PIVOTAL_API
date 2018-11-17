from behave import *
from src.pivotal_services.Workspaces import Workspaces

use_step_matcher("re")


@then('I verify if the workspace is created')
def step_impl(context):
    assert context.last_response is not None


@when("I create a workspace with fields:")
def step_impl(context):
    print "something"
