from typing import TYPE_CHECKING

from ..A3DObject import A3DObject


class FontFile(A3DObject):
    """Font file contains definitions for glyphs, this is used to create text profile."""
    
    def __init__(self, name: str = None):
        super().__init__(name)
    
    @classmethod
    def from_file(cls, file_name: str) -> 'FontFile':
        """Load FontFile from file name."""
        raise NotImplementedError("from_file is not implemented")
    
    @classmethod
    def parse(cls, data: bytes) -> 'FontFile':
        """Parse FontFile from byte data."""
        raise NotImplementedError("parse is not implemented")
