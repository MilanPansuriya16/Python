# step 1: install the required mysql connector (pip install mysql-connector-python)
# step 2: import the library
# step 3: pass the host,encrypted password,username to make connection
# step 4: create database in MySQL 
# step 5: create table in MySQL 
# step 6: insert data in to the created table
# step 7: create cursor 
# step 8: user cursor to query the data 
# step 9: do some CRUD operation 
# step 10: commit the changes to the database 

import mysql.connector
from loguru import logger

connection = mysql.connector.connect(host = 'Localhost',
                                     user = 'root',
                                     password = 'Milu@1609',
                                     database = 'home_builder')

# logger.info(f"{connection}")      # To check the connection is established or not

'''
# read the data from databases
select_query = 'select * from labours_table'
cursor = connection.cursor()
cursor.execute(select_query)
result = cursor.fetchall()
logger.info(f"{result}")
'''

'''
# insert the data into the table
insert_query = 'insert into labours_table(name,role,wages) values(%s,%s,%s)'
cursor = connection.cursor()
cursor.execute(insert_query,('Rahul','labour',700))
connection.commit()
logger.info(f"Entry inserted in the table")
'''

'''
# delete the data from the table
delete_query = 'delete from labours_table where id = 7'
cursor = connection.cursor()
cursor.execute(delete_query)
connection.commit()
logger.info(f"Entry delete in the table")
'''



