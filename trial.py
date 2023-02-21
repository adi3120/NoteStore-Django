from mysql.connector import (connection)


# cnx = connection.MySQLConnection(user='adiuser1', password='MNMisBST@123',
#                                  host='ingeneors.rwlb.japan.rds.aliyuncs.com:3306',
#                                  database='ingeneors')
query="insert into customer values (%s,%s,%s,%s,%s,%s)"			
val=('00B','AMAN','singh',12029209,'aman@gmail.com','00CB')

import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='adiuser1', password='MNMisBST@123',
                                 host='ingeneors.rwlb.japan.rds.aliyuncs.com',
                                 database='ingeneors')


cursor = cnx.cursor()


cursor.execute(query,val)
cursor.execute("select * from customer")

for (cust_id,cust_fname,cust_lname,cust_phone,cust_email,cust_cart_id) in cursor:
	print(cust_fname,cust_id)

cnx.close()