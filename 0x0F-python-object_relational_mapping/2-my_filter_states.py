#!/usr/bin/python3
""" script que tome un argumento y muestre todos los valores en la statestabla\
    btn_0e_0_usadonde namecoincide con el argumento."""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name LIKE '{}' COLLATE latin1_general_cs\
                ORDER BY states.id".format(argv[4]))
    states = cur.fetchall()
    for state in states:
        print("{:}".format(state))
    cur.close()
    db.close()
