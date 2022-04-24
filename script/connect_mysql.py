import mysql.connector
from mysql.connector import Error
# pip install mysql-connector-python

config = {
    'user': 'user',
    'password': 'password',
    'host': '192.168.2.120',
    'database': 'db',
    'port': '3306',
    'raise_on_warnings': True
}


def main():
    mysql_connection, cursor = connect()
    disconnect(mysql_connection, cursor)


def connect():
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            return connection, cursor
        else:
            print("Unable to connect.")
            exit()
    except Error as e:
        print("Error while connecting to MySQL", e)


def disconnect(connection, cursor):
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
