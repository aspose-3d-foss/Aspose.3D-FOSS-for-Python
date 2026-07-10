from typing import TYPE_CHECKING

from .Profile import Profile


class Text(Profile):
    """Text profile, this profile describes contours using font and text."""
    
    def __init__(self, name: str = None):
        super().__init__(name)
        self._content = ""
        self._font = None
        self._font_size = 1.0
    
    @property
    def content(self) -> str:
        return self._content
    
    @content.setter
    def content(self, value: str):
        self._content = str(value)
    
    @property
    def font(self):
        return self._font
    
    @font.setter
    def font(self, value):
        self._font = value
    
    @property
    def font_size(self) -> float:
        return self._font_size
    
    @font_size.setter
    def font_size(self, value: float):
        self._font_size = float(value)
