from flask import request, jsonify
from typing import Dict
from flask import Blueprint
from modules.translate_api import translator
from logger import appLogger
from modules.db_connection import connection


handlers = Blueprint('handlers', __name__)


@handlers.route('/translate', methods=['POST'])
def translate_route() -> str:
    appLogger.debug('Processing translate request')
    req_body: dict = request.get_json()
    print(req_body)
    word: str = req_body['word']
    translate: str = translator.get_translation(word)
    word_dict: Dict[str, str] = {'word': word, 'translate': translate}
    connection.add_word(word, translate)
    appLogger.debug("Record inserted successfully into table")
    return jsonify(word_dict)


@handlers.route('/list_words')
def list_words() -> str:
    appLogger.debug('Processing list words request')
    return jsonify(connection.get_words())

@handlers.route('/list_users_id')
def list_users_id() -> (str, int):
    appLogger.debug('Printing unique user_id')
    try:
        data = connection.get_users_and_words()
        return jsonify(data)
    except Exception as e:
        data = {"message": "Internal server error"}
        return jsonify(data), 500


@handlers.route('/delete_user', methods=['DELETE'])
def delete_user():
    appLogger.debug('Processing delete user')
    req_body: dict = request.get_json()
    user_id: str = req_body['user_id']
    try:
        connection.delete_user(user_id)
        appLogger.debug("Record deleted successfully from the table")
        data_after_removal = connection.get_users_and_words()
        return jsonify(data_after_removal)
    except Exception as e:
        data = {"message": "Internal server error"}
        return jsonify(data), 500
