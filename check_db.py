import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="chat",
  password="123"
)

mycursor = mydb.cursor()
# mycursor.execute("USE chatapp")
# mycursor.execute("SELECT 1 FROM 1 FROM `users`;")

mycursor.execute("SELECT id FROM users WHERE id;")
for x in mycursor:
  print(x)