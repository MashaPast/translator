import pytest
from helpers import helpers_func as h

SERVER_API_URL = 'http://127.0.0.1:5000/'

@pytest.mark.happypath
def test_translate():
    response = h.make_post_request_to_translate((SERVER_API_URL + str('translate')))
    response_time = h.get_response_time(response)

    body = h.get_response_body(response)

    assert response.ok
    assert response_time < 600
    assert isinstance(body, dict)
    assert body != {} #not empty

    assert isinstance(body['word'], str)
    assert isinstance(body['translate'], str)

@pytest.mark.happypath
def test_list_users_id_response():
    response = h.make_get_request((SERVER_API_URL + str('list_users_id')))
    response_time = h.get_response_time(response)

    body = h.get_response_body(response)

    assert response.ok
    assert response_time < 100
    assert isinstance(body, list)  # not empty
    assert len(body) != 0

    field_type = h.check_body_types_in_list(body)
    assert field_type == dict

@pytest.mark.happypath
def test_list_words():
    response = h.make_post_request_to_list_words(SERVER_API_URL + str('list_words'))
    response_time = h.get_response_time(response)

    body = h.get_response_body(response)

    assert response.ok
    assert response_time < 100
    assert isinstance(body, list)  # not empty
    assert len(body) != 0

    field_type = h.check_body_types_in_list(body)
    assert field_type == dict

@pytest.mark.happypath
def test_delete_user():
    response = h.make_get_request((SERVER_API_URL + str('list_users_id')))
    body = h.get_response_body(response)
    num_of_users = h.count_num_of_users(body)

    response = h.make_del_request((SERVER_API_URL + str('delete_user')))
    response_time = h.get_response_time(response)

    del_body = h.get_response_body(response)
    num_of_users_after_del = h.count_num_of_users(del_body)

    assert response.ok
    assert response_time < 100
    assert isinstance(body, list)  # not empty
    assert len(body) != 0
    assert num_of_users - num_of_users_after_del == 1

    field_type = h.check_body_types_in_list(del_body)
    assert field_type == dict

