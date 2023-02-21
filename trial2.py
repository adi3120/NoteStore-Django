import mysql.connector

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

path=r"D:\projects\alibaba\myEnv\demo1\eminem.jpg"

connection = mysql.connector.connect(host='localhost',
                                             database='testing',
                                             user='root',
                                             password='MNMisBST@123')

cursor = connection.cursor()
# sql_insert_blob_query = """ INSERT INTO photos(name,photo) VALUES (%s,%s)"""

# empPicture = convertToBinaryData(path)

# val=("eminem",empPicture)
# result = cursor.execute(sql_insert_blob_query, val)


# connection.commit()

query="SELECT * from photos"

cursor.execute(query)

for (id,name,photo) in cursor:
	print(id,name)
	write_file(photo,"MYPIC.jpeg")


