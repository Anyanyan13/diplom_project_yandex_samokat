import configuration
import requests

def create_new_order(body):                                                                   # функция для отправки POST-запроса на создание нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                        json = body)

def search_order_by_track(track):                                                               # функция для отправки GET-запроса на получение информации о заказе по трек-номеру
   return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK,
                       params={"t": track})
