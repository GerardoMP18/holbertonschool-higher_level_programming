#!/usr/bin/python3
""" Script that list all cities from the database hbtn_0e_4_usa"""


import MySQLdb
from sys import argv

if __name__ == '__main__':

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    cur = conn.cursor()

    cur.execute("SELECT C.id, C.name, S.name \
                FROM cities C \
                INNER JOIN states S \
                ON C.state_id = S.id \
                ORDER BY C.id")

    rows = cur.fetchall()

    for row in rows:
        print("{}".format(row))

    cur.close()
    conn.close()
