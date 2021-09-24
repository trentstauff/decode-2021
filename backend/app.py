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
socket_io = SocketIO(app, cors_allowed_origins="*")
savedData = ""

@app.route("/", defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')


@app.route("/webhook", methods=['POST'])
def process_web_hooks():
    data = request.get_json()
    postal_code = data['business_details']['postal_code']
    location = findLatLng(postal_code)
    savedData = data
    socket_io.emit("data_response", data)
    return f"{location}"

@app.route('/large.csv')
def generate_large_csv():
    def generate():
        for row in range(100):
            yield f"{row}\n"
    return app.response_class(generate(), mimetype='text/csv')

@socket_io.on('connect')
def handle_message():
    print('[INFO] Web client connected: {}'.format(request.sid))
    send({
            "target": "DASHBOARD" | "LANDING_SITE",
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
            "target": "DASHBOARD" | "LANDING_SITE",
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
            "target": "DASHBOARD" | "LANDING_SITE",
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
            "target": "DASHBOARD" | "LANDING_SITE",
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

@socket_io.on('message')
def handle_message(data):
    print('received message: ' + data)

api.add_resource(ApiHandler, '/flask/hello')

# app.run(debug=True)
socket_io.run(app=app, host='127.0.0.1', port=5001, debug=True)
