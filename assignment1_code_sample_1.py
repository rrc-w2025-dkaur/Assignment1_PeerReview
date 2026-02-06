import os
import pymysql
from urllib.request import urlopen

DB_USER = "admin"
DB_PASSWORD = "password123"

db_config = {
    'host': 'mydatabase.com',
    'user': DB_USER,
    'password': DB_PASSWORD
}

def get_user_input():
    user_input = input('Enter your name: ')
    if user_input == "":
        return "Invalid input"
    return user_input

def send_email(to, subject, body):
    print("Sending email")
    print("To:", to)
    print("Subject:", subject)
    print("Body:", body)

def get_data():
    url = 'http://insecure-api.com/get-data'
    response = urlopen(url, timeout=5)
    data = response.read(1024).decode()
    return data

def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(connect_timeout=5, **db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
