from blockchain_common.wrapper_transaction_receipt import WrapperTransactionReceipt


class DucxTransactionReceipt(WrapperTransactionReceipt):
    pass


class DucxTransactionReceiptMaker:
    @staticmethod
    def build(transaction_receipt: dict) -> DucxTransactionReceipt:
        tx_hash = transaction_receipt['transactionHash']
        contracts = [transaction_receipt['contractAddress']]
        logs = 'logs'
        success = bool(int(transaction_receipt['status'], 16))
        return DucxTransactionReceipt(tx_hash, contracts, logs, success)
