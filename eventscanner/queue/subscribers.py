from pubsub import pub

from eventscanner.monitors.payments.ducx_payment_monitor import DucxPaymentMonitor


pub.subscribe(DucxPaymentMonitor.on_new_block_event, 'DUCSTUSX_MAINNET')
