from flask import Flask, send_from_directory, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api_handler import ApiHandler

app = Flask(__name__, static_url_path='', static_folder='frontend/public')
CORS(app) #comment this on deployment, used to slience warning
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')


@app.route("/webhook", methods=["POST"])
def webhook():
    res = request.get_json(force=True)

    print(res)
    return

# url
api.add_resource(ApiHandler, '/flask/hello')

app.run()
