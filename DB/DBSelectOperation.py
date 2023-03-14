import mysql.connector

# select
select_query = "select * from orders"

try:
    connection = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")
    cursor = connection.cursor()  # create a cursor
    cursor.execute(select_query)  # execute query
    for row in cursor:
        print(row[0], row[1], row[2])     # Print the columns in each row
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