import requests
import pandas as pd
from sqlalchemy import create_engine
import json
import time
from datetime import datetime

# === Identifiants API ===
STRAVA_CLIENT_ID = "153745"
STRAVA_CLIENT_SECRET = "7f4fd98d47e32b6432759f6d1b80022fa649083f"
STRAVA_REFRESH_TOKEN = "9fa66efea2fba60cd88bac01a1d76dc5822bb17b"

# === Connexion PostgreSQL ===
DB_NAME = "strava"
DB_USER = "airflow_user"
DB_PASSWORD = "test_strava"
DB_HOST = "localhost"
DB_PORT = "5432"
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# === 1. Rafraîchir le token Strava ===
print("🔄 Rafraîchissement du token...")
refresh_response = requests.post(
    "https://www.strava.com/api/v3/oauth/token",
    data={
        "client_id": STRAVA_CLIENT_ID,
        "client_secret": STRAVA_CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": STRAVA_REFRESH_TOKEN,
    },
)
refresh_data = refresh_response.json()
access_token = refresh_data["access_token"]

# === 2. Récupérer toutes les activités avec pagination ===
print("📥 Récupération de toutes les activités...")

headers = {"Authorization": f"Bearer {access_token}"}
all_activities = []
page = 1

while True:
    response = requests.get(
        "https://www.strava.com/api/v3/athlete/activities",
        headers=headers,
        params={"per_page": 200, "page": page}
    )
    data = response.json()

    if not data:
        break

    all_activities.extend(data)
    print(f"📄 Page {page} récupérée ({len(data)} activités)")
    page += 1
    time.sleep(1)  # pour respecter la limite d'API Strava

df = pd.json_normalize(all_activities)
print(f"✅ Total récupéré : {len(df)} activités")

# === 3. Insérer dans PostgreSQL ===
from sqlalchemy import text
with engine.begin() as conn:
    conn.execute(text("DELETE FROM activities"))
df.to_sql("activities", engine, if_exists="append", index=False)
print("📤 Données insérées dans PostgreSQL ('activities')")
