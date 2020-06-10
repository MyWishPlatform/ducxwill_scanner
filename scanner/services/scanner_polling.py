import time

from scanner.services.scanner import Scanner
from blockchain_common.wrapper_network import WrapperNetwork
from scanner.services.last_block_persister import LastBlockPersister


class ScannerPolling(Scanner):

    def __init__(self, network: WrapperNetwork, last_block_persister: LastBlockPersister, polling_interval: int,
                 commitment_chain_length: int, reach_interval: int = 0):

        super().__init__(network, last_block_persister)
        self.polling_interval = polling_interval
        self.commitment_chain_length = commitment_chain_length
        self.reach_interval = reach_interval

    def poller(self):
        self.next_block_number = self.last_block_persister.get_last_block()
        print('hello from')
        while True:
            self.polling()


    def polling(self):
        self.last_block_number = self.network.get_last_block()

        if self.last_block_number - self.next_block_number > self.commitment_chain_length:
            self.load_next_block()
            time.sleep(self.reach_interval)
            return

        print('no block')
        time.sleep(self.polling_interval)


    def load_next_block(self):
        block = self.network.get_block(self.next_block_number)

        self.last_block_persister.save_last_block(self.next_block_number)
        self.next_block_number += 1

        self.process_block(block)

    def open(self):
        pass

    def close(self):
        pass
