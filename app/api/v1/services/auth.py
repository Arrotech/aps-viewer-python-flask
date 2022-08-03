import os
from autodesk_forge_sdk import AuthenticationClient, Scope


client = AuthenticationClient()
internal_auth_client = client.authenticate(
    os.environ["FORGE_CLIENT_ID"], os.environ["FORGE_CLIENT_SECRET"], [Scope.BUCKET_READ, Scope.BUCKET_CREATE, Scope.DATA_READ, Scope.DATA_WRITE, Scope.DATA_CREATE])
public_auth_client = client.authenticate(
    os.environ["FORGE_CLIENT_ID"], os.environ["FORGE_CLIENT_SECRET"], [Scope.VIEWABLES_READ])
