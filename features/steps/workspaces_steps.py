from behave import *
from src.api.request_manager import RequestManager
from src.util.ReadCfg import ReadCfg
use_step_matcher("re")


@step("I create a new workspace with fields:")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.req_helper = RequestManager.put_request(ReadCfg.get_value("url") + "workspaces", context.table)



@then('I verify if the workspace is created with "Workspace1" data')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
