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
                SELECT Language, Percentage, IsOfficial 
                FROM countrylanguage 
                WHERE CountryCode = 'SWE' 
                ORDER BY Language ASC 
                    """)
            cursor.execute(sql)
            rows = cursor.fetchall()
            if not rows:
                print("No language found.")
            else:
                for language, percentage, is_official in rows:
                    print(f"{language}: {percentage}, {is_official}.")

            rader = len(rows)
            print(f"Antall rader: {rader}.")

except Error as e:
    print(f"Error using MySQL: {e}")

# for-løkken trenger tre variabler fordi vi henter tre kolonner med select-spørringen. 
