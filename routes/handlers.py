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
    id = req_body['id']
    word_dict: Dict[str, str] = {'word': word, 'translate': translate}
    connection.insert_into_db(word, translate, id)
    appLogger.debug("Record inserted successfully into table")
    return jsonify(word_dict)


@handlers.route('/list_words')
def list_words() -> str:
    appLogger.debug('Processing list words request')
    user_id = '22'
    return jsonify(connection.select_to_db(user_id))
