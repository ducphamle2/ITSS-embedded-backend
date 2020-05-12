from flask import (Flask, request, session, g, redirect,
                   url_for, abort, render_template, flash, Response)
from flask_cors import CORS
from flask_socketio import SocketIO, join_room, emit, send
from utils.utils import response

app = Flask(__name__)
socketio = SocketIO(app)

# USE CORS SO THE BROWSER CAN CALL TO THE SERVER
CORS(app)


@app.route("/moveActions/left", methods=["POST"])
def moveLeft():
    # USE JSON FOR SIMPLICITY
    request_json = request.get_json()
    print("request json: ", request_json)
    # socketio.emit("move", request_json["message"])  # emit to the robot socket
    return response('success', "moved left", 200)


@app.route("/moveActions/right", methods=["POST"])
def moveRight():
    request_json = request.get_json()
    print("request json: ", request_json)
    return response('success', "moved right", 200)


@socketio.on('message')
def handle_message(msg):
    print('received message: ' + msg)
    #send(msg, broadcast=True)


# NOTE: THIS MAIN FILENAME MUST MATCH THE NAME IN THE PROCFILE
# Eg: this file is named main.py, then in procfile => main:app

if __name__ == '__main__':
    socketio.run(app, debug=True)
    # app.run(debug=True)
    #app.run(host='0.0.0.0', port='8088')
