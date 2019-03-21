#! /usr/bin/python3

import sys
from typing import List
from src.services.builder_facade import BuilderFacade


class BuilderWorker:
    availble = (
        'nginx',
        'php',
        'nodejs',
        'mysql',
        'psql',
        'redis',
    )

    services = []

    def start(self):
        self.print_available()
        print('Add service: \n')
        self.read()

    def build(self):
        print('Added: ' + ','.join(self.services))
        print('Building...')
        BuilderFacade.make(self.services)
        print('Done!')

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
                if not self.is_valid(service):
                    continue

                self.services.append(service)

            self.print_added()

    def confirm(self):
        print('Start building? Type n or y:')
        for line in sys.stdin:
            line = line.rstrip()
            if line in ('', 'y'):
                break
            else:
                self.read(self.services)

    def print_available(self):
        print('Available services: ' + ', '.join(self.availble))

    def print_added(self):
        self.print_available()
        print('Added: ' + ','.join(self.services) + '\n')

    def is_valid(self, line: str):
        if line not in self.availble:
            return False

        if line in self.services:
            return False

        return True

    def get_services(self):
        return self.services

    @staticmethod
    def run():
        cli = BuilderCli()
        cli.start()
        cli.build()
