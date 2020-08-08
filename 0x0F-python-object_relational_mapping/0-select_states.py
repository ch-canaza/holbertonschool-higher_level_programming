#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa:"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         pep8db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from states ORDER BY states.id")
    states = cur.fetchall()
    for state in states:
        print("{}".format(state))
    cur.close()
    db.close()
