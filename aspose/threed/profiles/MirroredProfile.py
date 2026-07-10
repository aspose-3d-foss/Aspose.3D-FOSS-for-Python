from typing import TYPE_CHECKING

from .Profile import Profile

if TYPE_CHECKING:
    from .ParameterizedProfile import ParameterizedProfile


class MirroredProfile(Profile):
    """IFC compatible mirror profile.
    This profile defines a new profile by mirroring the base profile about the y axis."""
    
    def __init__(self, base_profile: Profile = None):
        super().__init__(None)
        self._base_profile = base_profile
    
    @property
    def base_profile(self) -> Profile:
        return self._base_profile
    
    @base_profile.setter
    def base_profile(self, value: Profile):
        self._base_profile = value
