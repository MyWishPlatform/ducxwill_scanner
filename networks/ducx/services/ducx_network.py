from blockchain_common.wrapper_network import WrapperNetwork
from blockchain_common.parity_interface import ParityInterface
from networks.ducx.services.ducx_block import DucxBlock, DucxBlockMaker
from networks.ducx.services.ducx_transaction_receipt import DucxTransactionReceipt, DucxTransactionReceiptMaker


class DucxNetwork(WrapperNetwork):
    def __init__(self, type):
        super().__init__(type)
        self.parity = ParityInterface('ducx_testnet')

    def get_last_block(self) -> int:
        return int(self.parity.eth_blockNumber(), 16)

    def get_block(self, block_number) -> DucxBlock:
        block = self.parity.eth_getBlockByNumber(hex(block_number), True)
        return DucxBlockMaker.build(block)

    def get_tx_receipt(self, hash: str) -> DucxTransactionReceipt:
        tx_receipt = self.parity.eth_getTransactionReceipt(hash)
        return DucxTransactionReceiptMaker.build(tx_receipt)
