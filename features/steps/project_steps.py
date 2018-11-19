from behave import *
from src.pivotal_services.Projects import Projects
use_step_matcher("re")


@when("I create a project with")
def step_impl(context):
    body = {}
    for row in context.table:
        body = {row["field"]: row["content"]}
    project = Projects()
    context.last_response = project.create(body)
