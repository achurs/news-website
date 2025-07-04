#import necessary libraries
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import threading
import time
import db
import rss


# Initialize Flask app and SocketIO
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Configure the app
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Flask-SocketIO server!"})


@socketio.on('connect')
def connected():
    handle_connect()

# disconnection socketio events
@socketio.on('disconnect')
def disconnected():
    handle_disconnect()

# Handle custom message events
@socketio.on('message')
def handle_message(data):
    print('Received message:', data)

# Function to send news items to connected clients
def send_news(msg):
        print('Sent:', msg['title'])
        info = {
            'title': msg['title'],
            'link': msg['link'],
            'published': msg['published']
        }
        socketio.emit('message', info) 
        db.insert_news_item(msg['title'], msg['link'], msg['published'])

@socketio.on('getAllNews')
def get_all_news():
    """Handle news requests from clients."""
    print('News request received')
    news_req = db.get_all_news()
    socketio.emit('allNews', {'news': news_req})
    print('Sent all news to client')

# Handle client connection and disconnection
def handle_connect():
    print('Client connected')

def handle_disconnect():
    print('Client disconnected')

# Function to generate news items periodically
def news_generator():
    while True:
        time.sleep(10)
        item = rss.news()
        send_news(item)

if __name__ == '__main__':
    threading.Thread(target=news_generator, daemon=True).start()
    print('Starting Flask-SocketIO server...')
    socketio.run(app, host='0.0.0.0', port=5000)