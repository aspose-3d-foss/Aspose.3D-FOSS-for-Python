from typing import TYPE_CHECKING

from ..Entity import Entity

if TYPE_CHECKING:
    from .SkeletonType import SkeletonType
    from .Curve import Curve
    from .IMeshConvertible import IMeshConvertible
    from ..Node import Node


class Skeleton(Entity):
    """The Skeleton is mainly used by CAD software to help designer to manipulate the transformation of skeletal structure, it's usually useless outside the CAD softwares.
    To make the skeleton hierarchy acts like one object in CAD software, it's necessary to mark the top Skeleton node as the root one by setting type to SKELETON,
    and all children set to BONE"""
    
    def __init__(self, name: str = None):
        """Constructor of Skeleton."""
        if name is None:
            name = "Skeleton"
        super().__init__(name)
        self._type = SkeletonType.Skeleton
    
    @property
    def type(self) -> 'SkeletonType':
        """Gets the skeleton type."""
        return self._type
    
    @type.setter
    def type(self, value: 'SkeletonType') -> None:
        """Sets the skeleton type."""
        self._type = value
    
    @property
    def size(self) -> float:
        """Gets or sets the size of the skeleton."""
        raise NotImplementedError("size is not implemented")
    
    @size.setter
    def size(self, value: float) -> None:
        """Gets or sets the size of the skeleton."""
        raise NotImplementedError("size is not implemented")
    
    @property
    def joints(self):
        """Gets the joints of the skeleton."""
        raise NotImplementedError("joints is not implemented")
    
    @property
    def mesh(self):
        """Gets the mesh of the skeleton."""
        raise NotImplementedError("mesh is not implemented")
