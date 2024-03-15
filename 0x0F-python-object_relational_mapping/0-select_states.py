#!/usr/bin/python3

import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    con = db.cursor()
    con.execute("SELECT * FROM states ORDER BY id ASC")
    print(con.fetchall())
    con.close()
