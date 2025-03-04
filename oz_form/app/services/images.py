from flask import Blueprint, jsonify

images = Blueprint('images', __name__)

@images.route('/image/main', methods=['GET'])
def get_main_image():
    return jsonify({"image": "https://example.com/image.jpg"}), 200
