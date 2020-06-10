import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

print(BASE_DIR)


from networks.ducx.services.ducx_network import DucxNetwork
from scanner.services.last_block_persister import LastBlockPersister
from networks.ducx.services.ducx_scanner import DucxScanner

from settings.settings_local import *


class DucxMaker:
    def __init__(self):
        network = DucxNetwork('DUCATUSX_TESTNET')
        last_block_persister = LastBlockPersister(network)
        polling_interval = 10
        commitment_chain_length = 5
        self.scanner = DucxScanner(network, last_block_persister, polling_interval, commitment_chain_length)


if __name__ == '__main__':
    scanner = DucxMaker()
    scanner.scanner.poller()
