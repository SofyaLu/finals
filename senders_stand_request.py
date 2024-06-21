import configuration
import data
import requests

def post_new_order(body):
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body,
        headers=data.headers
    )
    track_number = response.json().get('track')
    return response, track_number


def get_order(track_number):
    response = requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track_number),
        headers=data.headers
    )
    return response
