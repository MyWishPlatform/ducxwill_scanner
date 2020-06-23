from pubsub import pub

from eventscanner.monitors.payments.ducx_payment_monitor import DucxPaymentMonitor
from eventscanner.monitors.contracts.deploy_monitor import DeployMonitor


pub.subscribe(DucxPaymentMonitor.on_new_block_event, 'DUCATUSX_MAINNET')
pub.subscribe(DucxPaymentMonitor.on_new_block_event, 'BINANCE_TESTNET')
pub.subscribe(DeployMonitor.on_new_block_event, 'DUCATUSX_MAINNET')
pub.subscribe(DeployMonitor.on_new_block_event, 'DUCATUSX_TESTNET')
