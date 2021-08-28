#!/usr/bin/env python3
from common import *

bd_addr = "00:a0:50:83:31:dc" # insert your Bluetooth Address

adapter = None
try:
    (adapter, device) = connect(bd_addr)
    send(device, [0x0d, 0x0d, 0x83, 0xf0, 0x10, 0x01, 0x0f, 0x00, 0x05, 0x1c, 0x01, 0x06])
finally:
    if adapter:
        adapter.stop()
