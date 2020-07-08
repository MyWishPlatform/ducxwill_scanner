import collections

from scanner.services.scanner_polling import ScannerPolling
from blockchain_common.wrapper_block import WrapperBlock
from scanner.events.block_event import BlockEvent
from scanner.services.last_block_persister import LastBlockPersister
from . import DucxNetwork

from eventscanner.queue.subscribers import pub
from logger import logger


class DucxScanner(ScannerPolling):

    def __init__(self, network: DucxNetwork, last_block_persister: LastBlockPersister, polling_interval: int,
                 commitment_chain_length: int):
        super().__init__(network, last_block_persister, polling_interval, commitment_chain_length)

    def process_block(self, block: WrapperBlock):
        print('{}: new block received {} ({})'.format(self.network.type, block.number, block.hash), flush=True)

        if not block.transactions:
            print('{}: no transactions in {} ({})'.format(self.network.type, block.number, block.hash), flush=True)
            return

        address_transactions = collections.defaultdict(list)
        for transaction in block.transactions:
            from_address = transaction.inputs[0]
            to_address = transaction.outputs[0]
            if from_address:
                address_transactions[from_address.lower()].append(transaction)
            else:
                logger.warn(
                    '{}: Empty from field for transaction {}. Skip it.'.format(self.network.type, transaction.tx_hash))
            if to_address and to_address.address:
                address_transactions[to_address.address.lower()].append(transaction)
            else:
                if transaction.creates:
                    address_transactions[transaction.creates.lower()].append(transaction)
                else:
                    try:
                        tx_receipt = self.network.get_tx_receipt(transaction.tx_hash)
                        contract_address = tx_receipt.contracts[0]
                        transaction.creates = contract_address
                        address_transactions[contract_address.lower()].append(transaction)
                    except Exception:
                        logger.exception('{}: Error on getting transaction {} receipt.'.format(self.network.type,
                                                                                               transaction.tx_hash))
                        logger.warn(
                            '{}: Empty to and creates field for transaction {}. Skip it.'.format(self.network.type,
                                                                                                 transaction.tx_hash))

        print('{}: transactions'.format(self.network.type), address_transactions, flush=True)
        block_event = BlockEvent(self.network, block, address_transactions)

        pub.sendMessage(self.network.type, block_event=block_event)
