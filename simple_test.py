import json
from SuitecrmPythonClient import SuitecrmApiClient

secrets = None
with open("test_secret.json", "r") as fh:
    secrets = json.load(fh)

client = SuitecrmApiClient(baseURL=secrets["base_url"])
login_session = client.getLoginSessionBasedOnClientIdAndSecret(clientId=secrets["client_id"], clientSecret=secrets["client_secret"])

print(client.getModules(login_session))