from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from database import SessionLocal  # Remove the module prefix
from models import Card           # Remove the module prefix

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/cards', methods=['GET'])
def get_cards():
    session = SessionLocal()
    cards = session.query(Card).all()
    result = []
    for card in cards:
        card_data = {
            'user_id': card.user_id,
            'containers': card.containers,
            'location': card.location,
            'order_type': card.order_type,
            'status': 'pending'
        }
        result.append(card_data)
    session.close()
    return jsonify(result)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('order_updated')
def handle_order_update(data):
    socketio.emit('order_updated', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5001, debug=True)