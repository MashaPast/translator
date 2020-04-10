import pytest
from helpers import helpers_func as h

SERVER_API_URL = 'http://127.0.0.1:5000/'
LIMIT_OF_RESPONSE_TIME = 400


@pytest.mark.happypath
@pytest.mark.parametrize('word_and_id', [{
        "word": "flower",
        "user_id": "24"
    },
    {
        "word": "1321",
        "user_id": "24"
    }])
def test_translate(word_and_id):
    response = h.make_post_request_to_translate((SERVER_API_URL + str('translate')), word_and_id)
    response_time = h.get_response_time(response)

    body = h.get_response_body(response)

    assert response.ok
    assert response_time < LIMIT_OF_RESPONSE_TIME
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
    assert response_time < LIMIT_OF_RESPONSE_TIME
    assert isinstance(body, list)  # not empty
    assert len(body) != 0

    field_type = h.check_body_types_in_list(body)
    assert field_type == dict

@pytest.mark.happypath
@pytest.mark.parametrize('user_id', [{
        "user_id": "107269932"
    },
    {
        "user_id": "402614150"
    }])
def test_list_words_by_id(user_id):
    response = h.make_post_request_to_list_words(SERVER_API_URL + str('list_words_by_id'), user_id)
    response_time = h.get_response_time(response)

    body = h.get_response_body(response)

    assert response.ok
    assert response_time < LIMIT_OF_RESPONSE_TIME
    assert isinstance(body, list)  # not empty
    assert len(body) != 0

    field_type = h.check_body_types_in_list(body)
    assert field_type == dict

@pytest.mark.happypath
def test_delete_user():
    word_and_id_to_post = {
        "word": "flower",
        "user_id": "22"
    }
    h.make_post_request_to_translate((SERVER_API_URL + str('translate')), word_and_id_to_post)
    user_to_del = {
        "user_id": "22"
    }
    response_get = h.make_get_request(SERVER_API_URL + str('list_users_id'))
    body = h.get_response_body(response_get)
    num_of_users = h.count_num_of_users(body)

    response_del = h.make_del_request((SERVER_API_URL + str('delete_user')), user_to_del)
    response_time = h.get_response_time(response_del)

    del_body = h.get_response_body(response_del)
    num_of_users_after_del = h.count_num_of_users(del_body)

    assert response_del.ok
    assert response_time < LIMIT_OF_RESPONSE_TIME
    assert isinstance(del_body, list)  # not empty
    assert len(del_body) != 0
    assert num_of_users - num_of_users_after_del == 1

    field_type = h.check_body_types_in_list(del_body)
    assert field_type == dict


