# Telegram Translator Bot
Telegram Translator Bot (TTB) is an application that runs inside Telegram and translates english words into russian. 
TTB uses HTTP-based [Telegram Bot API](https://core.telegram.org/bots/api) and [Yandex Translator API](https://yandex.ru/dev/translate/doc/dg/concepts/about-docpage/). 
                                 
## Admin API
###  Translate 

The Translate endpoint provides a translation of a word from English into Russian.

![translate endpoint](/images/translate.png)

###  List users id

The List users id endpoint provides number of requested words of each user.

![list_users_id endpoint](/images/list_users_id.png)

###  List words

The List words endpoint provides words of user by his id

![list_words endpoint](/images/list_words.png)

###  Delete user

The Delete user endpoint provides removing user by his id 

![delete_user endpoint](/images/delete_user.png)

## Bot API

* Use command '/start' to see keyboard options.
* Use command '/translate' in format '/translate your_word' to get translation.
* Use command '/list_my_words' to get list of last 10 words you requested me to translate. 

## Running the tests

## Allure report