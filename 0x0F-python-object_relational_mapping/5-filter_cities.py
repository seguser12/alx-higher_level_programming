#!/usr/bin/python3
''' lists all cities in a state matching argument'''

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
        cur.execute("SELECT cities.name\
                    FROM cities LEFT JOIN states\
                    ON states.id=cities.state_id\
                    WHERE states.name=%s\
                    ORDER BY cities.id ASC", match)
        cities = cur.fetchall()
        for city in cities:
            print(cities)

    except EXCEPTION as e:
        pass
