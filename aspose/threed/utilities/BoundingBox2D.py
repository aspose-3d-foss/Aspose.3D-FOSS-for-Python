class BoundingBox2D:
    """The axis-aligned bounding box for Vector2"""

    def __init__(self, minimum: 'Vector2' = None, maximum: 'Vector2' = None):
        from .Vector2 import Vector2
        from .BoundingBoxExtent import BoundingBoxExtent
        if minimum is None and maximum is None:
            self._minimum = Vector2(0, 0)
            self._maximum = Vector2(0, 0)
            self._extent = BoundingBoxExtent.NULL
        else:
            self._minimum = minimum
            self._maximum = maximum
            from .BoundingBoxExtent import BoundingBoxExtent
            self._extent = BoundingBoxExtent.FINITE

    @property
    def extent(self) -> 'BoundingBoxExtent':
        return self._extent

    @property
    def minimum(self) -> 'Vector2':
        return self._minimum

    @property
    def maximum(self) -> 'Vector2':
        return self._maximum

    def merge(self, pt: 'Vector2'):
        from .BoundingBoxExtent import BoundingBoxExtent
        if self._extent == BoundingBoxExtent.NULL:
            self._minimum = pt
            self._maximum = pt
            self._extent = BoundingBoxExtent.FINITE
        else:
            if pt.x < self._minimum.x:
                self._minimum.x = pt.x
            if pt.y < self._minimum.y:
                self._minimum.y = pt.y
            if pt.x > self._maximum.x:
                self._maximum.x = pt.x
            if pt.y > self._maximum.y:
                self._maximum.y = pt.y

    def merge(self, bb: 'BoundingBox2D'):
        from .BoundingBoxExtent import BoundingBoxExtent
        if bb.extent == BoundingBoxExtent.NULL:
            return
        if self._extent == BoundingBoxExtent.NULL:
            self._minimum = bb.minimum
            self._maximum = bb.maximum
            self._extent = BoundingBoxExtent.FINITE
        else:
            if bb.minimum.x < self._minimum.x:
                self._minimum.x = bb.minimum.x
            if bb.minimum.y < self._minimum.y:
                self._minimum.y = bb.minimum.y
            if bb.maximum.x > self._maximum.x:
                self._maximum.x = bb.maximum.x
            if bb.maximum.y > self._maximum.y:
                self._maximum.y = bb.maximum.y

    @property
    def NULL(self) -> 'BoundingBox2D':
        from .Vector2 import Vector2
        from .BoundingBoxExtent import BoundingBoxExtent
        return BoundingBox2D(Vector2(0, 0), Vector2(0, 0))

    @property
    def INFINITE(self) -> 'BoundingBox2D':
        from .Vector2 import Vector2
        from .BoundingBoxExtent import BoundingBoxExtent
        import math
        return BoundingBox2D(
            Vector2(-math.inf, -math.inf),
            Vector2(math.inf, math.inf)
        )
