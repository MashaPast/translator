import requests
from logger import appLogger
import json


def make_get_request(full_url):
    response = requests.get(full_url)
    appLogger.debug("Response status is {}".format(response.status_code))
    return response


def make_post_request_to_translate(full_url, data):
    header = {"content-type": "application/json"}
    response = requests.post(full_url, data=json.dumps(data), headers=header)
    appLogger.debug("Response status is {}".format(response.status_code))
    return response


def make_post_request_to_list_words(full_url, id):
    header = {"content-type": "application/json"}
    response = requests.post(full_url, data=json.dumps(id), headers=header)
    appLogger.debug("Response status is {}".format(response.status_code))
    return response


def make_del_request(full_url, id):
    header = {"content-type": "application/json"}
    response = requests.delete(full_url, data=json.dumps(id), headers=header)
    appLogger.debug("Response status is {}".format(response.status_code))
    return response

def count_num_of_users(resp_body):
    return len(resp_body)



def get_response_time(response):
    response_time = response.elapsed.total_seconds()
    appLogger.debug("Request completed in {} ms".format(response_time * 1000))
    return response_time * 1000


def get_response_body(response_for_body):
    body: list = response_for_body.json()
    appLogger.debug('Getting response body from API')
    return body


def check_body_types_in_list(json_data):
    for i in range(0, len(json_data)):
        field_type = (type(json_data[i]))
        appLogger.info('Check type ' + str(i) + str(field_type))
        return field_type


def check_body_types_in_list_of_dict(json_data):
    for row in json_data:
        return type(row['word']), type(row['translate'])
