## create fabric lakehouse connection and foreign catalog
import os
from dotenv import load_dotenv

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import catalog

import requests

# load environment variables from .env file
load_dotenv()

## authenticate to adb python sdk using config_profile and create workspace scoped object
#config_profile = os.environ.get("DATABRICKS_CONFIG_PROFILE")
#w = WorkspaceClient(profile=config_profile)

# create access token for Fabric Lakehouse
# tenant id, client id/secret for permissions-test sp
tenant_id = os.environ.get("TENANT_ID")
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# resource for sql server
resource = "https://database.windows.net/.default offline_access"

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
token_response = requests.post(token_url, data=data)
if token_response.status_code == 200:
    access_token = token_response.json().get("access_token")
    #print("Access Token:", access_token)
else:
    print("Failed to obtain access token:", token_response.status_code, token_response.text)
    exit(1)

# construct header for API requests
headers = {
    "Authorization": f'Bearer {access_token}',
    "Content-Type": "application/json"
}

# create connnection object in adb workspace to Fabric lakehouse
conn_host = os.environ.get("HOST")
conn_clientid = os.environ.get("CLIENT_ID")
conn_clientsecret = os.environ.get("CLIENT_SECRET")
conn_oauthscope = os.environ.get("OAUTH_SCOPE")
conn_authendpoint = os.environ.get("AUTHORIZATION_ENDPOINT")
conn_oauthredirect = os.environ.get("OAUTH_REDRIECT_URI")

# construct request body - see https://docs.databricks.com/api/workspace/connections/create
request_body = {
    "host": conn_host,
    "port": "1433",
    "client_id": conn_clientid,
    "client_secret": conn_clientsecret,
    "oauth_scope": conn_oauthscope,
    "authorization_endpoint": conn_authendpoint,
    "oauth_redirect_uri": conn_oauthredirect,
    "pkce_verifier": "uSEEBJIX9TpIZmlWzPkrvin-HoXA_TWghZY04H_YKfzJG3kn3_MyXg",
}

adb_ws_url = os.environ.get("DATABRICKS_WORKSPACE_URL")

try:
    # make request to create connection
    response = requests.post(
        f"{adb_ws_url}/api/2.1/connections",
        headers=headers,
        json=request_body
    )

    if response.status_code == 200:
        conn_create = response.json()
        print("Connection created successfully:", conn_create)
    else:
        print("Failed to create connection:", response.status_code, response.text)

except Exception as e:
    print("Error occurred while creating connection:", str(e))


