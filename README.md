# Telegram Translator Bot
Telegram Translator Bot (TTB) is an application that translates English words into Russian and saves them to the database. 
TTB uses HTTP-based [Telegram Bot API](https://core.telegram.org/bots/api) and [Yandex Translator API](https://yandex.ru/dev/translate/doc/dg/concepts/about-docpage/). 
TTB provides two main commands: '/translate' command for translation of words and '/list_my_words' command for getting list of last 10 words, which user requested bot to translate.
To see bot options use command '/help'. The Admin API is developed, it is implemented with four endpoints and HTTP methods: Translate (POST method), List users id(GET method), List words by id(POST method), 
Delete user(DELETE method). All the methods are shown in Postman screenshots. The Admin API uses PostgreSQL database to store data. Tests for the Admin API are written with pytest framework using python. Test functions are marked for happypath and negative scenarios. 
Test report is generated with Allure test reporting tool. All prerequisites, instructions for running the tests and generating Allure report are presented in README.md on GitHub.

## Prerequisites
Your system should have the following to run TTB:
* Python_version = "3.7"
* PostgreSQL database version > 10
* Yandex Translator API Key
* Authorization token for Telegram bot

## Bot API

* Use command '/help' to see bot options.

![help](/images/help.png) <img src="/images/help.png" width=300 align=center>

* Use command '/translate' in format '/translate your_word' to get translation.

![translate](/images/translate_hi.png) <img src="/images/translate_hi.png" width=300 align=center>

* Use command '/list_my_words' to get list of last 10 words you requested me to translate. 

![list_my_words](/images/list_my_words.png) <img src="/images/list_my_words.png" width=300 align=center>

* Send 'thank you' to get a sticker.

![list_my_words](/images/thank_you.png) <img src="/images/thank_you.png" width=300 align=center>
                                 
## Admin API
###  Translate 

The Translate endpoint provides a translation of a word from English into Russian.

![translate endpoint](/images/translate.png)

###  List users id

The List users id endpoint provides number of requested words of each user.

![list_users_id endpoint](/images/list_users_id.png)

###  List words

The List words by id endpoint provides words of user by his id

![list_words endpoint](/images/list_words.png)

###  Delete user

The Delete user endpoint provides removing user by his id 

![delete_user endpoint](/images/delete_user.png)

## Running the tests
* Running all tests
```bash
pytest -s -v test_API/
```
* Selecting marked test functions for a run
```bash
pytest -v -m negative
```

## Allure report

* Generating Allure test report

```bash
pytest --alluredir=./results test_API/
allure generate ./results -o ./allure-report
```
* Opening Allure test report in browser 
```bash
allure open allure-report/
```
Allure overview page

![allure_report_overview](/images/allure_report_overview.png)

Allure test suits page

![allure_test_suits](/images/allure_test_suits.png)

Allure graphs

![allure_graphs](/images/allure_graphs.png)
