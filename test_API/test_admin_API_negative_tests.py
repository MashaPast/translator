import pytest
from helpers import helpers_func as h

SERVER_API_URL = 'http://127.0.0.1:5000/'
LIMIT_OF_RESPONSE_TIME = 400

@pytest.mark.negative
def test_translate_response_400():
    word_and_id = [{
        "asakjsadj": "flower",
        "user_id": "24"
    }]
    response = h.make_post_request_to_translate((SERVER_API_URL + str('translate')), word_and_id)
    response_time = h.get_response_time(response)

    body = h.get_response_body(response)

    assert response.status_code == 400
    assert response_time < LIMIT_OF_RESPONSE_TIME
    assert isinstance(body, dict)
    assert body != {} #not empty

    assert body == {"message": "Bad request error"}


@pytest.mark.negative
def test_list_words_by_id_response_400():
    user_id = [{
        "user_id": "22"
    }]
    response = h.make_post_request_to_list_words(SERVER_API_URL + str('list_words_by_id'), user_id)
    response_time = h.get_response_time(response)

    body = h.get_response_body(response)

    assert response.status_code == 400
    assert response_time < LIMIT_OF_RESPONSE_TIME
    assert isinstance(body, dict)
    assert len(body) != 0


@pytest.mark.negative
def test_delete_user_response_400():
    user_to_del = [{
        "wwqdqd": "22"
    }]

    response = h.make_del_request((SERVER_API_URL + str('delete_user')), user_to_del)
    response_time = h.get_response_time(response)
    del_body = h.get_response_body(response)

    assert response.status_code == 400
    assert response_time < LIMIT_OF_RESPONSE_TIME
    assert isinstance(del_body, dict)
    assert len(del_body) != 0

