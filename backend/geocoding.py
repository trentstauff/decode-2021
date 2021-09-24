import requests, os

from dotenv import load_dotenv, find_dotenv, dotenv_values


def find_lat_lng(address):
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
        return latitude, longitude
    raise Exception(f"Response not OK! {response}")
