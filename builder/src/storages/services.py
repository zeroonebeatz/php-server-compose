from typing import List, Tuple

class Services:
    services = []
    availble = (
        'nginx',
        'php',
        'nodejs',
        'mysql',
        'psql',
        'redis',
    )

    def __init__(self, availble: Tuple):
        self.availble = availble

    def add(self, service: str):
        self.services.append(service)

    def get(self):
        return self.services

    def is_valid(self, line: str):
        if line not in self.availble:
            return False

        if line in self.services:
            return False

        return True
