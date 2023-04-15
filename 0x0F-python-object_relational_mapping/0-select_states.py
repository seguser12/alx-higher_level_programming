#!/usr/bin/python3
'''lists all states from the database'''

import sys
import MySQLdb


if __name__ == '__main__':

    try:
        sql_user = sys.argv[1]
        sql_pass = sys.argv[2]
        db_name = sys.argv[3]

        my_host = 'localhost'
        port = 3306

        db = MySQLdb.connect(host=my_host, user=sql_user,
                             passwd=sql_pass, db=db_name,
                             host=my_host, port=port)

        cur = db.cursor()
        cur.execute('SELECT * FROM states ORDER BY states.id ASC')
        states = cur.fetchall()

        for state in states:
            print(state)

        cur.close()
        db.close()
    except Exception as e:
        pass
