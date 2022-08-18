#!/usr/bin/python3
""" Get all state data """


import MySQLdb
from sys import argv

if __name__ == "__main__":

    conn = MySQLdb.connect(
            host="localhost",
            port=3306, user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8")

    # Creating a cursor object for query execution
    cur = conn.cursor()
    cur.execute('SELECT * FROM states \
                ORDER BY states.id')

    # data recovery
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
    cur.close()
    conn.close()
