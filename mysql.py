from __future__ import print_function

hostname = 'localhost'
username = 'charles'
password = ''
database = 'mysql'

def doQuery(conn):
    cur = conn.cursor()

    cur.execute("Select fname, lname FROM employee")

    for firstname, lastname in cur.fetchall():
        print(firstname, lastname)


print("Using mysqlclient (MySQLdb):")
import MySQLdb
MyConnection = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database)
doQuery(myConnection)
myConnection.close()

print("Using pymysql:")
import pymysql
MyConnection = pymysql.connect(host=hostname, user=username, passwd=password, db=database)
doQuery(myConnection)
myConnection.close()