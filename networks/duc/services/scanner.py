from blockchain_common.wrapper_block import WrapperBlock
from scanner.services.scanner_polling import ScannerPolling


class DucScanner(ScannerPolling):

    def __init__(self, network, last_block_persister, polling_interval, commitment_chain_length):
        super().__init__(network, last_block_persister, polling_interval, commitment_chain_length)

    def process_block(self, block: WrapperBlock):
        if not block.transactions:
            return
