# from mysql.connector import *
import mysql.connector
mydb = mysql.connector.Connect(host="localhost",user="root",passwd="root",database="genraldb")
mycursor=mydb.cursor()
mycursor.execute("select * from userprofile")
for i in mycursor:
    print(i)
