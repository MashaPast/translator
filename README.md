# Telegram Translator Bot
Telegram Translator Bot (TTB) is an application that translates English words into Russian and stores them for each user in the database. TTB uses HTTP-based [Telegram Bot API](https://core.telegram.org/bots/api) and [Yandex Translator API](https://yandex.ru/dev/translate/doc/dg/concepts/about-docpage/).
TTB provides three main commands:
- '/translate' - to translate word
- '/list_my_words' - to get a list of last 10 words, which user requested the TTB to translate
- '/help' - to see TTB options

Server application exposes the Admin API, it is implemented with four HTTP endpoints:
- 'POST /translate' - to translate word
- 'GET /list_users_id' - to get number of requested words of each user
- 'POST /list_words_by_id' - to get words of user by his id
- 'DELETE /delete_user' - to delete user by his id

All the methods are shown in Postman screenshots. Server application utilizes PostgreSQL database to store data.

Tests for the Admin API are written with pytest framework using python 3. Test functions are marked as happypath and negative scenarios.

Test report is generated with Allure test reporting tool. All prerequisites, instructions for running the tests and generating Allure report are presented in README.md on GitHub.
## Prerequisites
Your system should have the following to run TTB:
* Python_version = "3.7"
* PostgreSQL database version > 10
* Yandex Translator API Key
* Authorization token for Telegram bot

## Bot API

* Use command '/help' to see bot options.

<img src="/images/help.png" width=300 align=center>

* Use command '/translate' in format '/translate your_word' to get translation.

<img src="/images/translate_hi.png" width=300 align=center>

* Use command '/list_my_words' to get list of last 10 words you requested me to translate. 

<img src="/images/list_my_words.png" width=300 align=center>

* Send 'thank you' to get a sticker.

<img src="/images/thank_you.png" width=300 align=center>
                                 
## Admin API
###  Translate 

'POST /translate' endpoint provides a translation of a word from English into Russian.

![translate endpoint](/images/translate.png)

###  List users id

'GET /list_users_id' endpoint provides number of requested words of each user.

![list_users_id endpoint](/images/list_users_id.png)

###  List words

'POST /list_words_by_id' endpoint provides words of user by his id

![list_words endpoint](/images/list_words.png)

###  Delete user

'DELETE /delete_user' endpoint provides removing user by his id 

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
