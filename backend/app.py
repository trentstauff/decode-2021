import json

from flask_cors import CORS  # comment this on deployment
from flask_restful import Api
from flask_socketio import SocketIO

from api_handler import ApiHandler
from flask import Flask, send_from_directory, request, jsonify
from geocoding import findLatLng

app = Flask(__name__, static_url_path='', static_folder='frontend/public')
CORS(app)  # comment this on deployment, used to silence warning
api = Api(app)
api.add_resource(ApiHandler, '/flask/hello')

# SocketIO object
socket_io = SocketIO(app)

filtered_client_data = {}


@app.route("/", defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')


@app.route("/webhook", methods=['POST'])
def process_web_hooks():
    data = request.get_json()
    get_filtered_client_data(data)
    return jsonify(json.dumps(filtered_client_data))


@socket_io.on("connect", namespace="/test")
def connection_started():
    print('[INFO] Web client connected: {}'.format(request.sid))


@socket_io.on("disconnect", namespace="/test")
def connection_ended():
    print('[INFO] Web client disconnected: {}'.format(request.sid))


@socket_io.on("fetch_data")
def provide_data_to_caller():
    socket_io.emit("data_response", json.dumps({}))


def get_filtered_client_data(data):
    global filtered_client_data
    filtered_client_data = get_response_data(data)
    return


def get_response_data(data):
    postal_code = data['data']['business_details']['postal_code']
    location_coordinates = findLatLng(postal_code)
    response_data = {
        "target": "LANDING_SITE",
        "event_type": "capture.created",
        "data": {
            "capture": {
                "EventType": "",
                "transaction_type": data['data']['capture']['transaction_type'],
                "currency": data['data']['capture']['currency'],
                "merchant_currency": data['data']['capture']['merchant_currency'],
                "created_at": data['data']['capture']['created_at'],
                "updated_at": data['data']['capture']['updated_at'],
                "amount": data['data']['capture']['amount'],
                "merchant_amount": data['data']['capture']['merchant_amount'],
            },
            "merchant_details": {
                "longitude": location_coordinates[0],
                "latitude": location_coordinates[1],
            },
            "business_details": {
                "longitude": location_coordinates[0],
                "latitude": location_coordinates[1],
            }
        }
    }

    return response_data


app.run(debug=True)
socket_io.run(app=app, host='0.0.0.0', port=5001)
