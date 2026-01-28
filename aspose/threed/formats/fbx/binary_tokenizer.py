import struct


class TokenType:
    OPEN_BRACKET = 0
    CLOSE_BRACKET = 1
    DATA = 2
    COMMA = 3
    KEY = 4

    @staticmethod
    def to_string(t):
        names = {
            0: 'OPEN_BRACKET',
            1: 'CLOSE_BRACKET',
            2: 'DATA',
            3: 'COMMA',
            4: 'KEY'
        }
        return names.get(t, 'UNKNOWN')


class Token:
    def __init__(self, value, token_type: int):
        self._value = value
        self._type = token_type

    @property
    def value(self):
        return self._value

    @property
    def text(self):
        if isinstance(self._value, str):
            return self._value
        return str(self._value)

    @property
    def type(self) -> int:
        return self._type

    def __repr__(self):
        return f"Token({TokenType.to_string(self._type)}, {repr(self._value)})"


class BinaryTokenizer:
    def __init__(self, data):
        self.data = data
        self.cursor = 0
        self.is_64bit = False

    def tokenize(self):
        if len(self.data) < 27:
            raise ValueError("File is too short")

        magic = self.data[0:18].decode('ascii', errors='ignore')
        if magic != 'Kaydara FBX Binary':
            raise ValueError("Invalid FBX binary file header")

        self.cursor = 18
        
        self.cursor += 5
        
        version = self._read_uint32()
        self.is_64bit = version >= 7500

        tokens = []
        while self.cursor < len(self.data):
            try:
                if not self._read_scope(tokens):
                    break
            except EOFError:
                break

        return tokens

    def _read_scope(self, tokens):
        end_offset = self._read_offset()

        if end_offset == 0:
            return False

        if end_offset > len(self.data):
            raise ValueError(f"Block offset {end_offset} is out of range")
        if end_offset < self.cursor:
            raise ValueError(f"Block offset {end_offset} is negative")

        prop_count = self._read_offset()
        prop_length = self._read_offset()

        name = self._read_string()
        tokens.append(Token(name, 4))

        begin_cursor = self.cursor

        if begin_cursor + prop_length > len(self.data):
            raise ValueError("Property length out of bounds")

        for i in range(prop_count):
            data = self._read_data(begin_cursor + prop_length)
            tokens.append(Token(data, 2))

            if i != prop_count - 1:
                tokens.append(Token(',', 3))

        if self.cursor - begin_cursor != prop_length:
            raise ValueError("Property length not reached")

        sentinel_block_length = 25 if self.is_64bit else 13

        if self.cursor < end_offset:
            if end_offset - self.cursor < sentinel_block_length:
                raise ValueError("Insufficient padding bytes at block end")

            tokens.append(Token('{', 0))

            end = end_offset - sentinel_block_length
            while self.cursor < end:
                self._read_scope(tokens)

            tokens.append(Token('}', 1))

            sentinel = self.data[self.cursor:self.cursor + sentinel_block_length]
            if any(b != 0 for b in sentinel):
                raise ValueError("Failed to read nested block sentinel")
            self.cursor += sentinel_block_length

        if self.cursor != end_offset:
            raise ValueError("Scope length not reached")

        return True

    def _read_offset(self):
        if self.is_64bit:
            return self._read_uint64()
        return self._read_uint32()

    def _read_uint32(self):
        if self.cursor + 4 > len(self.data):
            raise EOFError()
        value = struct.unpack('<I', self.data[self.cursor:self.cursor + 4])[0]
        self.cursor += 4
        return value

    def _read_uint64(self):
        if self.cursor + 8 > len(self.data):
            raise EOFError()
        value = struct.unpack('<Q', self.data[self.cursor:self.cursor + 8])[0]
        self.cursor += 8
        return value

    def _read_int16(self):
        if self.cursor + 2 > len(self.data):
            raise EOFError()
        value = struct.unpack('<h', self.data[self.cursor:self.cursor + 2])[0]
        self.cursor += 2
        return value

    def _read_int32(self):
        if self.cursor + 4 > len(self.data):
            raise EOFError()
        value = struct.unpack('<i', self.data[self.cursor:self.cursor + 4])[0]
        self.cursor += 4
        return value

    def _read_int64(self):
        if self.cursor + 8 > len(self.data):
            raise EOFError()
        value = struct.unpack('<q', self.data[self.cursor:self.cursor + 8])[0]
        self.cursor += 8
        return value

    def _read_float32(self):
        if self.cursor + 4 > len(self.data):
            raise EOFError()
        value = struct.unpack('<f', self.data[self.cursor:self.cursor + 4])[0]
        self.cursor += 4
        return value

    def _read_float64(self):
        if self.cursor + 8 > len(self.data):
            raise EOFError()
        value = struct.unpack('<d', self.data[self.cursor:self.cursor + 8])[0]
        self.cursor += 8
        return value

    def _read_byte(self):
        if self.cursor + 1 > len(self.data):
            raise EOFError()
        value = self.data[self.cursor]
        self.cursor += 1
        return value

    def _read_string(self, long_length=False):
        len_len = 4 if long_length else 1
        if self.cursor + len_len > len(self.data):
            raise EOFError()

        if long_length:
            length = self._read_uint32()
        else:
            length = self._read_byte()

        if self.cursor + length > len(self.data):
            raise EOFError()

        s = self.data[self.cursor:self.cursor + length].decode('utf-8', errors='ignore')
        self.cursor += length
        return s

    def _read_data(self, limit):
        if self.cursor >= len(self.data):
            raise EOFError()

        type_char = chr(self._read_byte())
        start_cursor = self.cursor - 1

        if type_char == 'Y':
            self.cursor += 2
            value = struct.unpack('<h', self.data[self.cursor - 2:self.cursor])[0]
        elif type_char == 'C':
            value = bool(self._read_byte())
        elif type_char == 'I':
            value = self._read_int32()
        elif type_char == 'F':
            value = self._read_float32()
        elif type_char == 'D':
            value = self._read_float64()
        elif type_char == 'L':
            value = self._read_int64()
        elif type_char == 'R':
            length = self._read_uint32()
            raw_data = self.data[self.cursor:self.cursor + length]
            self.cursor += length
            value = raw_data
        elif type_char in 'fdlic':
            length = self._read_uint32()
            encoding = self._read_uint32()
            comp_len = self._read_uint32()

            array_data = self.data[self.cursor:self.cursor + comp_len]
            self.cursor += comp_len

            if encoding == 0:
                if type_char == 'f' or type_char == 'i':
                    stride = 4
                elif type_char == 'd' or type_char == 'l':
                    stride = 8
                else:
                    stride = 1

                expected_len = length * stride
                if len(array_data) != expected_len:
                    raise ValueError(f"Array length mismatch: type={type_char}, length={length}, stride={stride}, expected_len={expected_len}, actual_len={len(array_data)}")

                if type_char == 'f':
                    values = list(struct.unpack(f'<{length}f', array_data))
                elif type_char == 'd':
                    values = list(struct.unpack(f'<{length}d', array_data))
                elif type_char == 'i':
                    values = list(struct.unpack(f'<{length}i', array_data))
                elif type_char == 'l':
                    values = list(struct.unpack(f'<{length}q', array_data))
                elif type_char == 'c':
                    values = list(array_data)
                else:
                    values = array_data

                value = values
            elif encoding == 1:
                import zlib
                decompressed = zlib.decompress(array_data)
                
                if type_char == 'f':
                    values = list(struct.unpack(f'<{length}f', decompressed))
                elif type_char == 'd':
                    values = list(struct.unpack(f'<{length}d', decompressed))
                elif type_char == 'i':
                    values = list(struct.unpack(f'<{length}i', decompressed))
                elif type_char == 'l':
                    values = list(struct.unpack(f'<{length}q', decompressed))
                elif type_char == 'c':
                    values = list(decompressed)
                else:
                    values = decompressed

                value = values
            else:
                raise ValueError(f"Unknown encoding {encoding}")
        elif type_char == 'S':
            value = self._read_string(long_length=True)
        else:
            raise ValueError(f"Unexpected type code: {type_char}")

        if self.cursor > limit:
            raise ValueError(f"Data exceeds limit")

        return value
