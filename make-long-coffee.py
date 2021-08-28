#!/usr/bin/env python3

from common import *
import time

bd_addr = "00:a0:50:83:31:dc" # insert your Bluetooth Address

adapter = None
try:
    (adapter, device) = connect(bd_addr)
    send(device, [0x0d, 0x07, 0x84, 0x0f, 0x02, 0x01])
    # wait for startup
    time.sleep(45)
    send(device, [0x0d, 0x0f, 0x83, 0xf0, 0x03, 0x01, 0x01, 0x00, 0xb4, 0x02, 0x01, 0x00, 0x00, 0x06])
finally:
    if adapter:
        adapter.stop()
