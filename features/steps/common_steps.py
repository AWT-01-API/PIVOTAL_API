from behave import given, step, use_step_matcher
from src.api.RequestManager import RequestManager
from src.util.ReadCfg import ReadCfg
from src.pivotal_services.APISetter import APISetter
import jsonschema
import simplejson as json
from src.util.read_file import ReadFile

use_step_matcher("re")


@given('I login as \"([^\"]*)\"')
def step_impl(context, user):
    APISetter(user)


@given('I send a basic auth get request \"([^\"]*)\"')
def step_impl(context, endpoint):
    context.req_helper = RequestManager(ReadCfg.get_value("url") + ":/services/v5",)
    context.last_response = context.req_helper.get_request_basic_auth(endpoint)


@step('I save the response as \"([^\"]*)\"')
def step_impl(context, resp_name):
    context.response_map = {resp_name: context.last_response}


@step('I set the api token as \"([^\"]*)\"')
def step_impl(context, key):
    spliced_keys = key.split(".", 1)
    if len(spliced_keys) > 1:
        namekey = spliced_keys[0]
        jsonkey = spliced_keys[1]
        token = context.response_map[namekey].json()[jsonkey]
        context.req_helper.set_token(str(token))
    else:
        # log message "key must have 2 keys: "Example.name""
        return None


@step('I send a post request \"([^\"]*)\" with')
def step_impl(context, endpoint):
    body = {}
    for row in context.table:
        body = {row["field"]: row["content"]}
    context.last_response = context.req_helper.post_request(endpoint, body)
    context.id = context.last_response.json()['id']


@step('I verify if the response status code is \"([^\"]*)\"')
def step_impl(context, status_code):
    assert (status_code == str(context.last_response.status_code)) is not None


@step('I verify if the \"([^\"]*)\" body is correct')
def step_impl(context, schema):
    schema_data = ReadFile.get_file_validator('schema-' + schema + '.json')
    schema_project = json.loads(schema_data)
    jsonschema.validate(context.response.json(), schema_project)

