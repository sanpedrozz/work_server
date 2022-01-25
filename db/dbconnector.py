import psycopg2
from psycopg2.extras import RealDictCursor


class DBConnector:
    def __init__(self, database: str, user: str, password: str, host: str, port: str):
        self.connect = psycopg2.connect(database=database,
                                        user=user,
                                        password=password,
                                        host=host,
                                        port=port,
                                        cursor_factory=RealDictCursor)
        self.cursor = self.connect.cursor()

    def fetchall_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert_query(self, query):
        self.cursor.execute(query)
        self.connect.commit()
