#!/usr/bin/python3
''' lists all states with name matches argument passed
and safe from sql injection '''

import sys
import MySQLdb


if __name__ == '__main__':

    try:
        sql_user = sys.argv[1]
        sql_pass = sys.argv[2]
        db_name = sys.argv[3]
        match = sys.argv[4]

        db = MySQLdb.connect(user=sql_user, passwd=sql_pass,
                             db=db_name, host='localhost', port=3306)
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name=%s\
                    ORDER BY states.id ASC".format(match))
        states = cur.fetchall()
        for state in states:
            print(state)

    except EXCEPTION as e:
        pass
