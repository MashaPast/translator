import psycopg2
from logger import appLogger
from config import config


class Connection:
    user: str
    password: str
    host: str
    port: str
    database: str

    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.connection_to_db = psycopg2.connect(user=self.user, password=self.password, host=self.host, port=self.port,
                                                 database=self.database)

    def add_word(self, word, translate, user_id):
        cursor = self.connection_to_db.cursor()
        insert_words = '''INSERT INTO dict (WORD_ENG, WORD_TRANSLATION, USER_ID) VALUES (%s, %s, %s)'''
        values_to_insert: list = [word, translate, user_id]
        cursor.execute(insert_words, values_to_insert)
        self.connection_to_db.commit()

    def get_words(self, user_id) -> list:
        appLogger.debug("Selecting words from db")
        cursor = self.connection_to_db.cursor()
        select_list_words = '''SELECT * FROM dict WHERE USER_ID = %s order by ID desc LIMIT 10'''
        values_to_select: list = [user_id]
        cursor.execute(select_list_words, values_to_select)
        rows: list = cursor.fetchall()
        appLogger.debug('Words listed from db')
        words = []
        for row in rows:
            word_dict = {
                'word': row[1],
                'translate': row[2]
            }
            words.append(word_dict)
        return words

    def get_users_and_words(self) -> list:
        appLogger.debug('Selecting unique users')
        cursor = self.connection_to_db.cursor()
        select_users = '''SELECT user_id, COUNT(word_eng) FROM dict GROUP BY user_id'''
        try:
            cursor.execute(select_users)
            list_of_users_and_words: list = cursor.fetchall()
            user_id_words = []
            for row in list_of_users_and_words:
                user_dict = {
                    'user id': row[0],
                    'number of words of the user': row[1]
                }
                user_id_words.append(user_dict)
            return user_id_words
        except Exception as err:
            appLogger.error(err)
            raise err



    def delete_user(self, user_id) -> None:
        appLogger.debug('Delete user')
        cursor = self.connection_to_db.cursor()
        delete_user = '''DELETE FROM dict WHERE USER_ID = %s'''
        values_to_delete: list = [user_id]
        try:
            cursor.execute(delete_user, values_to_delete)
            self.connection_to_db.commit()
        except Exception as err:
            appLogger.error(err)
            raise err

pg_config = config['PostgresSection']
connection = Connection(pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'], pg_config['database'])
appLogger.debug('Connection created')
