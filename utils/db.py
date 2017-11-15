__author__ = 'kathan'

import os
import sqlite3
from web import Storage

app_path = os.path.abspath(__file__ + "/../..")
DATABASE = os.path.join(app_path, 'rover_db.db')


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = namedtuple_factory

    return connection


def namedtuple_factory(cursor, row):
    fields = [col[0] for col in cursor.description]
    return Storage(dict(zip(fields, row)))


def execute_script(script):
    conn = get_connection()
    if not conn:
        raise Exception("Connection lost with database")

    cursor = conn.cursor()

    error = None
    try:
        cursor.executescript(script)
    except Exception, e:
        error = e
        cursor.connection.rollback()
    else:
        conn.commit()
    finally:
        conn.close()

    if error:
        raise error


def execute_statement(query, query_values):
    conn = get_connection()
    if not conn:
        raise Exception("Connection lost with database")

    cursor = conn.cursor()

    error = None
    try:
        cursor.execute(query, query_values)
    except Exception, e:
        error = e
        cursor.connection.rollback()
    else:
        conn.commit()
    finally:
        conn.close()

    if error:
        raise error


def fetch_one(query, query_values):
    conn = get_connection()
    if not conn:
        raise Exception("Connection lost with database")

    cursor = conn.cursor()

    try:
        cursor.execute(query, query_values)
        row = cursor.fetchone()
    except Exception, e:
        raise e
    finally:
        conn.close()

    return row


def fetch_all(query):
    conn = get_connection()
    if not conn:
        raise Exception("Connection lost with database")

    cursor = conn.cursor()

    try:
        cursor.execute(query)
        rows = cursor.fetchall()
    except Exception, e:
        raise e
    finally:
        conn.close()

    return rows