'''
Nana-Core: **Listener** Module

+  Listen on port 5051 for events from Mirai-api-HTTP
+  Export **Listener** Class
    - Classes derived from **Listener** would process acquired events
'''

from Utils.Dispatcher import Dispatcher
from Utils.Interface import Action, Destination, MessageElement
from flask import Flask, request
from flask_cors import CORS

MainListener = Flask(__name__)
cors = CORS(MainListener, resources={r"/api/*": {"origins": "*"}})

@MainListener.route("/recv", methods=['GET', 'POST'])
def recv():
    action = Action([MessageElement.fromPlainText(str(request.json))], [Destination.fromQQGroup(683950981)])
    Dispatcher.send(action)
    return "received"
