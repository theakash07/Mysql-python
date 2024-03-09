# MySQL Data Insertion Script
#
# This script connects to a MySQL database and inserts a single row of data into a specified table.
# The example uses a table named `YAIK` in the `sky` schema.

import mysql.connector  # Import the mysql.connector module to interact with MySQL

try:
    # Establish a connection to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost",  # Database server address
        user="root",       # Database username
        password="2507"    # User's password
    )

    print(mydb)  # Print the connection object, useful for debugging to confirm connection

    # Create a cursor object using the connection
    mycursor = mydb.cursor()

    # SQL statement to insert data into the `YAIK` table of the `sky` schema
    # Here, we insert values directly into columns: studentid, firstname, lastname, 
    # registrationdate, class, and course_name
    mycursor.execute("INSERT INTO sky.YAIK VALUES('001', 'akash', 'singh', '2004-07-01', 'sql', 'hola')")

except mysql.connector.Error as error:  # Catch any errors that occur during the database operations
    print(f"Failed to insert data into MySQL table: {error}")  # Print the error

finally:
    # This block ensures that the connection to the database is closed properly
    if mydb.is_connected():
        mydb.commit()  # Commit the transaction to make sure the insert is saved
        mycursor.close()  # Close the cursor
        mydb.close()       # Close the database connection
        print("MySQL connection is closed")  # Inform the user that the operation is complete
