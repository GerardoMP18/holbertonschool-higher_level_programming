#!/usr/bin/python3
""" Script that takes in the name of a state as an argument and list all
    cities of that state, using the database hbtn_0e_4_usa """


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
    cur.execute("SELECT cities.name \
                 FROM cities \
                 INNER JOIN states \
                 ON cities.state_id = states.id \
                 WHERE states.name = %s \
                 ORDER BY cities.id", (argv[4],))

    rows = cur.fetchall()

    data = []
    separator = ", "

    for row in rows:
        data.append(row[0])
    print(separator.join(data))

    cur.close()
    conn.close()
