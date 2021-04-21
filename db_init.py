import mysql.connector
from mysql.connector import Error
import pandas as pd
import configs


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def database_init(create_database=False):
    create_database_query = "CREATE DATABASE scheduler"
    check_database_exists_query = "SHOW DATABASES LIKE scheduler"
    connection = create_server_connection(host_name=configs.HOST_NAME, user_name=configs.USER_NAME,
                                          user_password=configs.PASSWORD)
    if not execute_query(connection, check_database_exists_query):
        execute_query(connection, create_database_query)
    return connection
