import os
from flask import make_response, jsonify, request, render_template
from app.api.v1 import blueprint_v1
from app.api.v1.services.oss import list_objects, upload_object
from app.api.v1.services.md import get_manifest, translate_object
from autodesk_forge_sdk.md import urnify
from werkzeug.utils import secure_filename


@blueprint_v1.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@blueprint_v1.route("/models", methods=['GET'])
def get_objects():
    try:
        objects = list_objects(bucket_key=os.environ.get("FORGE_BUCKET"))
        return make_response(jsonify(objects))
    except Exception as e:
        return make_response(jsonify({
            "error": str(e)
        }), 400)


@blueprint_v1.route("/models", methods=['POST'])
def upload():
    try:
        if 'model-file' in request.files:
            filedata = request.files['model-file']
            if filedata.filename != '':
                if filedata:
                    f = filedata.read()
                    buff = bytearray(f)
                    filename = secure_filename(filedata.filename)
                    uploaded_model = upload_object(
                        os.environ.get("FORGE_BUCKET"), filename, buff)
                    translate_object(urnify(uploaded_model["objectId"]), [
                        {"type": "svf", "views": ["2d", "3d"]}])
                    return make_response(jsonify({
                        "name": uploaded_model["objectKey"],
                        "urn": urnify(uploaded_model["objectId"])
                    }), 200)
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
