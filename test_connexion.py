import psycopg2

conn = psycopg2.connect(
    dbname="xxx",
    user="xxx",
    password="xxx",
    host="localhost",
    port="5432"
)

print("✅ Connexion PostgreSQL réussie !")
conn.close()
