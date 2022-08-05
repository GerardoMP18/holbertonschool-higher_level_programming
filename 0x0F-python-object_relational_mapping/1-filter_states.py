#!/usr/bin/python3
""" Script to filter the names of states that star with the letter N """


import MySQLdb
from sys import argv

if __name__ == '__main__':

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE 'N%'")

    rows = cur.fetchall()

    for row in rows:
        print("{}".format(row))

    cur.close()
    conn.close()
