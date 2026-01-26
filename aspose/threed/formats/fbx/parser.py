from typing import List, Optional, Dict, Any
from .tokenizer import Token, TokenType


class FbxElement:
    def __init__(self, key_token: Token):
        self._key_token = key_token
        self._tokens: List[Token] = []
        self._compound: Optional['FbxScope'] = None

    @property
    def key(self) -> str:
        return self._key_token.text

    @property
    def tokens(self) -> List[Token]:
        return self._tokens

    @property
    def compound(self) -> Optional['FbxScope']:
        return self._compound

    def add_token(self, token: Token):
        self._tokens.append(token)

    def set_compound(self, scope: 'FbxScope'):
        self._compound = scope


class FbxScope:
    def __init__(self):
        self._elements: Dict[str, List[FbxElement]] = {}

    @property
    def elements(self) -> Dict[str, List[FbxElement]]:
        return self._elements

    def add_element(self, element: FbxElement):
        key = element.key
        if key not in self._elements:
            self._elements[key] = []
        self._elements[key].append(element)

    def get_elements(self, key: str) -> List[FbxElement]:
        return self._elements.get(key, [])

    def get_first_element(self, key: str) -> Optional[FbxElement]:
        elements = self.get_elements(key)
        return elements[0] if elements else None


class FbxParser:
    def __init__(self, tokens: List[Token]):
        self._tokens = tokens
        self._position = 0
        self._root_scope = None
        self._parse()

    @property
    def root_scope(self) -> FbxScope:
        return self._root_scope

    def _current_token(self) -> Optional[Token]:
        if self._position < len(self._tokens):
            return self._tokens[self._position]
        return None

    def _advance(self) -> Optional[Token]:
        if self._position < len(self._tokens):
            token = self._tokens[self._position]
            self._position += 1
            return token
        return None

    def _parse(self):
        self._root_scope = self._parse_scope(top_level=True)

    def _parse_scope(self, top_level=False) -> FbxScope:
        scope = FbxScope()

        if not top_level:
            token = self._current_token()
            if token is None or token.type != TokenType.OPEN_BRACKET:
                raise ValueError(f"Expected OPEN_BRACKET, got {token}")
            self._advance()

        while True:
            token = self._current_token()
            if token is None:
                if top_level:
                    break
                raise ValueError("Unexpected end of file, expected closing bracket")

            if token.type == TokenType.CLOSE_BRACKET:
                if top_level:
                    break
                self._advance()
                return scope

            if token.type == TokenType.KEY:
                element = self._parse_element()
                scope.add_element(element)
            else:
                raise ValueError(f"Unexpected token type {token.type}, expected KEY or CLOSE_BRACKET")

        return scope

    def _parse_element(self) -> FbxElement:
        token = self._current_token()
        if token is None or token.type != TokenType.KEY:
            raise ValueError(f"Expected KEY token, got {token}")

        element = FbxElement(token)
        self._advance()

        while True:
            token = self._current_token()
            if token is None:
                raise ValueError("Unexpected end of file, expected closing bracket or key")

            if token.type == TokenType.DATA:
                element.add_token(token)
                self._advance()

                next_token = self._current_token()
                if next_token is None:
                    raise ValueError("Unexpected end of file, expected bracket, comma or key")

                if next_token.type == TokenType.DATA and next_token.line == token.line + 1:
                    element.add_token(next_token)
                    self._advance()
                    continue

                if next_token.type not in [TokenType.OPEN_BRACKET, TokenType.CLOSE_BRACKET, TokenType.COMMA, TokenType.KEY]:
                    raise ValueError(f"Unexpected token type {next_token.type}, expected bracket, comma or key")

            elif token.type == TokenType.OPEN_BRACKET:
                child_scope = self._parse_scope()
                element.set_compound(child_scope)
                return element

            elif token.type == TokenType.KEY or token.type == TokenType.CLOSE_BRACKET:
                return element

            elif token.type == TokenType.COMMA:
                self._advance()

            else:
                self._advance()

    def parse_value(self, token: Token) -> Any:
        text = token.text.strip('"')

        if text.startswith('a:'):
            return self._parse_array(text[2:])

        try:
            return int(text)
        except ValueError:
            try:
                return float(text)
            except ValueError:
                return text

    def _parse_array(self, data: str) -> List[Any]:
        values = []
        parts = data.split(',')
        for part in parts:
            part = part.strip()
            if not part:
                continue
            try:
                values.append(int(part))
            except ValueError:
                try:
                    values.append(float(part))
                except ValueError:
                    values.append(part.strip('"'))
        return values
