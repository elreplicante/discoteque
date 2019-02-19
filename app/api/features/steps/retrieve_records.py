import json
from http import HTTPStatus

from expects import *


@given(u'I lost all my records')
def step_lost_all_records(context):
    pass


@when(u'I see my records list')
def step_see_record_list(context):
    context.response = context.client.get('/records')


@then(u'I see nothing')
def step_see_nothing(context):
    expect(context.response.status_code).to(equal(HTTPStatus.OK))
    expect(json.loads(context.response.data)).to(be_empty)

@given(u'There are some records in my discoteque')
def step_impl(context):
    context.client.post('/record', data={
        'name': 'Challenger',
        'artist': 'Baby\'s Gang'
    }, follow_redirects=True)


@then(u'I see the records')
def step_impl(context):
    response = context.client.get('/records')

    expect(json.loads(response.data)).to_not(be_empty)
