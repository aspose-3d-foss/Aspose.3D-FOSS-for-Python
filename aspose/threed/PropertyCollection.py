from typing import List


class PropertyCollection:
    def __init__(self):
        self._properties = []

    @property
    def count(self) -> int:
        return len(self._properties)

    def find_property(self, property_name: str):
        for prop in self._properties:
            if prop.name == property_name:
                return prop
        return None

    def get(self, property: str):
        prop = self.find_property(property)
        return prop.value if prop else None

    def remove_property(self, property):
        if isinstance(property, str):
            prop = self.find_property(property)
            if prop:
                self._properties.remove(prop)
                return True
            return False
        elif hasattr(property, 'name'):
            if property in self._properties:
                self._properties.remove(property)
                return True
            return False
        return False

    def __getitem__(self, key: int):
        return self._properties[key]

    def __len__(self):
        return len(self._properties)

    def __iter__(self):
        return iter(self._properties)

    def __repr__(self) -> str:
        return f"PropertyCollection({len(self._properties)} properties)"
