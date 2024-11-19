import numpy as np
import mysql.connector

connection = mysql.connector.connect( host = 'localhost'  ,  
database = "Assets"    , 
user = "root" ,        
password = "bhanu786pal"    
    )


if connection.is_connected():
    print('Connected')
cursor = connection.cursor()
cursor.execute("SHOW TABLES;")


tables = cursor.fetchall()

cursor.execute("SELECT * FROM work_orders ;")

headers = [i[0] for i in cursor.description]
print("Headers:", headers)

rows = cursor.fetchall()

for row in rows:
    print(row)


import pandas as pd
query = "SELECT * FROM work_orders"
Workorders= pd.read_sql(query, connection)


Workorders.head()

Workorders.isnull().sum()