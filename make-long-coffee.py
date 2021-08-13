#!/usr/bin/env python3

import pygatt
import time

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
    # wait for startup
    time.sleep(45)
    # make long coffee
    # byte position 9 is "amount", 10 is "hotness", 11 is "aroma intensity"
    send(device, [0x0d, 0x0f, 0x83, 0xf0, 0x03, 0x01, 0x01, 0x00, 0xb4, 0x02, 0x01, 0x00, 0x00, 0x06])
finally:
    adapter.stop()
