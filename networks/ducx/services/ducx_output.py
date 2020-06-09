from blockchain_common.wrapper_output import WrapperOutput


class DucxOutput(WrapperOutput):
    @classmethod
    def build(self, transaction) -> WrapperOutput:
        return WrapperOutput(
            transaction['hash'],
            0,
            transaction['to'],
            int(transaction['value'], 16),
            transaction['input']
        )
