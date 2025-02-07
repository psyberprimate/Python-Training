import psycopg2
import json
import os
from psycopg2 import Error
from poll import Poll

login_file_path = "/Learning3/Poll/login.json"

class Connection():
    """Class for connecting to postgreSQL. Takes json file 'login.json' for connection configurations.
    """
    def __init__(self, login_file_path : str = None):
            with open(os.path.join(
                os.getcwd()+os.path.normcase(login_file_path))) as json_file:
                data = json.load(json_file)
            try:
                self.connection = psycopg2.connect(user=data['user'],
                                            password=data['password'],
                                            host=data['host'],
                                            port=data['port'],
                                            database=data['database'])
            except (Exception, Error) as error:
                print(f"Error while connecting to PostgreSQL: {error}")

    def disconnect(self):
        self.connection.close()
        print("PostgreSQL connection is closed")
        
    def get_information(self):
        cursor = self.connection.cursor()
        print("PostgreSQL server information")
        print(self.connection.get_dsn_parameters())
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print(f"Connected to: {record}", "\n")
        cursor.close()
            
if __name__ == "__main__":
    connect = Connection(login_file_path=login_file_path)
    connect.get_information()
    poll = Poll(connection_instance=connect)
    poll.create_tables()
    connect.disconnect()