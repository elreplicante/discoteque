from api.app import app
from expects import *

@given(u'I lost all my records')
def step_lost_all_records(context):
    context.api = app.test_client()


@when(u'I see my records list')
def step_impl(context):
    context.response = context.api.get('/')


@then(u'I see anything')
def step_impl(context):
    print(context.response.__dict__)
    expect(context.response.status_code).to(equal(200))
    expect(context.response.status_code).to(equal(200))