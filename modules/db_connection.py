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

    def insert_into_db(self, word, translate, user_id):
        cursor = self.connection_to_db.cursor()
        insert_words = '''INSERT INTO dict_for_bot (WORD_IN_ENG, WORD_TRANSLATION, USER_ID) VALUES (%s, %s, %s)'''
        values_to_insert = (word, translate, user_id)
        cursor.execute(insert_words, values_to_insert)
        self.connection_to_db.commit()

    def select_to_db(self) -> list:
        cursor = self.connection_to_db.cursor()
        select_list_words = """select * from dict_for_bot"""
        cursor.execute(select_list_words)
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


pg_config = config['PostgresSection']
connection = Connection(pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'], pg_config['database'])
appLogger.debug('Connection created')
