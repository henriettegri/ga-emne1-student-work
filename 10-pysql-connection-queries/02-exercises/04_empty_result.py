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
                WHERE CountryCode = 'ZZZ' 
                ORDER BY Language ASC 
                    """)
            cursor.execute(sql)
            rows = cursor.fetchall()
            if not rows:
                print("No language found at this countrycode.")
            else:
                for language, percentage, is_official in rows:
                    print(f"{language}: {percentage}, {is_official}.")

            rader = len(rows)
            print(f"Antall rader: {rader}.")

except Error as e:
    print(f"Error using MySQL: {e}")

# en tom resultatliste er ikke det samme som en databasefeil. En databasefeil betyr at noe gikk galt. En tom liste er
# et gyldig resultat.
