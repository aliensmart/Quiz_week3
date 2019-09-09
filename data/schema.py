import sqlite3
import os
import csv

DIR = os.path.dirname(__file__)
DBFILENAME = "tsla.db"
DBPATH = os.path.join(DIR, DBFILENAME)

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as connection:
        cur = connection.cursor()
        SQL = "DROP TABLE IF EXISTS tsla; "
        cur.execute(SQL)

        SQL = """
            CREATE TABLE tsla(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                open FLOAT,
                high FLOAT,
                low FLOAT,
                close FLOAT,
                adjust_close FLOAT,
                volume FLOAT
            );
        """
