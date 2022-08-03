import os
from autodesk_forge_sdk import OSSClient, OAuthTokenProvider

client = OSSClient(OAuthTokenProvider(
    os.environ["FORGE_CLIENT_ID"], os.environ["FORGE_CLIENT_SECRET"]))


def create_bucket(bucket_name, data_retention_policy, region):
    bucket = client.create_bucket(
        bucket_key=bucket_name,
        data_retention_policy=data_retention_policy,
        region=region)
    return bucket


def get_bucket(bucket_key):
    bucket = client.get_bucket_details(bucket_key=bucket_key)
    return bucket


def list_objects(bucket_key):
    objects = client.get_objects(bucket_key=bucket_key)
    return objects
