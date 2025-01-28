import sqlite3
import os

connection = sqlite3.connect(os.path.join(os.getcwd()+os.path.normcase("/Learning3/Journal/journal.db")))

def create_table():
    connection.execute("CREATE TABLE IF NOT EXISTS entries (entry_content TEXT, entry_date TEXT)")
    connection.commit()

def close_connection():
    connection.close()

def add_new_entry():
    entry_content = input("Tell me about today? \n")
    entry_date = input("Enter the date: \n")
    print(f"entry_content: {entry_content}, entry_date: {entry_date}")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO entries (entry_content, entry_date) VALUES ('{entry_content}', '{entry_date}');")
    connection.commit()

def see_entries():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM entries;")
    print()
    for index in cursor:
        print(f"{index[0]}\n{index[1]}\n")
        
if __name__ == '__main__':
    create_table()