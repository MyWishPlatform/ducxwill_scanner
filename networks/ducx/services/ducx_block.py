from blockchain_common.wrapper_block import WrapperBlock
from networks.ducx.services.ducx_transaction import DucxTransactionMaker


class DucxBlock(WrapperBlock):
    pass


class DucxBlockMaker:
    @staticmethod
    def build(block: dict) -> DucxBlock:
        hash = block['hash']
        number = int(block['number'], 16)
        timestamp = int(block['timestamp'], 16)
        transactions = [DucxTransactionMaker.build(transaction) for transaction in block['transactions']]
        return DucxBlock(hash, number, timestamp, transactions)
