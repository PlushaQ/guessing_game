import sqlite3

class DatabaseConnection:
    """
    Database connection context manager
    """
    def __init__(self, host: str):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()

class Database:
    def create_scores_table(self):
        with DatabaseConnection('scores.db') as connection:
            cursor = connection.cursor()

            cursor.execute('CREATE TABLE IF NOT EXISTS scores (id integer primary key, name text, score integer, range text)')
            

    def insert_new_scores(self, name, score, numbers_range):
        with DatabaseConnection('scores.db') as connection:
            cursor = connection.cursor()

            cursor.execute('INSERT INTO scores (name, score, range) VALUES (?, ?, ?)', (name, score, numbers_range))


    def get_top_ten_scores(self):
        with DatabaseConnection('scores.db') as connection:
            cursor = connection.cursor()
            
            cursor.execute('SELECT * FROM scores ORDER BY score LIMIT 10')
            scores = cursor.fetchall()
            return scores

