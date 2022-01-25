from db.dbconnector import DBConnector
from config import Config


class DBDevices:
    def __init__(self):
        self.connection = DBConnector(**Config.db_devices)
        self.plcs = []

    def get_devices(self):
        """get devices from database"""
        query = "SELECT name, ip, robot_quantity FROM robots_config WHERE active = 1"
        self.plcs = self.connection.fetchall_query(query)
        return self.plcs
