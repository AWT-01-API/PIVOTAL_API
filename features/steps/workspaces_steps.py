from behave import *
from src.api.request_manager import RequestManager
use_step_matcher("re")


@step("I create a new workspace with fields:")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    RequestManager.put_request("workspaces")


@step('I store the response as "Workspace1"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """


@then('I verify if the workspace is created with "Workspace1" data')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """


@step('I store the response as "Workspace1"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
