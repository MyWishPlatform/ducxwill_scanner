from scanner.events.block_event import BlockEvent
from mywish_models.models import UserSiteBalance, session
from eventscanner.queue.pika_handler import send_in_queue


class DucxPaymentMonitor:
    def on_new_block_event(self, block_event: BlockEvent):
        addresses = block_event.transactions_by_address.keys()
        user_site_balances = session.query(UserSiteBalance).filter(UserSiteBalance.eth_address.in_(addresses)).all()
        for user_site_balance in user_site_balances:
            transactions = block_event.transactions_by_address[user_site_balance.eth_address.lower()]

            if not transactions:
                print('fail')

            for transaction in transactions:
                if user_site_balance.eth_address.lower() != transaction.outputs[0].address.lower():
                    print('transaction from internal address. Skip')
                    continue

                tx_receipt = block_event.network.get_tx_receipt(transaction.tx_hash)

                message = {
                    'userId': user_site_balance.user.id,
                    'transactionHash': transaction.tx_hash,
                    'currency': 'DUCX',
                    'amount': transaction.outputs[0].value,
                    'siteId': user_site_balance.subsite.id,
                    'success': tx_receipt.success,
                    'status': 'COMMITED'
                }

                send_in_queue('payment', 'notification-ducatusx-mainnet', message)
