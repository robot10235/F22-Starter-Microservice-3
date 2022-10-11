from flask import Flask, Response, request
from datetime import datetime
import json
from mail_resource import MailResource
from address_resource import AddressResource
from phone_resource import PhoneResource
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(app)


@app.route("/api/students/<uni>/addresses", methods=["GET", "POST", "DELETE"])
def get_address_by_uni(uni):
    if request.method == "GET":
        result = AddressResource.get_by_uni(uni)
        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    elif request.method == "POST":
        data = request.get_json()
        result = AddressResource.add_by_uni(uni, data)
        if result > 0:
            rsp = Response("ADD OK", status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    else:
        result = AddressResource.delete_by_uni(uni)
        if result > 0:
            rsp = Response("DELETE OK", status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/students/<uni>/emails", methods=["GET", "POST", "DELETE"])
def get_mail_by_uni(uni):
    if request.method == "GET":
        result = MailResource.get_by_uni(uni)
        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    elif request.method == "POST":
        data = request.get_json()
        result = MailResource.add_by_uni(uni, data)
        if result > 0:
            rsp = Response("ADD OK", status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    else:
        result = MailResource.delete_by_uni(uni)
        if result > 0:
            rsp = Response("DELETE OK", status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/students/<uni>/phones", methods=["GET", "POST", "DELETE"])
def get_phones_by_uni(uni):
    if request.method == "GET":
        result = PhoneResource.get_by_uni(uni)
        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    elif request.method == "POST":
        data = request.get_json()
        result = PhoneResource.add_by_uni(uni, data)
        if result > 0:
            rsp = Response("ADD OK", status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    else:
        result = PhoneResource.delete_by_uni(uni)
        if result > 0:
            rsp = Response("DELETE OK", status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)

