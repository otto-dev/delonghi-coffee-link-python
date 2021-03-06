#!/usr/bin/env python3
from common import *

bd_addr = "00:a0:50:83:31:dc" # insert your Bluetooth Address

adapter = None
try:
    (adapter, device) = connect(bd_addr)
    send(device, [0x0d, 0x07, 0x84, 0x0f, 0x02, 0x01])
finally:
    if adapter:
        adapter.stop()
