import configuration
import data
import requests

def post_new_order(body):
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body,
        headers=data.headers
    )

    assert response.status_code == 201

    track_number = response.json().get('track')
    assert track_number is not None
    return track_number



def get_order(track_number):
    response = requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track_number),
        headers=data.headers
    )
    return response


def test_create_and_get_order():
        # Шаг 1: Выполнить запрос на создание заказа
        track_number = post_new_order(data.order_body)

        # Шаг 2: Выполнить запрос на получение заказа по треку заказа
        response = get_order(track_number)

        # Шаг 3: Проверить, что код ответа равен 200
        assert response.status_code == 200







#def post_new_order(body):
    #return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         #json=body,
                         #headers=data.headers)
#response = post_new_order(data.order_body)
#assert response.status_code == 201
#track_number = response.json().get('track')
#print(track_number)
#rint(response.url)
#print(response.status_code)



#def get_order(track_number):
    #response = requests.get(
        #configuration.URL_SERVICE + configuration.GET_ORDER_PATH + track_number,
        #headers=data.headers)
    #print(response.status_code)
    #print(response.url)
    #return response


#def test_create_and_get_order():
    #track_number = post_new_order(data.order_body)
    #response = get_order(track_number)
    #assert response.status_code == 200