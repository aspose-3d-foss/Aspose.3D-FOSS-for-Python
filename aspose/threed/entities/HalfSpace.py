from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aspose.threed import Entity


class HalfSpace:
    """HalfSpace represents a infinity space which is split by a plane, this can be used with BooleanOperator"""
    
    def __init__(self, *args):
        raise NotImplementedError("__init__ is not implemented")
    
    def remove_property(self, *args) -> bool:
        raise NotImplementedError("remove_property is not implemented")
    
    def get_property(self, property: str):
        raise NotImplementedError("get_property is not implemented")
    
    def set_property(self, property: str, value):
        raise NotImplementedError("set_property is not implemented")
    
    def find_property(self, property_name: str):
        raise NotImplementedError("find_property is not implemented")
    
    def get_bounding_box(self):
        raise NotImplementedError("get_bounding_box is not implemented")
    
    def get_entity_renderer_key(self):
        raise NotImplementedError("get_entity_renderer_key is not implemented")
    
    @property
    def name(self) -> str:
        """Gets the name."""
        raise NotImplementedError("name is not implemented")
    
    @name.setter
    def name(self, value: str):
        """Sets the name."""
        raise NotImplementedError("name is not implemented")
    
    @property
    def properties(self):
        """Gets the collection of all properties."""
        raise NotImplementedError("properties is not implemented")
    
    @property
    def scene(self):
        """Gets the scene that this object belongs to."""
        raise NotImplementedError("scene is not implemented")
    
    @property
    def parent_nodes(self):
        """Gets all parent nodes, an entity can be attached to multiple parent nodes for geometry instancing."""
        raise NotImplementedError("parent_nodes is not implemented")
    
    @property
    def excluded(self) -> bool:
        """Gets whether to exclude this entity during exporting."""
        raise NotImplementedError("excluded is not implemented")
    
    @excluded.setter
    def excluded(self, value: bool):
        """Sets whether to exclude this entity during exporting."""
        raise NotImplementedError("excluded is not implemented")
    
    @property
    def parent_node(self):
        """Gets the first parent node, if set the first parent node, this entity will be detached from other parent nodes."""
        raise NotImplementedError("parent_node is not implemented")
    
    @parent_node.setter
    def parent_node(self, value):
        """Sets the first parent node, if set the first parent node, this entity will be detached from other parent nodes."""
        raise NotImplementedError("parent_node is not implemented")
    
    @property
    def normal(self):
        """The normal of the split plane, the plane is defined as N * P + D = 0 where N is Normal and P is any point on the plane."""
        raise NotImplementedError("normal is not implemented")
    
    @normal.setter
    def normal(self, value):
        """The normal of the split plane, the plane is defined as N * P + D = 0 where N is Normal and P is any point on the plane."""
        raise NotImplementedError("normal is not implemented")
    
    @property
    def position(self):
        """The any point on the split plane, the plane is defined as N * P + D = 0 where N is Normal and P is any point on the plane."""
        raise NotImplementedError("position is not implemented")
    
    @position.setter
    def position(self, value):
        """The any point on the split plane, the plane is defined as N * P + D = 0 where N is Normal and P is any point on the plane."""
        raise NotImplementedError("position is not implemented")
