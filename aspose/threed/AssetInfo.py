from .A3DObject import A3DObject
from typing import Optional
from datetime import datetime


class AssetInfo(A3DObject):
    def __init__(self, name: str = None):
        super().__init__(name)
        self._title = ""
        self._subject = ""
        self._author = ""
        self._keywords = ""
        self._revision = ""
        self._comment = ""
        self._application_name = ""
        self._application_vendor = ""
        self._application_version = ""
        self._url = ""
        self._copyright = ""
        self._creation_time = None
        self._modification_time = None
        self._unit_name = ""
        self._unit_scale_factor = 1.0

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = str(value)

    @property
    def subject(self) -> str:
        return self._subject

    @subject.setter
    def subject(self, value: str):
        self._subject = str(value)

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str):
        self._author = str(value)

    @property
    def keywords(self) -> str:
        return self._keywords

    @keywords.setter
    def keywords(self, value: str):
        self._keywords = str(value)

    @property
    def revision(self) -> str:
        return self._revision

    @revision.setter
    def revision(self, value: str):
        self._revision = str(value)

    @property
    def comment(self) -> str:
        return self._comment

    @comment.setter
    def comment(self, value: str):
        self._comment = str(value)

    @property
    def application_name(self) -> str:
        return self._application_name

    @application_name.setter
    def application_name(self, value: str):
        self._application_name = str(value)

    @property
    def application_vendor(self) -> str:
        return self._application_vendor

    @application_vendor.setter
    def application_vendor(self, value: str):
        self._application_vendor = str(value)

    @property
    def application_version(self) -> str:
        return self._application_version

    @application_version.setter
    def application_version(self, value: str):
        self._application_version = str(value)

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value: str):
        self._url = str(value)

    @property
    def copyright(self) -> str:
        return self._copyright

    @copyright.setter
    def copyright(self, value: str):
        self._copyright = str(value)

    @property
    def creation_time(self) -> Optional[datetime]:
        return self._creation_time

    @creation_time.setter
    def creation_time(self, value: Optional[datetime]):
        self._creation_time = value

    @property
    def modification_time(self) -> Optional[datetime]:
        return self._modification_time

    @modification_time.setter
    def modification_time(self, value: Optional[datetime]):
        self._modification_time = value

    @property
    def unit_name(self) -> str:
        return self._unit_name

    @unit_name.setter
    def unit_name(self, value: str):
        self._unit_name = str(value)

    @property
    def unit_scale_factor(self) -> float:
        return self._unit_scale_factor

    @unit_scale_factor.setter
    def unit_scale_factor(self, value: float):
        self._unit_scale_factor = float(value)

    @property
    def coordinate_system(self):
        return None

    @coordinate_system.setter
    def coordinate_system(self, value):
        pass

    @property
    def up_vector(self):
        return None

    @up_vector.setter
    def up_vector(self, value):
        pass

    @property
    def front_vector(self):
        return None

    @front_vector.setter
    def front_vector(self, value):
        pass

    @property
    def axis_system(self):
        return None

    @axis_system.setter
    def axis_system(self, value):
        pass

    @property
    def ambient(self):
        return None

    @ambient.setter
    def ambient(self, value):
        pass
