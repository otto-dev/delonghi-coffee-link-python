#!/usr/bin/python
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


data = bytearray([0x0d, 0x07, 0x84, 0x0f, 0x02, 0x01])
print(sign(data))

