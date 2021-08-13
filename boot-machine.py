#!/usr/bin/env python3

import pygatt

bd_addr =        "00:a0:50:83:31:dc" # insert your Bluetooth Address
characteristic = "00035b03-58e6-07dd-021a-08123a000301"
#descriptor =    "00002902-0000-1000-8000-00805f9b34fb"

adapter = pygatt.GATTToolBackend()

def sign(data : bytearray):
    crc = 0x1D0F
    for i in range(0, len(data)):
        crc ^= data[i] << 8
        for _ in range(0,8):
            if (crc & 0x8000) > 0:
                crc =(crc << 1) ^ 0x1021
            else:
                crc = crc << 1
    return data + bytearray((crc & 0xFFFF).to_bytes(2, byteorder='big'))

def send(device, bytes):
  device.char_write(characteristic, sign(bytearray(bytes)))

try:
    adapter.start()
    device = adapter.connect(bd_addr)
    # turn on machine:
    send(device, [0x0d, 0x07, 0x84, 0x0f, 0x02, 0x01])
finally:
    adapter.stop()
