import os


class LastBlockPersister:
    base_dir = 'settings'

    def __init__(self, network: str):
        self.network = network

    def get_last_block(self) -> int:
        with open(os.path.join(self.base_dir, self.network), 'r') as file:
            last_block_number = file.read()
        return int(last_block_number)

    def save_last_block(self, last_block_number: int):
        with open(os.path.join(self.base_dir, self.network), 'w') as file:
            file.write(str(last_block_number))
