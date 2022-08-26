import os
from flask import request
from autodesk_forge_sdk import OSSClient, OAuthTokenProvider
from autodesk_forge_sdk.dm import DataRetention
from autodesk_forge_sdk.md import urnify

client = OSSClient(OAuthTokenProvider(
    os.environ["FORGE_CLIENT_ID"], os.environ["FORGE_CLIENT_SECRET"]))


def ensure_bucket_exists(bucket_key):
    try:
        client.get_bucket_details(bucket_key=bucket_key)
    except Exception as e:
        client.create_bucket(
            bucket_key=bucket_key,
            data_retention_policy=DataRetention.TRANSIENT,
            region='US')


def upload_object(bucket_key, filename, buff):
    ensure_bucket_exists(bucket_key=bucket_key)
    uploaded_model = client.upload_object(bucket_key, filename, buff)
    return uploaded_model


def list_objects(bucket_key):
    ensure_bucket_exists(bucket_key=bucket_key)
    objects = client.get_objects(bucket_key=bucket_key)
    objs = objects["items"]
    data = []
    for i in range(len(objs)):
        urn_dict = {"name": objs[i]["objectKey"],
                    "urn": urnify(objs[i]["objectId"])}
        data.append(urn_dict)
    return data
