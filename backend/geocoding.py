import requests

API_KEY = 'AIzaSyCqmlVrzMvQZHDK1VqOeoap7mUOFq1dhVc'

# def findLatLng(address):
address = "Toronto, ON"

params = {
    'key': API_KEY,
    'address': address
}

base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

response = requests.get(base_url, params=params).json()

# Check if the request was processed successfully
if response['status'] == 'OK':
    # If so, grab the long lat from the response
    geometry = response['results'][0]['geometry']    
    latitude = geometry['location']['lat']
    longitude = geometry['location']['lng']

print(latitude, longitude)