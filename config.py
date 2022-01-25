import pathlib


class Config:
    def __init__(self):
        pass

    PATH = pathlib.Path(__file__).parent.resolve()

    DB_NAME = 'OPC'
    DB_USER = 'postgres'
    DB_PASSWORD = '6450300'
    DB_HOST = '192.168.201.40'
    DB_PORT = '5432'


alarm_robot_token = "1691655389:AAEov2b8_8tFnMj3Xz_XYArIAE87t4-nMwM"
channel_moscow_alarm = "-590139888"

login = 'kolesnik'  # логин для системы видеонаблюдения
password = 'DCNwg42#rwn'  # пароль для системы видеонаблюдения
header = {
    'Content-type': 'application/x-msgpack'}  # не трогать - способ кодирования апроса/ответа сервера видеонаблюдения
maxduration = 120  # максимальная длина видео

# словарь для сопоставления номера каждой камеры с URL для доступа к ней и её
# уникальным id на сервере видеонаблюдения. Чтобы добавить новую камеру в этот список, узнайте ее id,
# отправив GET запрос на адрес "URL камеры/cameras"

cameras = {
    0: {"cameraId": 6, "cameraURL": "http://192.168.201.17:9786/rpc", "cameraTimeShift": 0},
    1: {"cameraId": 12, "cameraURL": "http://192.168.201.17:9786/rpc", "cameraTimeShift": 0},
    2: {"cameraId": 29, "cameraURL": "http://192.168.30.10:9786/rpc", "cameraTimeShift": -20},
    3: {"cameraId": 0, "cameraURL": "http://192.168.30.11:9786/rpc", "cameraTimeShift": -8},
    4: {"cameraId": 37, "cameraURL": "http://192.168.20.10:9786/rpc", "cameraTimeShift": -21},
    5: {"cameraId": 38, "cameraURL": "http://192.168.20.10:9786/rpc", "cameraTimeShift": -19},
    6: {"cameraId": 7, "cameraURL": "http://192.168.80.50:9786/rpc", "cameraTimeShift": 0},
    7: {"cameraId": 6, "cameraURL": "http://192.168.10.10:9786/rpc", "cameraTimeShift": -18}
}
