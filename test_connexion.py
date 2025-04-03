import psycopg2

conn = psycopg2.connect(
    dbname="strava",
    user="airflow_user",
    password="test_strava",
    host="localhost",
    port="5432"
)

print("✅ Connexion PostgreSQL réussie !")
conn.close()
