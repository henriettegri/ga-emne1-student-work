#try:
#import mysql.connector
#except:
#   print("Importen mislykkes.")

#else:
#    print('MySQL-pakka er klar.')


import mysql.connector
from mysql.connector import Error

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
            sql = (
                "SELECT Name, Population "
                "FROM city "
                "WHERE CountryCode = 'NOR'"
            )
            #trenger ikke semikolon inne i en python-streng, må ha mellomrom mellom spørring og dobbelfnutt
            #følg med på at fargene er riktig
            cursor.execute(sql)
            rows = cursor.fetchall()
            if not rows:
                print("No cities found.")
            else:
                for name, population in rows:
                    print(f'{name}: {population}')
except Error as e:
    print(f"Error using MySQL: {e}")