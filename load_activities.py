# load_activities.py

import pandas as pd
from sqlalchemy import create_engine

# === Connexion à PostgreSQL ===
DB_NAME = "strava"
DB_USER = "airflow_user"
DB_PASSWORD = "test_strava"
DB_HOST = "localhost"
DB_PORT = "5432"

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# === Lecture du fichier CSV ===
csv_path = "data/activities.csv"
df = pd.read_csv(csv_path)

# === Envoi vers PostgreSQL ===
df.to_sql("activities", engine, if_exists="replace", index=False)

print("✅ Données insérées dans la table 'activities'")
