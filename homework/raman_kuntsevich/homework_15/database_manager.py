import mysql.connector
import logging


class DatabaseManager:
    def __init__(self, host, port, user, password, database):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.connection = self.connect_to_database(host, port, user, password, database)

    def connect_to_database(self, host, port, user, password, database):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                passwd=password,
                database=database
            )
            if self.connection.is_connected():
                self.logger.info(f"Connected to the database: {database}")
                return self.connection
        except Exception as e:
            self.logger.info(f"Error: {e}")
            return None

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.logger.info("Connection closed")

    def execute_insert_query(self, query, data=None):
        try:
            cursor = self.connection.cursor()
            if data:
                cursor.executemany(query, data)
            else:
                cursor.execute(query)
            self.connection.commit()
            self.logger.info(f"Insert successful. Query: {query}, Data: {data}")
            result_ids = [cursor.lastrowid + i for i in range(len(data))]
            return result_ids
        except Exception as e:
            self.logger.info(f"Error: {e}")
            self.connection.rollback()

    def execute_select_query(self, query, data=None):
        try:
            cursor = self.connection.cursor(dictionary=True)
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            # self.logger.info(f"Select successful. Query: {query}, Data: {data}")
            result = cursor.fetchall()
            return result
        except Exception as e:
            self.logger.info(f"Error: {e}")
            return None

    def execute_update_query(self, query, data=None):
        try:
            cursor = self.connection.cursor()
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            self.connection.commit()
            self.logger.info(f"Update successful. Query: {query}, Data: {data}")
        except Exception as e:
            self.logger.info(f"Error: {e}")
            self.connection.rollback()
