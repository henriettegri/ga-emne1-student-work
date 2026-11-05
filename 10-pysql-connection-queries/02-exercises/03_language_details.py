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
            for language, percentage, is_official in rows:
                print(f"{language}: {percentage}%, {is_official}.")

            rader = len(rows)
            print(f"Antall rader: {rader}.")
            #print(f"Found {len(rows} language rows")

except Error as e:
    print(f"Error using MySQL: {e}")

# for-løkken trenger tre variabler fordi vi henter tre kolonner med select-spørringen. Rekkefølgen
# bestemmes av select-spørringen
#utpakkingen krever like mange variabler som det er verdier i tupelen.
