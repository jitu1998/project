import mysql.connector

cnx = mysql.connector.connect(user='root', password='1234',host='localhost',database='project')
cnx.close()