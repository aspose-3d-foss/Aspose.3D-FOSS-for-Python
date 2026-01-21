from typing import TYPE_CHECKING, Optional

from .IOConfig import IOConfig

if TYPE_CHECKING:
    from aspose.threed import FileFormat


class LoadOptions(IOConfig):
    def __init__(self):
        super().__init__()
        self._encoding = None
