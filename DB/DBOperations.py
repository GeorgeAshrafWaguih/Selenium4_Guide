import mysql.connector

# insert , update , delete
insert_query = "insert into student values(104, 'Kim)"
update_query = "update student set sname='Geo' where sid=104"
delete_query = "delete from student where sid=104"

# insert
try:
    connection = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")
    cursor = connection.cursor()  # create a cursor
    cursor.execute(insert_query)  # execute query
    connection.commit()  # commit
    connection.close()
    print("Record Added")
except:
    print("Connection unsuccessful")

# update
try:
    connection = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")
    cursor = connection.cursor()  # create a cursor
    cursor.execute(update_query)  # execute query
    connection.commit()  # commit
    connection.close()
    print("Record Added")
except:
    print("Connection unsuccessful")

# delete
try:
    connection = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")
    cursor = connection.cursor()  # create a cursor
    cursor.execute(delete_query)  # execute query
    connection.commit()  # commit
    connection.close()
    print("Record Added")
except:
    print("Connection unsuccessful")