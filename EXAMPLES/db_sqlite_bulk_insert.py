#!/usr/bin/env python
import os
import sqlite3
import random

FRUITS = ["pomegranate", "cherry", "apricot", "date", "apple",
          "lemon", "kiwi", "orange", "lime", "watermelon", "guava",
          "papaya", "fig", "pear", "banana", "tamarind", "persimmon",
          "elderberry", "peach", "blueberry", "lychee", "grape"]

DB_NAME = 'fruitprices.db'  # <1>

CREATE_TABLE = """
create table fruit (
    name varchar(30),
    price decimal
)
"""  # <2>

INSERT = '''
insert into fruit (name, price) values (?, ?)
'''  # <3>


def main():  # 'main' is not a keyword
    """
    Program entry point.

    :return: None
    """
    conn = get_connection()
    create_database(conn)
    populate_database(conn)

    read_database()


def get_connection():
    """
    Get a connection to the PRODUCE database

    :return: SQLite3 connection object.
    """
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)  # <4>

    s3conn = sqlite3.connect(DB_NAME)  # <5>
    return s3conn


def create_database(conn):
    """
    Create the fruit table

    :param conn: The database connection
    :return: None
    """
    conn.execute(CREATE_TABLE)  # <6>


def populate_database(conn):
    """
    Add rows to the fruit table

    :param conn: The database connection
    :return: None
    """

    INSERT = '''
    insert into fruit (name, price) values (?, ?)
    '''  # <3>

    fruit_data = get_fruit_data()  # [('apple', .49), ('kiwi', .38)]

    for i, fruit_info in enumerate(fruit_data, 1):
        try:
            for fruit_info in fruit_data:
                print("fruit_info:", fruit_info)
                conn.execute(INSERT, fruit_info)
            # conn.executemany(INSERT, fruit_data) # short cut for the previous lines
        except sqlite3.DatabaseError as err:
            print(err)
            conn.rollback()
        if i % 5 == 0:
            print("Committing")
            conn.commit()

def get_fruit_data():
    """
    Create iterable of fruit records.

    :return: Generator of name/price tuples.
    """
    return ((f, round(random.random() * 10 + 5, 2)) for f in FRUITS)  # <9>


def read_database():
    conn = sqlite3.connect(DB_NAME)
    for name, price in conn.execute('select name, price from fruit'):
        print('{:12s} {:6.2f}'.format(name, price))


if __name__ == '__main__':
    main()
