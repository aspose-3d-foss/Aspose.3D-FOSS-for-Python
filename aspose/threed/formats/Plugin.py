from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Importer import Importer
    from .Exporter import Exporter
    from .FormatDetector import FormatDetector
    from .LoadOptions import LoadOptions
    from .SaveOptions import SaveOptions
    from aspose.threed import FileFormat


class Plugin(ABC):
    @abstractmethod
    def get_file_format(self) -> 'FileFormat':
        pass
    
    @abstractmethod
    def get_importer(self) -> 'Importer':
        pass
    
    @abstractmethod
    def get_exporter(self) -> 'Exporter':
        pass
    
    @abstractmethod
    def get_format_detector(self) -> 'FormatDetector':
        pass
    
    @abstractmethod
    def create_load_options(self) -> 'LoadOptions':
        pass
    
    @abstractmethod
    def create_save_options(self) -> 'SaveOptions':
        pass
