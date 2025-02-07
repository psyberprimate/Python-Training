import psycopg2
import json
import os
from psycopg2 import Error
from psycopg2 import pool
import database
from contextlib import contextmanager

login_file_path = "/Learning3/Poll/login.json"


class ConnectionPool():
    """Class for connecting to postgreSQL via simple connection pool.
    Takes json file 'login.json' for connection configurations.
    """

    _connection_pool = None

    @staticmethod
    def init(min_connection: int, max_connection: int,
             login_file_path: str = None):
        try:
            complete_path = os.path.join(
                os.getcwd()+os.path.normpath(login_file_path)
            )
            with open(complete_path, 'r') as json_file:
                data = json.load(json_file)

            ConnectionPool._connection_pool = pool.SimpleConnectionPool(minconn=min_connection,
                                                                        maxconn=max_connection,
                                                                        user=data['user'],
                                                                        password=data['password'],
                                                                        host=data['host'],
                                                                        port=data['port'],
                                                                        database=data['database'])
            if ConnectionPool._connection_pool:
                print("PostgreSQL connection pool is now open")

        except (Exception, Error) as error:
            print(f"Error while connecting to PostgreSQL: {error}")

    @staticmethod
    def get_connection():
        if ConnectionPool._connection_pool:
            try:
                return ConnectionPool._connection_pool.getconn()
            except Error as pgerror:
                print(pgerror)

    @staticmethod
    def release_connection(connection):
        if ConnectionPool._connection_pool:
            try:
                ConnectionPool._connection_pool.putconn(connection)
            except Exception as e:
                print(e)

    @contextmanager
    def auto_connect():
        """Gets a connection, yields it and release it back to pool afterwards
        """
        connection = ConnectionPool.get_connection()
        try:
            yield connection
        except Exception as pgerror:
            print(pgerror)
        finally:
            ConnectionPool.release_connection(connection)

    @staticmethod
    def disconnect():
        if ConnectionPool._connection_pool:
            try:
                ConnectionPool._connection_pool.closeall()
                print("PostgreSQL connection is closed")
            except Error as pgerror:
                print(pgerror)

    @staticmethod
    def get_information(connection):
        cursor = connection.cursor()
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters())
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print(f"Connected to: {record}", "\n")
        cursor.close()


if __name__ == "__main__":
    ConnectionPool.init(min_connection=1, max_connection=10,
                        login_file_path=login_file_path)
    connection = ConnectionPool.get_connection()
    ConnectionPool.get_information(connection)
    database.create_tables(database_connection=connection)
    ConnectionPool.disconnect()
