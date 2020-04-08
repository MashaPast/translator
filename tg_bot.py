import telebot
from modules.translate_api import translator
from modules.db_connection import connection
from logger import appLogger
from config import config
import flag


bot = telebot.TeleBot(config['TelegramAPI']['token'])


@bot.message_handler(commands=['start'])
def start_message(message: telebot.types.Message):
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True, True, True)
    keyboard1.row('hi', 'quit', 'thank you', 'help')
    bot.send_message(message.chat.id, 'Hi', reply_markup=keyboard1)

@bot.message_handler(commands=['help'])
def help_message(message: telebot.types.Message):
    bot.send_message(message.chat.id, "This is a bot for translating words from English into Russian. \n" 
                                      "\n"
                                      "Use command '/start' to see keyboard options: hi, quit, thank you and help. \n"
                                       "\n"
                                      "Use command '/translate' in format '/translate your_word' to get translation. \n"
                                      "\n"
                                      "Use command '/list_my_words' to get list of last 10 words you requested me to translate. \n"
                                      "\n"
                                    "Translated by the Yandex.Translate service: http://translate.yandex.ru")



@bot.message_handler(commands=['list_my_words'])
def list_all_words(message: telebot.types.Message):
    appLogger.debug('Processing list words request')
    answer_from_db = (connection.get_words(message.from_user.id))
    answer_from_bot = ""
    for i in range((len(answer_from_db) - 1), -1, -1):
        str_of_word = answer_from_db[i]['word']
        print(type(str_of_word))
        str_of_translate = answer_from_db[i]['translate']
        answer_from_bot += flag.flagize(":GB:") + str_of_word + " - " + flag.flagize(":RU:") + str_of_translate + "\n"
    answer_from_bot += "\n" + "Translated by the Yandex.Translate service: http://translate.yandex.ru"
    bot.send_message(message.chat.id, answer_from_bot)


def return_param(message_to_translate: str):
    list_to_trnsl = message_to_translate.split()[1:]
    str_to_trnsl = ','.join(list_to_trnsl)
    return str_to_trnsl


@bot.message_handler(commands=['translate'])
def translate(message):
    try:
        word_to_translate = return_param(message.text)
        appLogger.debug('Getting translate from API')
        translate: str = translator.get_translation(word_to_translate.lower())
        if not word_to_translate == translate:
            connection.add_word(word_to_translate.lower(), translate, message.from_user.id)
            appLogger.debug("New word and translate inserted successfully into table")
            bot.send_message(message.chat.id, 'translation of your word:\n' + str(translate) + "\n" + "\n"
                             + "Translated by the Yandex.Translate service: http://translate.yandex.ru")
        else:
            bot.send_message(message.chat.id, 'You sent inappropriate word')
    except KeyError:
        bot.send_message(message.chat.id, "Add word you want to translate in format '/translate your_word'")


@bot.message_handler(content_types=['text'])
def answer_text(message: telebot.types.Message):
    if message.text.lower() == 'quit':
        bot.send_message(message.chat.id, 'Buy')
    elif message.text.lower() == 'hi':
        bot.send_message(message.chat.id, 'Please enter english word you want to translate')
    elif message.text.lower() == 'thank you':
        bot.send_sticker(message.chat.id, 'CAADBAADCQADDzYrCWNaDCjhhrNPFgQ')
    elif message.text.lower() == 'help':
        help_message(message)



@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


