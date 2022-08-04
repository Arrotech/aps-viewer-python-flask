import os
import base64
from flask import make_response, jsonify, request, render_template
from app.api.v1 import blueprint_v1
from app.api.v1.services.oss import list_objects, client
from app.api.v1.services.md import get_manifest, translate_object
from autodesk_forge_sdk.md import urnify
from werkzeug.utils import secure_filename


@blueprint_v1.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@blueprint_v1.route("/models", methods=['GET', 'POST'])
async def bucket_objects():
    try:
        if request.method == 'GET':
            objects = list_objects(bucket_key=os.environ.get("FORGE_BUCKET"))
            objs = objects["items"]
            data = []
            for i in range(len(objs)):
                urn_dict = {"name": objs[i]["objectKey"],
                            "urn": urnify(objs[i]["objectId"])}
                data.append(urn_dict)
            print(data)
            return make_response(jsonify(data), 200)
        elif request.method == 'POST':
            if 'model-file' in request.files:
                filedata = request.files['model-file']
                if filedata.filename != '':
                    if filedata:
                        f = filedata.read()
                        buff = bytearray(f)
                        filename = secure_filename(filedata.filename)
                        uploaded_model = client.upload_object(
                            os.environ.get("FORGE_BUCKET"),
                            filename,
                            buff)
                        translate_object(urnify(uploaded_model["objectId"]), [
                            {"type": "svf", "views": ["2d", "3d"]}])
                        return make_response(jsonify({
                            "name": uploaded_model["objectKey"],
                            "urn": urnify(uploaded_model["objectId"])
                        }), 200)
                    return make_response(jsonify({
                        "error": "No file selected"
                    }), 400)
                return make_response(jsonify({
                    "error": "No file selected"
                }))
            return make_response(jsonify({
                "error": "No file uploaded"
            }))
    except Exception as e:
        return make_response(jsonify({
            "error": str(e)
        }), 400)


@blueprint_v1.route("/models/<string:urn>/status", methods=['GET'])
def get_status(urn):
    try:
        print(urn)
        manifest = get_manifest(urn)
        if manifest:
            messages = []
            if manifest["derivatives"]:
                for derivative in manifest["derivatives"]:
                    messages.extend(
                        derivative["messages"] if "messages" in derivative else [])
                    # if derivative["children"]:
                    #     for child in derivative["children"]:
                    #         messages.extend(child["messages"] if "messages" in child else [])
            return make_response(jsonify({
                "status": manifest["status"],
                "progress": manifest["progress"],
                "messages": messages
            }), 200)
        else:
            return make_response(jsonify({
                "status": "n/a"
            }), 404)
    except Exception as e:
        return make_response(jsonify({
            "error": str(e)
        }), 400)
