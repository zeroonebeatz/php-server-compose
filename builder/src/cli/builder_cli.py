from src.services.builder_facade import BuilderFacade
from src.cli.builder_io import BuilderIO


class BuilderCli:
    io = None

    def __init__(self, io: BuilderIO):
        self.io = io

    def run(self):
        self.start()
        self.build()

    def start(self):
        self.io.print_available()
        print('Add service: \n')
        self.io.read()

    def build(self):
        print('Added: ' + ','.join(self.io.services.get()))
        print('Building...')
        BuilderFacade.build(self.io.services)
        print('Done!')
