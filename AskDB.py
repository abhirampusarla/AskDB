import mysql.connector
from mysql.connector import Error

#Function to check db is connected

def check_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',       
            user='root',   
            password='Your Own Password',  
            database='Enter Your Database name'  
        )

        if connection.is_connected():
            print("Connection successful!")
            db_info = connection.server_info
            print("MySQL Server version:", db_info)

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

# Run the function
check_db_connection()
