from typing import Dict
import io
import yaml


class Builder:
    conf = {}  # compose configuration
    confd = ''  # services config dir
    out = ''  # output file path

    def __init__(self, conf: Dict, confd: str, out: str):
        self.conf = conf
        self.confd = confd
        self.out = out

    def push(self, fname: str, service: str = None):
        if service is None:
            service = fname

        conf = Builder.read_yaml(self.confd + fname + '.yml')
        self.conf['services'][service] = conf

    def write_yaml(self):
        with io.open(self.out, 'w', encoding='utf8') as outfile:
            yaml.dump(self.conf, outfile, default_flow_style=False, allow_unicode=True)

    def make(self):
        self.write_yaml()

    @staticmethod
    def read_yaml(path: str):
        with open(path, 'r') as stream:
            data = yaml.load(stream)
        return data
