from behave import given
from src.API.request_manager import RequestManager

@given(u'I send a post request {endpoint} with')
def set_impl(context, endpoint):
    for row in context.table:
        print(row['name'])
        print(row['project_id'])