import pytest
import requests
#from logger import appLogger


def make_request(full_url):
    response = requests.get(full_url)
#    appLogger.debug("Response status is {}".format(response.status_code))
    return response


def get_response_time(response):
    response_time = response.elapsed.total_seconds()
#    appLogger.debug("Request completed in {} ms".format(response_time * 1000))
    return response_time * 1000


def get_response_body(response_for_body):
    body: list = response_for_body.json()
#    appLogger.debug('Getting response body from API')
    return body


def check_body_types(json_data):
    for i in range(0, len(json_data)):
        field_type = (type(json_data[i]))
#        appLogger.info('Check type ' + str(i) + str(field_type))
        return field_type

#@pytest.mark.parametrize(('endpoint'), ['list_users_id'])
def test_list_users_id_response():
    response = make_request(('http://127.0.0.1:5000/' + str('list_users_id')))
    response_time = get_response_time(response)

    body = get_response_body(response)


    assert response.ok
    assert response_time < 3
    assert isinstance(body, list)  # not empty
    assert len(body) != 0

    field_type = check_body_types(body)
    assert field_type == dict