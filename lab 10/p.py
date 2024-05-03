import psycopg2
try:
    connection = psycopg2.connect(
        dbname="postgres3",
        user="postgres",
        password="12345678",
        host="localhost",
        port="5432"
    )
    print("Connected to PostgreSQL!")
except psycopg2.Error as e:
    print("Unable to connect to the database:", e)
cursor = connection.cursor()
