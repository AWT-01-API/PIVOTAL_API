from behave import given, step, use_step_matcher
from src.API.request_manager import RequestManager
from src.API.project.projects import Projects
from src.util.ReadCfg import ReadCfg

@given('I login as "user1"')
def step_impl(context):
    key = ReadCfg.get_value("apiToken")
    context.req_helper = RequestManager("https://www.pivotaltracker.com/services/v5", "", "")
    context.req_helper.set_token(key)
    context.last_response = context.req_helper.get_request("/me")
    print (context.last_response.status_code)

@given('a {name}')
def step_impl(context, name):
    r_name = ""
    for row in context.table:
        r_name = row['name']

    project = Projects()
    res = project.create_project(r_name)
    print(res)

@step('I verify the status code is "200"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    #raise NotImplementedError(u'STEP: And I verify the status code is "200"')