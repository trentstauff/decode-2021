from flask import Flask, send_from_directory, request
import flask
import json
from flask import Flask, send_from_directory, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS  # comment this on deployment
from flask_socketio import SocketIO, send, emit
from api_handler import ApiHandler
from data_redaction import convert_webhook_to_websocket_event
from geocoding import find_lat_lng

app = Flask(__name__, static_url_path='', static_folder='frontend/public')
CORS(app)  # comment this on deployment, used to silence warning
api = Api(app)

# SocketIO object
socket_io = SocketIO(app, cors_allowed_origins="*")
filtered_client_data = {}


@app.route("/", defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')

"""
    (1) Add all events to here when we receive them
    (2) For each event in here, send over the socket when requested 
"""
ws_events = []

@app.route("/webhook", methods=['POST'])
def process_web_hooks():
    data = json.loads(request.data)

    # TODO: Handle failure events better
    try:
        ws_event = convert_webhook_to_websocket_event(data, target='DASHBOARD')
        socket_io.emit('message', ws_event)
    except Exception as err:
        print(err)
    return jsonify({})


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


# @socket_io.on('message')
# def send_data_to_client():
#     while ws_events != []:
#         ws_event = ws_events.pop()
#         socket_io.emit(ws_event)

api.add_resource(ApiHandler, '/flask/hello')

socket_io.run(app=app, host='127.0.0.1', port=5001, debug=True)
