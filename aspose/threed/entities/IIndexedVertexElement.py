from typing import List


class IIndexedVertexElement:
    @property
    def indices(self) -> List[int]:
        raise NotImplementedError()
