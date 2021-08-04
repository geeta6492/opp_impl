
import pymysql

connection =None
def get_database_connection():
    global connection
    if connection==None:
        connection = pymysql.connect("localhost","root","root","persist")
    #print(connection)
    return connection


#get_database_connection()
