from typing import List, Tuple, Optional


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
    def __init__(self, text: str, token_type: int, line: int = 0, column: int = 0):
        self._text = text
        self._type = token_type
        self._line = line
        self._column = column

    @property
    def text(self) -> str:
        return self._text

    @property
    def type(self) -> int:
        return self._type

    @property
    def line(self) -> int:
        return self._line

    @property
    def column(self) -> int:
        return self._column

    def __repr__(self):
        return f"Token({TokenType.to_string(self._type)}, '{self._text}', line={self._line}, col={self._column})"


class FbxTokenizer:
    def __init__(self, data: str):
        self._data = data
        self._tokens: List[Token] = []

    def tokenize(self) -> List[Token]:
        line = 1
        column = 1
        in_comment = False
        in_double_quotes = False
        pending_data = False
        token_start = None
        token_end = None
        i = 0

        while i < len(self._data):
            c = self._data[i]

            if c == '\n':
                column = 0
                line += 1
                in_comment = False
                i += 1
            elif not in_comment:
                if in_double_quotes:
                    if c == '"':
                        in_double_quotes = False
                        token_end = i
                        self._process_data_token(token_start, token_end, TokenType.DATA, line, column)
                        pending_data = False
                        token_start = None
                        token_end = None
                    i += 1
                    continue

                if c == '"':
                    token_start = i
                    in_double_quotes = True
                    i += 1
                    continue

                if c == ';':
                    self._process_data_token(token_start, token_end, TokenType.DATA, line, column)
                    token_start = None
                    token_end = None
                    in_comment = True
                    i += 1
                    continue

                if c == '{':
                    self._process_data_token(token_start, token_end, TokenType.KEY, line, column)
                    token_start = None
                    token_end = None
                    self._tokens.append(Token('{', TokenType.OPEN_BRACKET, line, column))
                    i += 1
                    continue

                if c == '}':
                    self._process_data_token(token_start, token_end, TokenType.DATA, line, column)
                    token_start = None
                    token_end = None
                    self._tokens.append(Token('}', TokenType.CLOSE_BRACKET, line, column))
                    i += 1
                    continue

                if c == ',':
                    if pending_data:
                        self._process_data_token(token_start, token_end, TokenType.DATA, line, column, True)
                        token_start = None
                        token_end = None
                    self._tokens.append(Token(',', TokenType.COMMA, line, column))
                    i += 1
                    continue

                if c == ':':
                    if pending_data:
                        self._process_data_token(token_start, token_end, TokenType.KEY, line, column, True)
                        token_start = None
                        token_end = None
                    else:
                        raise ValueError(f"Unexpected colon at line {line}, column {column}")
                    i += 1
                    continue

                if c.isspace():
                    if token_start is not None:
                        peek_pos = i + 1
                        while peek_pos < len(self._data) and self._data[peek_pos].isspace() and self._data[peek_pos] != '\n':
                            peek_pos += 1

                        token_type = TokenType.DATA
                        if peek_pos < len(self._data) and self._data[peek_pos] == ':':
                            token_type = TokenType.KEY
                            i = peek_pos

                        self._process_data_token(token_start, token_end, token_type, line, column)
                        token_start = None
                        token_end = None
                    pending_data = False
                    i += 1
                else:
                    token_end = i
                    if token_start is None:
                        token_start = i
                    pending_data = True
                    i += 1

            else:
                i += 1

            column += 1

        return self._tokens

    def _process_data_token(self, start, end, token_type, line, column, must_have=False):
        if start is not None and end is not None:
            token_text = self._data[start:end + 1]
            self._tokens.append(Token(token_text, token_type, line, start + 1))
        elif must_have:
            raise ValueError(f"Unexpected character at line {line}, column {column}, expected data token")
