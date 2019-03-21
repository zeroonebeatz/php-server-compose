#! /usr/bin/python3

import sys
from typing import List
from src.storages.services import Services


class BuilderIO:
    services = None

    def __init__(self, services: Services):
        self.services = services

    def read(self, added: List = None):
        if added:
            self.print_added()

        for line in sys.stdin:
            line = line.rstrip()

            if line == '':
                self.confirm()
                break

            services_list = line.split(',')

            for service in services_list:
                service = service.strip()
                if not self.services.is_valid(service):
                    continue

                self.services.add(service)

            self.print_added()

    def confirm(self):
        print('Start building? Type n or y:')
        for line in sys.stdin:
            line = line.rstrip()
            if line in ('', 'y'):
                break
            else:
                self.read(self.services.get())

    def print_available(self):
        print('Available services: ' + ', '.join(self.services.available))

    def print_added(self):
        self.print_available()
        print('Added: ' + ','.join(self.services.get()) + '\n')

    def get_services(self):
        return self.services.get()
