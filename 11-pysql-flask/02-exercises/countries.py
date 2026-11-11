import mysql.connector
from config_local import DB_CONFIG

def get_countries(region):
    sql= (
        "SELECT Name, Population "
        "FROM country "
        "WHERE Region = %s "
        "ORDER BY Name ASC"
    )
    with mysql.connector.connect(
        **DB_CONFIG
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, (region,))
            return cursor.fetchall()