import requests, os

from dotenv import load_dotenv, find_dotenv, dotenv_values


def findLatLng(address):
    load_dotenv(find_dotenv())

    params = {
        'key': dotenv_values(".env")['API_KEY'],
        'address': address
    }

    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

    response = requests.get(base_url, params=params).json()

    # Check if the request was processed successfully
    if response['status'] == 'OK':
        # If so, grab the lat and long from the response
        geometry = response['results'][0]['geometry']
        latitude = geometry['location']['lat']
        longitude = geometry['location']['lng']

<<<<<<< HEAD
    return latitude, longitude
=======
    return [latitude, longitude]
>>>>>>> 7d8c4451b1c81d12687003975d0e5e1c6ca70a4f
