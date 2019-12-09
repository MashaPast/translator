import telebot
from modules.translate_api import translator
from modules.db_connection import connection
from logger import appLogger
from config import config
import flag

bot = telebot.TeleBot(config['TelegramAPI']['token'])


@bot.message_handler(commands=['start'])
def start_message(message: telebot.types.Message):
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True, True)
    keyboard1.row('hi', 'quit', 'miss you')
    bot.send_message(message.chat.id, 'Hi, Kotya', reply_markup=keyboard1)


@bot.message_handler(commands=['list_all'])
def list_all_words(message: telebot.types.Message):
    appLogger.debug('Processing list words request')
    answer_from_db = (connection.select_to_db(message.from_user.id))
    answer_from_bot = ""
    for i in range((len(answer_from_db) - 1), -1, -1):
        str_of_word = answer_from_db[i]['translate']
        str_of_translate = answer_from_db[i]['word']
        answer_from_bot += flag.flagize(":GB:") + str_of_word + " - " + flag.flagize(":RU:") + str_of_translate + "\n"
    bot.send_message(message.chat.id, answer_from_bot)


def return_param(message_to_translate: str):
    list_to_trnsl = message_to_translate.split()[1:]
    str_to_trnsl = ','.join(list_to_trnsl)
    return str_to_trnsl


@bot.message_handler(commands=['translate'])
def translate(message):
    word_to_translate = return_param(message.text)
    appLogger.debug('Getting translate from API')
    translate: str = translator.get_translation(word_to_translate.lower())
    if not word_to_translate == translate:
        connection.insert_into_db(word_to_translate.lower(), translate, message.from_user.id)
        appLogger.debug("New word and translate inserted successfully into table")
        bot.send_message(message.chat.id, 'translation of your word:\n' + str(translate))
    else:
        bot.send_message(message.chat.id, 'You sent inappropriate word')


@bot.message_handler(content_types=['text'])
def answer_text(message: telebot.types.Message):
    if message.text.lower() == 'quit':
        bot.send_message(message.chat.id, 'Buy')
    elif message.text.lower() == 'hi':
        bot.send_message(message.chat.id, 'Please enter english word you want to translate')
    elif message.text.lower() == 'miss you':
        bot.send_sticker(message.chat.id, 'CAADBAADCQADDzYrCWNaDCjhhrNPFgQ')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()