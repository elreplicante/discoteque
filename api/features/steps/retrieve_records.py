from api.app import app
from expects import *
import json

@given(u'I lost all my records')
def step_lost_all_records(context):
    pass


@when(u'I see my records list')
def step_impl(context):
    context.response = context.client.get('/')


@then(u'I see anything')
def step_impl(context):
    print(context.response.__dict__)
    expect(context.response.status_code).to(equal(200))
    expect(json.loads(context.response.data)).to(equal([]))