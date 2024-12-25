import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
mydb = mysql.connector.connect(
   host=os.environ.get('DB_HOST'),
   user=os.environ.get('DB_USER'),
   passwd=os.environ.get('DB_PASSWORD'),
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE users")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
   print(db)