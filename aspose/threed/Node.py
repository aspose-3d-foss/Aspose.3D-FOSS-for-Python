from typing import List, Optional, TYPE_CHECKING

from .SceneObject import SceneObject
from .Transform import Transform
from .GlobalTransform import GlobalTransform
from .utilities import BoundingBox
from .utilities.Matrix4 import Matrix4

if TYPE_CHECKING:
    from .Entity import Entity
    from .shading import Material


class Node(SceneObject):
    def __init__(self, name: Optional[str] = None, entity=None):
        super().__init__(name)
        self._parent_node: Optional['Node'] = None
        self._child_nodes: List['Node'] = []
        self._entities: List['Entity'] = []
        self._materials: List['Material'] = []
        self._transform = Transform()
        self._visible = True
        self._excluded = False
        self._asset_info = None
        self._meta_datas = []

        if entity is not None:
            self.add_entity(entity)

    @property
    def parent_node(self) -> Optional['Node']:
        return self._parent_node

    @parent_node.setter
    def parent_node(self, value: Optional['Node']):
        if self._parent_node is not None:
            if self in self._parent_node._child_nodes:
                self._parent_node._child_nodes.remove(self)
            self._parent_node.scene = None

        self._parent_node = value
        if value is not None:
            if self not in value._child_nodes:
                value._child_nodes.append(self)
            if value.scene is not None:
                self._propagate_scene(value.scene)
        else:
            self._propagate_scene(None)

    @property
    def child_nodes(self) -> List['Node']:
        return list(self._child_nodes)

    @property
    def entities(self) -> List['Entity']:
        return list(self._entities)

    @property
    def entity(self) -> Optional['Entity']:
        return self._entities[0] if self._entities else None

    @entity.setter
    def entity(self, value: Optional['Entity']):
        self._entities.clear()
        if value is not None:
            self._entities.append(value)
            if self not in value._parent_nodes:
                value._parent_nodes.append(self)

    @property
    def materials(self) -> List['Material']:
        return list(self._materials)

    @property
    def material(self) -> Optional['Material']:
        return self._materials[0] if self._materials else None

    @material.setter
    def material(self, value: Optional['Material']):
        self._materials.clear()
        if value is not None:
            self._materials.append(value)

    @property
    def transform(self) -> Transform:
        return self._transform

    @property
    def global_transform(self) -> GlobalTransform:
        matrix = self.evaluate_global_transform(True)
        return GlobalTransform(matrix)

    @property
    def visible(self) -> bool:
        return self._visible

    @visible.setter
    def visible(self, value: bool):
        self._visible = bool(value)

    @property
    def excluded(self) -> bool:
        return self._excluded

    @excluded.setter
    def excluded(self, value: bool):
        self._excluded = bool(value)

    @property
    def asset_info(self):
        return self._asset_info

    @asset_info.setter
    def asset_info(self, value):
        self._asset_info = value

    @property
    def meta_datas(self) -> List:
        return list(self._meta_datas)

    def add_entity(self, entity: 'Entity'):
        if entity not in self._entities:
            self._entities.append(entity)
            if self not in entity._parent_nodes:
                entity._parent_nodes.append(self)

    def add_child_node(self, node: 'Node'):
        if node not in self._child_nodes:
            self._child_nodes.append(node)
            node.parent_node = self

    def create_child_node(self, node_name: Optional[str] = None, entity=None,
                     material=None) -> 'Node':
        child = Node(node_name, entity)
        self.add_child_node(child)
        if material is not None:
            child.material = material
        return child

    def get_child(self, index_or_name):
        if isinstance(index_or_name, int):
            if 0 <= index_or_name < len(self._child_nodes):
                return self._child_nodes[index_or_name]
            return None
        else:
            name_str = str(index_or_name)
            for child in self._child_nodes:
                if child.name == name_str:
                    return child
            return None

    def merge(self, node: 'Node'):
        if node is None or node is self:
            return

        children_to_move = list(node._child_nodes)
        for child in children_to_move:
            child.parent_node = self

    def evaluate_global_transform(self, with_geometric_transform: bool) -> Matrix4:
        local_mat = self._transform.transform_matrix

        if self._parent_node is not None:
            parent_mat = self._parent_node.evaluate_global_transform(with_geometric_transform)
            local_mat = parent_mat.concatenate(local_mat)

        return local_mat

    def get_bounding_box(self) -> BoundingBox:
        bbox = BoundingBox.get_null()

        for entity in self._entities:
            try:
                entity_bbox = entity.get_bounding_box()
                bbox.merge(entity_bbox)
            except NotImplementedError:
                pass

        for child in self._child_nodes:
            child_bbox = child.get_bounding_box()
            bbox.merge(child_bbox)

        return bbox

    def select_single_object(self, path: str):
        raise NotImplementedError("select_single_object is not implemented")

    def select_objects(self, path: str):
        raise NotImplementedError("select_objects is not implemented")

    def _propagate_scene(self, scene):
        self.scene = scene
        for child in self._child_nodes:
            child._propagate_scene(scene)
        for entity in self._entities:
            entity.scene = scene

    def __repr__(self) -> str:
        return f"Node({self.name}, children={len(self._child_nodes)}, entities={len(self._entities)})"
