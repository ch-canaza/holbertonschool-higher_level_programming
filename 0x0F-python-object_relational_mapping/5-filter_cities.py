#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa:"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON states.id = cities.state_id\
                WHERE states.name=%s \
                ORDER BY cities.id", (argv[4],))
    cities = cur.fetchall()
    word_counter = 0
    for city in cities:
        if word_counter != 0:
            print(", ", end="")
        print("%s" % city, end="")
        word_counter += 1
    print("")
    cur.close()
    db.close()
