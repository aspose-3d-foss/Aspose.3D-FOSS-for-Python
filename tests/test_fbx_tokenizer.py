import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aspose.threed.formats.fbx.tokenizer import FbxTokenizer
from aspose.threed.formats.fbx.parser import FbxParser


def test_tokenizer():
    with open('examples/fbx7400ascii/box.fbx', 'r') as f:
        content = f.read()

    tokenizer = FbxTokenizer(content)
    tokens = tokenizer.tokenize()

    print(f"Tokenized {len(tokens)} tokens")
    for i, token in enumerate(tokens[:20]):
        print(f"  {i}: {token}")

    return tokens


def test_parser(tokens):
    parser = FbxParser(tokens)
    print(f"\nParsed root scope with {len(parser.root_scope.elements)} top-level elements")

    for key in list(parser.root_scope.elements.keys())[:10]:
        elements = parser.root_scope.get_elements(key)
        print(f"  {key}: {len(elements)} element(s)")


if __name__ == '__main__':
    tokens = test_tokenizer()
    test_parser(tokens)
    print("\nTest completed successfully!")
