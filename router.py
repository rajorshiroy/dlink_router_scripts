import requests


class Router:
    def __init__(self, username='Admin', password='', root='http://192.168.0.1/'):
        self.username = username
        self.password = password
        self.root = root

    def login(self) -> bool:
        pass

    def logout(self) -> bool:
        pass

    def whitelist_mac_address(self):
        pass

    def blacklist_mac_address(self):
        pass

    def change_password(self, new_password):
        pass

    def get_active_clients(self):
        pass
