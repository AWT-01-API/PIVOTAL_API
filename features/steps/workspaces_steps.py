from behave import *
from src.pivotal_services.Workspaces import Workspaces
import datetime
use_step_matcher("re")


@when('I create a workspace with')
def step_impl(context):
    body = {}
    for row in context.table:
        body = {row["field"]: row["content"]}
    workspace = Workspaces()
    body = {"name": body.get('name') + str(datetime.datetime.now().microsecond)}
    context.last_response = workspace.create(body)

@then('I verify if \"([^\"]*)\" is created')
def step_impl(context, workspace_created):
    workspace = Workspaces()
    new_response = workspace.get(context.last_response.json().get('id'))
    print new_response
    assert new_response.status_code is 200


@then('I verify if \"([^\"]*)\" exists in \"([^\"]*)\"')
def step_impl(context, project, workspace):
    assert context.last_response is not None


@step('I edit \"([^\"]*)\" with')
def step_impl(context, workspace):
    assert context.last_response is not None


@then('I verify if the field \"([^\"]*)\" of \"([^\"]*)\" is correct')
def step_impl(context, field, workspace):
    assert context.last_response is not None


@step('I delete \"([^\"]*)\"')
def step_impl(context, element):
    assert context.last_response is not None


@then('I verify if \"([^\"]*)\" is deleted')
def step_impl(context, element):
    assert context.last_response is not None


@step('I add \"([^\"]*)\" to the workspace \"([^\"]*)\"')
def step_impl(context, project, workspace):
    assert context.last_response is not None
