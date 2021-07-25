from behave import *
from hamcrest import assert_that, equal_to

from src.pivotal_services.Projects import Projects
from src.util.LoggerHandler import LoggerHandler

use_step_matcher("re")

log = LoggerHandler.get_instance()
project = Projects()


@when("I create a project with")
def step_impl(context):
    body = {}
    for row in context.table:
        body = {row["field"]: row["content"]}
    context.last_response = project.create_a_new_project(body)


@then("I validate that \"(.*)\" project is created")
def step_impl(context, project_name):
    """
    :type context: behave.runner.Context
    """
    project_info = project.get_project_info_by_name(project_name)
    assert_that(project_info['name'], equal_to(project_name))
