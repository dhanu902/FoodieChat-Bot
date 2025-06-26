from flask import Blueprint, request, jsonify
from Services.Google_Places import get_nearby_places

search_bp = Blueprint('search', __name__, url_prefix='/search')

@search_bp.route('', methods=['POST'])
def search_places():
    data = request.get_json()
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    radius = data.get("radius", 3000)

    results = get_nearby_places(latitude, longitude, radius)
    return jsonify({"places": results})