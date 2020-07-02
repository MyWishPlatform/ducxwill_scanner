from __future__ import annotations

from blockchain_common.wrapper_transaction import WrapperTransaction


class DucTransaction(WrapperTransaction):

    @staticmethod
    def build(transaction: dict) -> DucTransaction:
        hash = transaction['txid']
        inputs = [i for i in transaction['vin']]
        outputs = [o for o in transaction['vout']]
        contract_creation = False
        creates = "False"

        return DucTransaction(hash, inputs, outputs, contract_creation, creates)
