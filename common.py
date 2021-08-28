import pygatt

characteristic = "00035b03-58e6-07dd-021a-08123a000301"

connection_attempts = 5
timeout = 10.0

def connect(bd_addr):
    adapter = pygatt.GATTToolBackend()
    adapter.start()
    device = None
    for _ in range(0, connection_attempts):
        try:
            device = adapter.connect(bd_addr, timeout=1.0)
        except:
            pass
        else:
            break
    else:
        raise Exception('Failed to connect after {} attempts.'.format(connection_attempts))
    return (adapter, device)

def _sign(data : bytearray):
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
  device.char_write(characteristic, _sign(bytearray(bytes)))

