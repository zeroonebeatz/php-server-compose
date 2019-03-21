from typing import Tuple
from src.storages.links import Links


class Services:
    available = None
    links = None
    services = []

    def __init__(self, available: Tuple, links: Links):
        self.available = available
        self.links = links

    def add(self, service: str):
        self.services.append(service)

    def get(self):
        return self.services

    def is_valid(self, line: str):
        if line not in self.available:
            return False

        if line in self.services:
            return False

        return True
