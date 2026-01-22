from typing import List, TYPE_CHECKING

from ..A3DObject import A3DObject


if TYPE_CHECKING:
    from ..Property import Property
    from .BindPoint import BindPoint
    from .KeyframeSequence import KeyframeSequence


class AnimationNode(A3DObject):
    def __init__(self, name: str = None):
        super().__init__(name)
        self._bind_points: List[BindPoint] = []
        self._sub_animations: List['AnimationNode'] = []

    def find_bind_point(self, target: 'A3DObject', name: str) -> 'BindPoint':
        for bp in self._bind_points:
            if bp.property.name == name:
                return bp
        return None

    def get_bind_point(self, target: 'A3DObject', prop_name: str, create: bool) -> 'BindPoint':
        from .BindPoint import BindPoint
        prop = target.find_property(prop_name)
        if prop:
            bp = self.find_bind_point(target, prop_name)
            if bp is None and create:
                bp = BindPoint(target.scene, prop)
                self._bind_points.append(bp)
            return bp
        return None

    def create_bind_point(self, obj: 'A3DObject', prop_name: str) -> 'BindPoint':
        from .BindPoint import BindPoint
        prop = obj.find_property(prop_name)
        if prop:
            bp = BindPoint(obj.scene, prop)
            self._bind_points.append(bp)
            return bp
        return None

    def get_keyframe_sequence(self, target: 'A3DObject', prop_name: str, channel_name: str = None, create: bool = True) -> 'KeyframeSequence':
        from .KeyframeSequence import KeyframeSequence
        bp = self.get_bind_point(target, prop_name, create)
        if bp is None:
            return None

        if channel_name:
            channel = bp.get_channel(channel_name)
            if channel:
                seq = channel.keyframe_sequence
                if seq is None and create:
                    seq = bp.create_keyframe_sequence(channel_name)
                    channel.keyframe_sequence = seq
                return seq
            elif create:
                seq = bp.create_keyframe_sequence(channel_name)
                bp.bind_keyframe_sequence(channel_name, seq)
                return seq
        else:
            return bp.create_keyframe_sequence(prop_name)

        return None

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def properties(self):
        return self._properties

    @property
    def bind_points(self) -> List['BindPoint']:
        return list(self._bind_points)

    @property
    def sub_animations(self) -> List['AnimationNode']:
        return list(self._sub_animations)
