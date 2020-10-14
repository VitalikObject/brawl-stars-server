import zlib

from io import BufferedReader, BytesIO


class BSMessageReader(BufferedReader):
    def __init__(self, initial_bytes, endian: str = 'big'):
        super().__init__(BytesIO(initial_bytes))
        self.buffer = initial_bytes
        self.endian = endian
        self.i = 0

    def read_byte(self):
        return int.from_bytes(self.read(1), "big")

    def read_Vint(self):
        n = self._read_varint(True)
        return (n >> 1) ^ (-(n & 1))

    def read_short(self, length=2):
        return int.from_bytes(self.read(length), "big")

    def read_int(self, length=4):
        return int.from_bytes(self.read(length), "big")

    def readUInt8(self) -> int:
        return self.readUInteger()

    def readUInteger(self, length: int = 1) -> int:
        result = 0
        for x in range(length):
            byte = self.buffer[self.i]

            bit_padding = x * 8
            if self.endian == 'big':
                bit_padding = (8 * (length - 1)) - bit_padding

            result |= byte << bit_padding
            self.i += 1

        return result

    def _read_varint(self, rotate: bool = True):
        result = 0
        shift = 0
        while True:
            byte = self.read_byte()
            if rotate and shift == 0:
                seventh = (byte & 0x40) >> 6  # save 7th bit
                msb = (byte & 0x80) >> 7  # save msb
                n = byte << 1  # rotate to the left
                n = n & ~0x181  # clear 8th and 1st bit and 9th if any
                byte = n | (msb << 7) | seventh  # insert msb and 6th back in
            result |= (byte & 0x7f) << shift
            shift += 7
            if not (byte & 0x80):
                break
        return result

    def read_rrsint32(self):
        n = self._read_varint(True)
        return (n >> 1) ^ (-(n & 1))

    def readBool(self) -> bool:
        if self.readUInt8() >= 1:
            return True
        else:
            return False

    def read_string(self):
        length = self.read_int()
        if length == pow(2, 32) - 1:
            return b""
        else:
            try:
                decoded = self.read(length)
            except MemoryError:
                raise IndexError("String out of range.")
            else:
                return decoded.decode('utf-8')

    def peek_int(self, length=4):
        return int.from_bytes(self.peek(length)[:length], "big")
