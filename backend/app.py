import flask
from flask import Flask, send_from_directory, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS  # comment this on deployment
from flask_socketio import SocketIO, send
from api_handler import ApiHandler
from geocoding import findLatLng

app = Flask(__name__, static_url_path='', static_folder='frontend/public')
CORS(app)  # comment this on deployment, used to silence warning
api = Api(app)

# SocketIO object
socket_io = SocketIO(app)


@app.route("/", defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')


@app.route("/webhook", methods=['POST'])
def process_web_hooks():
    data = request.get_json()
    postal_code = data['business_details']['postal_code']
    location = findLatLng(postal_code)
    socket_io.emit("data_response", data)
    return f"{location}"


api.add_resource(ApiHandler, '/flask/hello')

app.run(debug=True)
socket_io.run(app)
