import requests

# Remplace ces valeurs avec les tiennes :
client_id = "153745"
client_secret = "7f4fd98d47e32b6432759f6d1b80022fa649083f"
redirect_uri = "http://localhost"

# Étape 1 : Afficher l'URL à visiter pour autoriser
#url = (

#print("👉 Ouvre cette URL dans ton navigateur :\n")
#print(url)

# Étape 2 : Récupérer le token une fois le code obtenu

code = "e21eb1a8f82ea8eb8b0ff00dfbf84fc83132717f"

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
