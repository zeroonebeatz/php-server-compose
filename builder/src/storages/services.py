from typing import Tuple


class Services:
    available = None
    services = []

    def __init__(self, available: Tuple):
        self.available = available

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
