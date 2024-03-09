# Import the MySQL connector module
import mysql.connector

# Establish a connection to the MySQL server
mydb = mysql.connector.connect(
    host="localhost",     # Specify the host where the MySQL server is running (in this case, it's localhost)
    user="root",          # Provide the username for connecting to the MySQL server
    password="2507"        # Provide the password for the specified user
)

# Print the connection object to verify the connection
print(mydb)

# Create a cursor object to interact with the MySQL server
mycursor = mydb.cursor()

# Execute a SQL query to show all available databases
mycursor.execute("SHOW DATABASES;")

# Iterate through the result set and print each database name
for x in mycursor:
    print(x)
