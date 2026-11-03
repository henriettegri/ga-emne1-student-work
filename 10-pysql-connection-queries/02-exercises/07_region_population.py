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
        region = input("Enter a region: ")
        hest = input("Enter lowest population: ")
        #min_population = int(input("Enter lowest population: ")
        min_population = int(hest)
        with connection.cursor() as cursor:
            sql = ("""
                SELECT name, Population
                FROM country
                WHERE  Region = %s AND population >= %s
                ORDER BY name ASC;
                    """)
            cursor.execute(sql, (region, min_population,))
            rows = cursor.fetchall()
            if not rows:
                print("No countries found in that region.")
            else:
                for name, pop in rows:
                    print(f"{name}: {pop}.")

            rader = len(rows)
            print(f"Antall rader: {rader}.")

except Error as e:
    print(f"Error using MySQL: {e}")

