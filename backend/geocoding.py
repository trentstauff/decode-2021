import requests

from dotenv import load_dotenv, find_dotenv, dotenv_values


store = {}


def findLatLng(address: str):

    # If we have already made this call, then let's just use what was stored
    stored_result = store.get(address, None)
    if stored_result:
        return stored_result[1], stored_result[2]

    load_dotenv(find_dotenv())

    params = {"key": dotenv_values(".env")["API_KEY"], "address": address}

    base_url = "https://maps.googleapis.com/maps/api/geocode/json?"

    response = requests.get(base_url, params=params).json()

    # Check if the request was processed successfully
    if response["status"] == "OK":
        # If so, grab the lat and long from the response
        geometry = response["results"][0]["geometry"]
        latitude = geometry["location"]["lat"]
        longitude = geometry["location"]["lng"]

        # Store the result in our local in-memory storage (dictionary)
        store[address] = (geometry, latitude, longitude)
        return latitude, longitude
    raise Exception(f"Response not OK! {response}")
