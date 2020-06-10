import threading
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from networks.ducx.ducx_starter import DucxMaker

networks = [DucxMaker]


class ScanEntrypoint(threading.Thread):

    def __init__(self, network_maker):
        super().__init__()
        self.network = network_maker()

    def run(self):
        self.network.scanner.poller()


if __name__ == '__main__':
    for net in networks:
        scan = ScanEntrypoint(net)
        scan.start()
