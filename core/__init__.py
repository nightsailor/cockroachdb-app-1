import logging
import os
import psycopg2
from decouple import config
from flask import Flask

app = Flask(__name__)

def print_hello(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT message FROM messages")
        logging.debug("print_hello(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # for row in rows:
        #     print(row[0])
        print(rows)
def main():
    # conn_string = input('Enter a connection string:\n')

    conn_string = config('CONNECTION_STRING', default='guess_me')

    conn = psycopg2.connect(os.path.expandvars(conn_string))
    print_hello(conn)

    # Close communication with the database.
    conn.close()

main()

from core import app1