from typing import List, TYPE_CHECKING, Any

from ..A3DObject import A3DObject

_builtin_property = property


if TYPE_CHECKING:
    from ..Scene import Scene
    from ..Property import Property
    from .AnimationChannel import AnimationChannel
    from .KeyframeSequence import KeyframeSequence


class BindPoint(A3DObject):
    def __init__(self, scene: 'Scene', prop: 'Property'):
        super().__init__()
        self._scene = scene
        self._property = prop
        self._channels: List['AnimationChannel'] = []

    def add_channel(self, name: str, value: Any, type=None) -> bool:
        from .AnimationChannel import AnimationChannel
        channel = AnimationChannel(name)
        channel.default_value = value
        self._channels.append(channel)
        return True

    def get_keyframe_sequence(self, channel_name: str) -> 'KeyframeSequence':
        for channel in self._channels:
            if channel.name == channel_name and channel.keyframe_sequence:
                return channel.keyframe_sequence
        return None

    def create_keyframe_sequence(self, name: str) -> 'KeyframeSequence':
        from .KeyframeSequence import KeyframeSequence
        seq = KeyframeSequence(name)
        seq._bind_point = self
        return seq

    def bind_keyframe_sequence(self, channel_name: str, sequence: 'KeyframeSequence'):
        for channel in self._channels:
            if channel.name == channel_name:
                channel.keyframe_sequence = sequence
                if sequence:
                    sequence._bind_point = self._bind_point
                break

    def get_channel(self, channel_name: str) -> 'AnimationChannel':
        for channel in self._channels:
            if channel.name == channel_name:
                return channel
        return None

    def reset_channels(self):
        self._channels.clear()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def properties(self):
        return self._properties

    @_builtin_property
    def property(self) -> 'Property':
        return self._property

    @_builtin_property
    def channels_count(self) -> int:
        return len(self._channels)
