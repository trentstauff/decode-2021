from flask import Flask, send_from_directory, request
import flask
import json
from flask import Flask, send_from_directory, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS  # comment this on deployment
from flask_socketio import SocketIO, send, emit
from api_handler import ApiHandler
from data_redaction import convert_webhook_to_websocket_event
# from geocoding import findLatLng

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


api.add_resource(ApiHandler, '/flask/hello')

socket_io.run(app=app, host='127.0.0.1', port=5001, debug=True)
