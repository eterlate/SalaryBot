import psycopg2
from config import *

import psycopg2



def connect_to_base():
    try:
        conn = psycopg2.connect(dbname=db_name, user=user, 
                        password=password, host=host)
        cursor = conn.cursor()
        print("Successfully connected...")
        return conn, cursor
    except Exception as ex:
        print("Bad connection")
        print(ex)

def close_connection(conn,cursor):
    conn.close()
    cursor.close()
    print('Connection closed...')