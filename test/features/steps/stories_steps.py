from behave import *

use_step_matcher("re")


@step('I send a post request to \"([^\"]*)\" with')
def step_impl(context, endpoint):
    PROJECT_ID = context.id
    end_point = '/projects/' + str(PROJECT_ID) + endpoint

    body = {}
    for row in context.table:
        body = {row["field"]: row["content"]}
    context.response = context.req_helper.post_request(end_point, body)


@then('I verify stories is created with "/stories"')
def step_impl(context):
    assert context.response.status_code == 200
