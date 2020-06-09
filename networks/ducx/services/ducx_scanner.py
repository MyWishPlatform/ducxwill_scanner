import collections

from scanner.services.scanner_polling import ScannerPolling
from networks.ducx.services.ducx_network import DucxNetwork
from blockchain_common.wrapper_block import WrapperBlock
from scanner.events.block_event import BlockEvent
from scanner.services.last_block_persister import LastBlockPersister

from eventscanner.monitors.payments.ducx_payment_monitor import DucxPaymentMonitor


class DucxScanner(ScannerPolling):
    counter = 0

    def __init__(self, network: DucxNetwork, last_block_persister: LastBlockPersister, polling_interval: int,
                 commitment_chain_length: int):
        super().__init__(network, last_block_persister, polling_interval, commitment_chain_length)

    def process_block(self, block: WrapperBlock):
        print('{}: new block received {} ({})'.format(self.network.type, block.number, block.hash))

        if not block.transactions:
            print('no transactions')
            return

        self.counter += 1
        address_transactions = collections.defaultdict(list)
        for transaction in block.transactions:
            from_address = transaction.inputs[0]
            to_address = transaction.outputs[0]
            if from_address:
                address_transactions[from_address.lower()].append(transaction)
            if to_address and to_address.address:
                address_transactions[to_address.address.lower()].append(transaction)
            else:
                if transaction.creates:
                    address_transactions[transaction.creates.lower()].append(transaction)
                else:
                    tx_receipt = self.network.get_tx_receipt(transaction.tx_hash)
                    contract_address = tx_receipt.contracts[0]
                    transaction.creates = contract_address
                    address_transactions[contract_address.lower()].append(transaction)

        block_event = BlockEvent(self.network, block, address_transactions)
        print(block_event)
        print()
        print(block_event.__dict__)
        print()
        for key, value in block_event.transactions_by_address.items():
            print(key)
            print(value.__dict__)
            print(value.outputs[0].__dict__)
            print()
        print()
        print()
        print()

        DucxPaymentMonitor().on_new_block_event(block_event)
