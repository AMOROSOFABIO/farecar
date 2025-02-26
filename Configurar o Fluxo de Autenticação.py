import requests
import os

# Carregar variáveis de ambiente
from dotenv import load_dotenv

load_dotenv()

ML_AUTH_URL = "https://api.mercadolibre.com/oauth/token"
APP_ID = os.getenv("ML_CLIENT_ID")
SECRET_KEY = os.getenv("ML_CLIENT_SECRET")
REDIRECT_URI = os.getenv("ML_REDIRECT_URI")
AUTHORIZATION_CODE = "COLOQUE_O_CODE_AQUI"

# Troca o code pelo access token
response = requests.post(
    ML_AUTH_URL,
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    data={
        "grant_type": "authorization_code",
        "client_id": APP_ID,
        "client_secret": SECRET_KEY,
        "code": AUTHORIZATION_CODE,                                                 "redirect_uri": REDIRECT_URI,
        },
)

if response.status_code == 200:
    data = response.json()
    print("Access Token:", data["access_token"])
    print("Refresh Token:", data["refresh_token"])
else:
    print("Erro ao trocar o code:", response.json())