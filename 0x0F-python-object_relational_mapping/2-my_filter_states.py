#!/usr/bin/python3
"""Script to filter states with arguments"""


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
                WHERE name = %s \
                ORDER BY states.id", (argv[4],))

    rows =  cur.fetchall()

    for row in rows:
        print("{}".format(row))
        
    cur.close()
    conn.close()

