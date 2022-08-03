import os
from autodesk_forge_sdk import ModelDerivativeClient, OAuthTokenProvider

client = ModelDerivativeClient(OAuthTokenProvider(
    os.environ["FORGE_CLIENT_ID"], os.environ["FORGE_CLIENT_SECRET"]))


def translate_object(urn, output_formats):
    job = client.submit_job(urn, output_formats)
    return job


def get_manifest(urn):
    manifest = client.get_manifest(urn)
    return manifest
