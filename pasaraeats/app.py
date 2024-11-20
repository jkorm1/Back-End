from flask import Flask, jsonify
from flask_cors import CORS
from pasaraeats.database import SessionLocal
from pasaraeats.models import Card

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

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
            'order_type': card.order_type
        }
        result.append(card_data)
    session.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
