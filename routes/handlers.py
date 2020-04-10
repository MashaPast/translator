from flask import request, jsonify
from typing import Dict
from flask import Blueprint
from modules.translate_api import translator
from logger import appLogger
from modules.db_connection import connection


handlers = Blueprint('handlers', __name__)


@handlers.route('/translate', methods=['POST'])
def translate_route() -> (str, int):
    appLogger.debug('Processing translate request')
    try:
        req_body: dict = request.get_json()
        word: str = req_body['word']
        user_id: str = req_body['user_id']
    except Exception as err: #dif exc
        appLogger.error("Bad request error", err)
        data = {"message": "Bad request error"}
        return jsonify(data), 400

    try:
        translate: str = translator.get_translation(word)
        word_dict: Dict[str, str] = {'word': word, 'translate': translate}
        connection.add_word(word, translate, user_id)
        appLogger.debug("Record inserted successfully into table")
        return jsonify(word_dict)
    except Exception as err: #dif exc
        appLogger.error("Error to get response from Yandex API", err)
        data = {"message": "Internal server error"}
        return jsonify(data), 500


@handlers.route('/list_words_by_id', methods=['POST'])
def list_words() -> (str, int):
    try:
        appLogger.debug('Processing list words request')
        req_body: dict = request.get_json()
        user_id: str = req_body['user_id']
    except Exception as err:
        appLogger.error("Bad request error", err)
        data = {"message": "Bad request error"}
        return jsonify(data), 400

    try:
        return jsonify(connection.get_words(user_id))
    except Exception as e:
        data = {"message": "Internal server error"}
        return jsonify(data), 500


@handlers.route('/list_users_id', methods=['GET'])
def list_users_id() -> (str, int):
    appLogger.debug('Printing unique user_id')
    try:
        data = connection.get_users_and_words()
        return jsonify(data)
    except Exception as e:
        data = {"message": "Internal server error"}
        return jsonify(data), 500


@handlers.route('/delete_user', methods=['DELETE'])
def delete_user() -> (str, int):
    try:
        appLogger.debug('Processing delete user')
        req_body: dict = request.get_json()
        user_id: str = req_body['user_id']
    except Exception as err: #dif exc
        appLogger.error("Bad request error", err)
        data = {"message": "Bad request error"}
        return jsonify(data), 400
    try:
        connection.delete_user(user_id)
        appLogger.debug("Record deleted successfully from the table")
        data_after_removal = connection.get_users_and_words()
        return jsonify(data_after_removal)
    except Exception as e:
        data = {"message": "Internal server error"}
        return jsonify(data), 500
