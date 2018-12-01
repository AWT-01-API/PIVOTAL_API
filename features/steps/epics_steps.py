from behave import then, step, use_step_matcher
from src.util.response_validator import ResponseValidator
from src.pivotal_services.Epics import Epics

use_step_matcher("re")


@step('I create a epic with')
def step_impl(context):
    body = {}
    for row in context.table:
        body = {row["field"]: row["content"]}
    epic = Epics(str(context.last_response.json()['id']), None)
    context.last_response = epic.create(body)


@then('I verify epic is created')
def step_impl(context):
    ResponseValidator.validate_status_code(context.last_response)


@then('I verify epic body is correct')
def step_impl(context):
    ResponseValidator.validate_schema('schema-epic.json', context.last_response)
