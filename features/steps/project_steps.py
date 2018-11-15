from behave import given, step
from src.util.loggerhandler import LoggerHandler
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
    try:
        project = Projects()
        context.res = project.create_project(r_name)
        LoggerHandler.get_instance().info("Project created" + r_name)
    except Exception as e:
        LoggerHandler.get_instance().error("arrived at exception: " + str(e))
        raise ("failed with exception: " + str(e))

@step('I verify the status code is "200"')
def step_impl(context):
    assert context.res.status_code == 200
