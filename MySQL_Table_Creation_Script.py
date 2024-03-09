# MySQL Table Creation Script
#
# This script connects to a MySQL database and creates a new table named `YAIK` 
# within a schema named `meta`. The `YAIK` table is intended to store student 
# information, including their ID, names, registration date, class, and course name.

import mysql.connector  # Import the mysql.connector module to work with MySQL

try:
    # Establish a connection to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost",  # Database server address
        user="root",       # Database username
        password="2507",   # User's password
        # Note: The database parameter is not provided here, ensure the `meta` schema exists.
    )

    print(mydb)  # Print the connection object (useful for debugging)

    # Create a cursor object using the connection
    mycursor = mydb.cursor()

    # SQL statement to create a new table named `YAIK` in the `meta` schema
    mycursor.execute('''CREATE TABLE meta.YAIK (
                        studentid INT,
                        firstname VARCHAR(50),
                        lastname VARCHAR(50),
                        registrationdate DATE,
                        class VARCHAR(50),
                        course_name VARCHAR(50))''')

    print("Table created successfully")  # Inform the user that the table was created

except mysql.connector.Error as error:  # Catch any errors that occur during the process
    print(f"Failed to create table in MySQL: {error}")  # Print the error

finally:
    # Ensure that the connection to the database is closed properly
    if mydb.is_connected():
        mycursor.close()  # Close the cursor
        mydb.close()       # Close the connection
        print("MySQL connection is closed")  # Inform the user
