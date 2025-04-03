import requests

client_id = "xxx"
client_secret = "xxx"
redirect_uri = "http://localhost"

# Récupérer le token une fois le code obtenu

code = "xxx"

response = requests.post("https://www.strava.com/api/v3/oauth/token", data={
    "client_id": client_id,
    "client_secret": client_secret,
    "code": code,
    "grant_type": "authorization_code"
})

tokens = response.json()
print("\n✅ Access Token :", tokens["access_token"])
print("🔁 Refresh Token :", tokens["refresh_token"])
print("📅 Expiration :", tokens["expires_at"])
