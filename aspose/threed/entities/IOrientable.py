from aspose.threed import Entity


class IOrientable(Entity):
    """Orientable entities shall implement this interface."""
    
    @property
    def direction(self):
        """Gets the direction that the entity is looking at."""
        raise NotImplementedError("direction is not implemented")
    
    @direction.setter
    def direction(self, value):
        """Sets the direction that the entity is looking at."""
        raise NotImplementedError("direction is not implemented")
    
    @property
    def target(self):
        """Gets the target that the entity is looking at."""
        raise NotImplementedError("target is not implemented")
    
    @target.setter
    def target(self, value):
        """Sets the target that the entity is looking at."""
        raise NotImplementedError("target is not implemented")
