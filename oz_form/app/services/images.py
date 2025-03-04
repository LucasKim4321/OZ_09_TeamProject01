from flask import Blueprint, jsonify, request
from app.models import db 
from app.models import Image 

images = Blueprint('images', __name__)

@images.route('/image/main', methods=['GET'])
def get_main_image():
    return jsonify({"image": "https://example.com/image.jpg"}), 200

@images.route('/image', methods=['POST'])
def create_image():
    data = request.json
    
    if 'type' not in data or data['type'] not in ['main', 'sub']:
        return jsonify({"error": "Invalid type. Must be 'main' or 'sub'"}), 400

    new_image = Image(
        url=data['url'],
        type=data['type']
    )
    db.session.add(new_image)
    db.session.commit()

    return jsonify({"message": f"ID: {new_image.id} Image Success Create"}), 201
