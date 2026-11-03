import mysql.connector
from mysql.connector import (Error)

try:
    print("Connecting to the database...")
    with mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="gokstad",
            database="world"
    ) as connection:
        print("Connected to MySQL!")
        with connection.cursor() as cursor:
            sql = (""" 


        """)
        cursor.execute(sql)
        rows = cursor.fetchall()
        if not rows:
            print("No.... found.")
        else:
            for ... in rows:
                print(f"{}")

except Error as e:
    print(f"Error using MySQL: {}")

