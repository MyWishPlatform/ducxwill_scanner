from blockchain_common.wrapper_transaction import WrapperTransaction
from networks.ducx.services.ducx_output import DucxOutput


class DucxTransaction(WrapperTransaction):
    pass


class DucxTransactionMaker:
    zero_address = '0x0000000000000000000000000000000000000000'

    @classmethod
    def build(self, transaction: dict) -> DucxTransaction:
        hash = transaction['hash']
        inputs = [transaction['from']]
        outputs = [DucxOutput.build(transaction)]
        contract_creation = not transaction['to'] or transaction['to'] == self.zero_address
        creates = transaction.get('creates')

        return DucxTransaction(hash, inputs, outputs, contract_creation, creates)
