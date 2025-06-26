import os
import requests

'''GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def get_nearby_places(latitude, longitude, radius):
    url = (
        f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
        f"location={latitude},{longitude}&radius={radius}"
        f"&type=restaurant&key={GOOGLE_API_KEY}"
    )

    response = requests.get(url)
    results = response.json().get("results", [])

    places = []
    for place in results:
        places.append({
            "name": place.get("name"),
            "address": place.get("vicinity"),
            "rating": place.get("rating"),
            "location": place.get("geometry", {}).get("location"),
        })

    return places
'''

def get_nearby_places(latitude, longitude, radius):
    # 🧪 Temporary mock data for testing UI/backend
    return [
        {
            "name": "Pizza Hub",
            "address": "123 Galle Road, Colombo",
            "rating": 4.5,
            "location": {"lat": float(latitude), "lng": float(longitude)}
        },
        {
            "name": "Burger Planet",
            "address": "456 Marine Drive, Colombo",
            "rating": 4.2,
            "location": {"lat": float(latitude) + 0.001, "lng": float(longitude) + 0.001}
        },
        {
            "name": "Vegan Vibes",
            "address": "789 Flower Rd, Colombo",
            "rating": 4.8,
            "location": {"lat": float(latitude) - 0.001, "lng": float(longitude) - 0.001}
        }
    ]