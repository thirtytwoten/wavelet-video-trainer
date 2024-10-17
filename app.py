import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app)

opacity = 0.5

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Function to simulate updating opacity
def update_opacity():
    global opacity
    
    # ***** TODO ******
    # update this to emit values calculated from EEG data
    # client is listening for 'update_opacity' event
    # and expects data in the form of {'opacity': opacity} where opacity is float between 0 and 1
    while True:
        # Simulate opacity changes: generate random float between 0 and 1
        opacity = random.uniform(0, 1)
        # Broadcast the new opacity to all connected clients
        socketio.emit('update_opacity', {'opacity': opacity})
        time.sleep(2)  # Update every 2 seconds

# WebSocket event for when a client connects
@socketio.on('connect')
def handle_connect():
    emit('update_opacity', {'opacity': opacity})

# Run the background thread to update opacity
thread = threading.Thread(target=update_opacity)
thread.daemon = True
thread.start()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
