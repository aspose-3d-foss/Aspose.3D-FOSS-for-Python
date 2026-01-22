from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .animation import AnimationNode, BindPoint, KeyframeSequence


class Property:
    def __init__(self, name: str, value=None):
        self._name = name
        self._value = value
        self._extra_data = {}

    @property
    def name(self) -> str:
        return self._name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def value_type(self):
        return type(self._value) if self._value is not None else type(None)

    def get_extra(self, name: str):
        return self._extra_data.get(name)

    def set_extra(self, name: str, value):
        self._extra_data[name] = value

    def get_bind_point(self, anim: 'AnimationNode', create: bool) -> 'BindPoint':
        return None

    def get_keyframe_sequence(self, anim: 'AnimationNode', create: bool) -> 'KeyframeSequence':
        return None

    def __repr__(self) -> str:
        return f"Property({self._name}, {self._value})"
