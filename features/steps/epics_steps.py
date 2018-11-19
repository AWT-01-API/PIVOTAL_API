from behave import then, step, use_step_matcher
import jsonschema
import simplejson as json
from src.util.read_file import ReadFile

use_step_matcher("re")


@step('I send a post request epic \"([^\"]*)\" with')
def step_impl(context, endpoint):
    endpoint = endpoint.replace("{project_id}", str(context.last_response.json()['id']))

    body = {}
    for row in context.table:
        body = {row["field"]: row["content"]}
        context.response = context.req_helper.post_request(endpoint, body)


@then('I verify epic is created')
def step_impl(context):
    assert context.response.status_code == 200


@then('I verify epic body is correct')
def step_impl(context):
    schema_data = ReadFile.get_file_validator('schema-epic.json')
    schema_project = json.loads(schema_data)
    jsonschema.validate(context.response.json(), schema_project)


