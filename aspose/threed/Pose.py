from aspose.threed import A3DObject, INamedObject
from aspose.threed import Node
from aspose.threed.utilities import Matrix4
from aspose.threed.PoseType import PoseType
from aspose.threed.BonePose import BonePose


class Pose(A3DObject, INamedObject):
    def __init__(self, name: str = None):
        super().__init__(name)
        self._pose_type = PoseType.BIND_POSE
        self._bone_poses = []

    @property
    def pose_type(self) -> PoseType:
        return self._pose_type

    @pose_type.setter
    def pose_type(self, value: PoseType):
        self._pose_type = value

    @property
    def bone_poses(self):
        return self._bone_poses

    def add_bone_pose(self, node: Node, matrix: Matrix4, local_matrix: bool = False):
        bone_pose = BonePose()
        bone_pose.node = node
        bone_pose.matrix = matrix
        bone_pose.is_local = local_matrix
        self._bone_poses.append(bone_pose)
