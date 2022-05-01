import mysql.connector
from mysql.connector import Error
import information_measure
# pip install mysql-connector-python

config = {
    'user': 'user',
    'password': 'password',
    'host': '192.168.2.120',
    'database': 'db',
    'port': '3306',
    'raise_on_warnings': True
}


def build_query():
    stats_arr = information_measure.retrieve()
    query = f"""INSERT INTO db.server_stats
            (timestamp, host, process_count, process_cpu_percentage, ping_min, ping_avg, ping_max, ping_dev, memory_total, memory_used, memory_free, memory_available, temp_cpu, temp_gpu)
        SELECT
        '{stats_arr["timestamp"]}' as timestamp,
        '{stats_arr["host"]}' as host,
        {stats_arr["process_count"]} as process_count,
        {stats_arr["process_cpu_percentage"]} as process_cpu_percentage,
        {stats_arr["ping_min"]} as ping_min,
        {stats_arr["ping_avg"]} as ping_avg,
        {stats_arr["ping_max"]} as ping_max,
        {stats_arr["ping_dev"]} as ping_dev,
        {stats_arr["memory_total"]} as memory_total,
        {stats_arr["memory_used"]} as memory_used,
        {stats_arr["memory_free"]} as memory_free,
        {stats_arr["memory_available"]} as memory_available,
        {stats_arr["temp_cpu"]} as temp_cpu,
        {stats_arr["temp_gpu"]} as temp_gpu;"""
    return query


def main():
    mysql_connection, cursor = connect()
    query = build_query()
    #print(query)
    cursor.execute(query)
    mysql_connection.commit()
    #print(cursor.rowcount, "Record inserted successfully into stats table")
    disconnect(mysql_connection, cursor)


def connect():
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            db_info = connection.get_server_info()
            #print("Connected to MySQL Server version ", db_info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            #print("You're connected to database: ", record)
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
        #print("MySQL connection is closed")


if __name__ == '__main__':
    main()
