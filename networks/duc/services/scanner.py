from collections import defaultdict

from eventscanner.queue.subscribers import pub

from scanner.events.block_event import BlockEvent
from scanner.services.scanner_polling import ScannerPolling
from .block import DucBlock


class DucScanner(ScannerPolling):

    def __init__(self, network, last_block_persister, polling_interval, commitment_chain_length):
        super().__init__(network, last_block_persister, polling_interval, commitment_chain_length)

    def process_block(self, block: DucBlock):
        print('{}: new block received {} ({})'.format(self.network.type, block.number, block.hash), flush=True)
        if not block.transactions:
            print('{}: no transactions in {} ({})'.format(self.network.type, block.number, block.hash), flush=True)
            return

        address_transactions = defaultdict(list)
        for transaction in block.transactions:
            for output in transaction.outputs:
                if output.address:
                    address_transactions[output.address.lower()].append(transaction)

        print('{}: transactions'.format(self.network.type), address_transactions, flush=True)
        block_event = BlockEvent(self.network, block, address_transactions)

        # pub.sendMessage(self.network.type, block_event=block_event)