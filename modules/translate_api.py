import requests
from typing import Dict
from logger import appLogger
from config import config


class TranslateApi:
    url: str
    key: str
    lang: str
    text: str

    def __init__(self, url: str, key: str, lang: str):
        self.url = url
        self.key = key
        self.lang = lang

    def get_translation(self, text: str) -> str:
        appLogger.debug('Making request to ya API')
        url = '{}?key={}&text={}&lang={}'.format(self.url, self.key, text, self.lang)
        try:
            response: requests.Response = requests.get(url)  # api
            word_data: Dict[str, any] = response.json()
            appLogger.info('Parsing translate response')
            translate: str = word_data['text'][0]
            return translate
        except Exception as err:
            appLogger.error("Error to get response from Yandex API", err)
            raise err


translate_config = config['YandexTranslateAPI']
translator: TranslateApi = TranslateApi(translate_config['url'], translate_config['key'], translate_config['lang']) #translator = TranslateApi(url, key, lang)
