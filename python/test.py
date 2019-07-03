input = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x011\x00\x00\x00\x00\x00\x00\x03\xe8\x00\x00\x00\x00\x012\x00\x00\x00\x00\x00\x00\x07\xd0\x01\x00\x00\x00\x012'

class WAL:
    def __init__(self, binary_wal):
        self.epoch_milli = None # uint64
        self.mid = None # unsigned int
        self.mesage_length = None # uint32
        self.payload = None #

        wal_messages = []
        message = 0
        counter = 0

        for byte in input:
            print(byte.to_bytes(1, 'big'))
            if counter == 13:
                wal_messages.append(message.to_bytes((message.bit_length() + 8) // 8, 'little'))
                message = 0
                counter = 0
                continue
            message <<= 8
            message += byte
            counter += 1


print(input)
test = WAL(input)
