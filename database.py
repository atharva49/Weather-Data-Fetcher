import mysql.connector
from mysql.connector import Error
from config import DB_HOST,DB_NAME,DB_PASSWORD,DB_USER

def get_db_connection():
    return mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB_NAME
    )

def create_weather_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INT AUTO_INCREMENT PRIMARY KEY,
            city VARCHAR(50),
            temperature FLOAT,
            description VARCHAR(100),
            datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    connection.commit()
    cursor.close()
    connection.close()
    print("Table created succesfully")

def insert_weather_data(city,temperature,description):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO weather (city, temperature, description)
            VALUES (%s, %s, %s)
        ''', (city, temperature, description))  # Ensure this is a tuple
        connection.commit()
        cursor.close()
        connection.close()
    except Error as e:
        print(f"Error: {e}")

def retrieve_weather_data():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM weather')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()
    except Error as e:
        print(f"Error: {e}")