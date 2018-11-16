from behave import *
from src.api.request_manager import RequestManager
from src.util.ReadCfg import ReadCfg
from src.pivotal_services.Workspaces import Workspaces

use_step_matcher("re")


@then('I verify if the workspace is created')
def step_impl(context):
    assert context.last_response is not None


@step("I a workspace with fields:")
def step_impl(context):
    workspace = Workspaces()
    workspace.create(context.table)
