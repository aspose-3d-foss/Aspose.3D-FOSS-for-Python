class Watermark:
    """Utility to encode/decode blind watermark to/from a mesh."""

    @staticmethod
    def encode_watermark(input: 'Mesh', text: str) -> 'Mesh':
        raise NotImplementedError("encode_watermark is not implemented")

    @staticmethod
    def encode_watermark(input: 'Mesh', text: str, password: str) -> 'Mesh':
        raise NotImplementedError("encode_watermark is not implemented")

    @staticmethod
    def encode_watermark(input: 'Mesh', text: str, password: str, permanent: bool) -> 'Mesh':
        raise NotImplementedError("encode_watermark is not implemented")

    @staticmethod
    def decode_watermark(input: 'Mesh') -> str:
        raise NotImplementedError("decode_watermark is not implemented")

    @staticmethod
    def decode_watermark(input: 'Mesh', password: str) -> str:
        raise NotImplementedError("decode_watermark is not implemented")
