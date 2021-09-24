import flask
import json
from flask import Flask, send_from_directory, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS  # comment this on deployment
from flask_socketio import SocketIO, send
from api_handler import ApiHandler
from geocoding import findLatLng

app = Flask(__name__, static_url_path='', static_folder='frontend/public')
CORS(app)  # comment this on deployment, used to silence warning
api = Api(app)

# SocketIO object
socket_io = SocketIO(app, cors_allowed_origins="*")
filtered_client_data = {}


@app.route("/", defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')


@app.route("/webhook", methods=['POST'])
def process_web_hooks():
    data = request.get_json()
    get_filtered_client_data(data)
    socket_io.emit("data_response", json.dumps(filtered_client_data))
    return "Sent data to front-end"


@socket_io.on('connect')
def handle_message():
    print('[INFO] Web client connected: {}'.format(request.sid))
    send({
        "target": "DASHBOARD",
        "event_type": "capture.created",
        "data": {
            "capture": {
                "EventType": "",
                "transaction_type": "CAPTURE",
                "currency": "CAD",
                "merchant_currency": "CAD",
                "created_at": 1632422976709,
                "updated_at": 1632422977059,
                "amount": 1384,
                "merchant_amount": 1384
            },
            "merchant_details": {
                "longitude": 100,
                "latitude": 100
            },
            "business_details": {
                "longitude": 100,
                "latitude": 100,
            }
        }
    })
    send({
        "target": "DASHBOARD",
        "event_type": "capture.created",
        "data": {
            "capture": {
                "EventType": "",
                "transaction_type": "CAPTURE",
                "currency": "CAD",
                "merchant_currency": "CAD",
                "created_at": 1632422976709,
                "updated_at": 1632422977059,
                "amount": 1384,
                "merchant_amount": 1384
            },
            "merchant_details": {
                "longitude": 200,
                "latitude": 200
            },
            "business_details": {
                "longitude": 300,
                "latitude": 300,
            }
        }
    })
    send({
        "target": "DASHBOARD",
        "event_type": "capture.created",
        "data": {
            "capture": {
                "EventType": "",
                "transaction_type": "CAPTURE",
                "currency": "CAD",
                "merchant_currency": "CAD",
                "created_at": 1632422976709,
                "updated_at": 1632422977059,
                "amount": 1384,
                "merchant_amount": 1384
            },
            "merchant_details": {
                "longitude": 400,
                "latitude": 400
            },
            "business_details": {
                "longitude": 100,
                "latitude": 100,
            }
        }
    })
    send({
        "target": "DASHBOARD",
        "event_type": "capture.created",
        "data": {
            "capture": {
                "EventType": "",
                "transaction_type": "CAPTURE",
                "currency": "CAD",
                "merchant_currency": "CAD",
                "created_at": 1632422976709,
                "updated_at": 1632422977059,
                "amount": 1384,
                "merchant_amount": 1384
            },
            "merchant_details": {
                "longitude": 700,
                "latitude": 100
            },
            "business_details": {
                "longitude": 600,
                "latitude": 600,
            }
        }
    })


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


api.add_resource(ApiHandler, '/flask/hello')

socket_io.run(app=app, host='127.0.0.1', port=5001, debug=True)
