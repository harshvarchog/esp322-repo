from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return "ESP32 WebSocket Server Running!"

@socketio.on('sensor_data')
def handle_sensor_data(data):
    print("Received sensor data:", data)
    emit('update_web', data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=10000)
