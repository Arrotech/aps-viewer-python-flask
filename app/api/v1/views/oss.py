import os
from flask import make_response, jsonify, request
from app.api.v1 import blueprint_v1
from app.api.v1.services.oss import client, create_bucket, get_bucket

from autodesk_forge_sdk.dm import DataRetention


@blueprint_v1.route("/buckets", methods=['GET', 'POST'])
def buckets():
    try:
        if request.method == 'POST':
            bucket = create_bucket(
                bucket_name=os.environ.get("FORGE_BUCKET"),
                data_retention_policy=DataRetention.TRANSIENT,
                region=os.environ.get("FORGE_REGION"))
            return make_response(jsonify({
                "bucket": bucket
            }), 200)
        return make_response(jsonify({
            "buckets": client.get_all_buckets()
        }))
    except Exception as e:
        return make_response(jsonify({
            "error": str(e)
        }), 400)


@blueprint_v1.route("/bucket", methods=['GET', 'DELETE'])
def bucket_details():
    try:
        if request.method == 'GET':
            bucket = get_bucket(bucket_key=os.environ.get("FORGE_BUCKET"))
            return make_response(jsonify({
                "bucket": bucket
            }), 200)
        elif request.method == 'DELETE':
            bucket = client.delete_bucket(
                bucket_key=os.environ.get("FORGE_BUCKET"))
            return make_response(jsonify({
            }), 204)
    except Exception as e:
        return make_response(jsonify({
            "error": str(e)
        }), 400)
