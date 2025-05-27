# script to test connection to Fabric APIs
import os
from dotenv import load_dotenv
import requests

load_dotenv()

tenant_id = os.environ.get("TENANT_ID")

# client id/secret for permissions-test sp
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# resource for Items - list lakehouses or get lakehouse
resource = "https://analysis.windows.net/powerbi/api/.default"

# resource for Items - list reports
#resource = "https://analysis.windows.net/powerbi/api/.default"

# resource for sql server
#resource = "https://database.windows.net/.default"

# request data
data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": resource,
}

# token request url
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

# make token request
response = requests.post(token_url, data=data)
if response.status_code == 200:
    access_token = response.json().get("access_token")
    #print("Access Token:", access_token)
else:
    print("Failed to obtain access token:", response.status_code, response.text)
    exit(1)

# construct header for API requests
headers = {
    "Authorization": f'Bearer {access_token}',
    "Content-Type": "application/json"
}

### -------------------------------- ###
## TEST API CALLS FABRIC ITEMS ONLY   ##
### -------------------------------- ###

# api url for items - list lakehouses
#api_url = "https://api.fabric.microsoft.com/v1/workspaces/aea17f3c-0e48-4161-9159-0f90ac920819/lakehouses"

# api url for items - list reports
#api_url = "https://api.fabric.microsoft.com/v1/workspaces/aea17f3c-0e48-4161-9159-0f90ac920819/reports"

# api url for Items - get lakehouse
api_url = " https://api.fabric.microsoft.com/v1/workspaces/aea17f3c-0e48-4161-9159-0f90ac920819/lakehouses/984a8b42-0491-4cf2-abb6-4e8ae84150a2"

# use the access token, header to make API requests
print("Fetching Fabric items...")

fabric_response = requests.get(api_url, headers=headers)
if fabric_response.status_code == 200:
    fab_items = fabric_response.json()
    print("Fabric items:", fab_items)
else:
    print("Failed to fetch Fabric items:", fabric_response.status_code, fabric_response.text)
    exit(1)
