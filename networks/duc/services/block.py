from blockchain_common.wrapper_block import WrapperBlock
from .transaction import DucTransaction


class DucBlock(WrapperBlock):

    @staticmethod
    def build(block: dict):
        hash = block['hash']
        number = block['heigth']
        timestamp = block['time']
        transactions = [DucTransaction(t) for t in block['tx']]
        return DucBlock(hash, number, timestamp, transactions)
