from .INamedObject import INamedObject
from .PropertyCollection import PropertyCollection


class A3DObject(INamedObject):
    def __init__(self, name: str = None):
        self._name = name if name is not None else ""
        self._properties = PropertyCollection()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = str(value)

    @property
    def properties(self) -> PropertyCollection:
        return self._properties

    def find_property(self, property_name: str):
        return self._properties.find_property(property_name)

    def get_property(self, property: str):
        return self._properties.get(property)

    def set_property(self, property: str, value):
        existing = self._properties.find_property(property)
        if existing:
            existing.value = value
        else:
            from .property import Property
            new_prop = Property(property, value)
            self._properties._properties.append(new_prop)

    def remove_property(self, property):
        return self._properties.remove_property(property)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._name})"
