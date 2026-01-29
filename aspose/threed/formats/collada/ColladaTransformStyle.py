from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class ColladaTransformStyle:
    _components_instance = None
    _matrix_instance = None

    def __new__(cls, name=None):
        if name == 'COMPONENTS':
            if cls._components_instance is None:
                cls._components_instance = super().__new__(cls)
                cls._components_instance._name = 'COMPONENTS'
            return cls._components_instance
        elif name == 'MATRIX':
            if cls._matrix_instance is None:
                cls._matrix_instance = super().__new__(cls)
                cls._matrix_instance._name = 'MATRIX'
            return cls._matrix_instance
        else:
            return super().__new__(cls)

    @property
    def name(self) -> str:
        return getattr(self, '_name', '')

    @staticmethod
    def COMPONENTS():
        if ColladaTransformStyle._components_instance is None:
            ColladaTransformStyle._components_instance = ColladaTransformStyle('COMPONENTS')
        return ColladaTransformStyle._components_instance

    @staticmethod
    def MATRIX():
        if ColladaTransformStyle._matrix_instance is None:
            ColladaTransformStyle._matrix_instance = ColladaTransformStyle('MATRIX')
        return ColladaTransformStyle._matrix_instance

    def __repr__(self):
        return f'ColladaTransformStyle.{self.name}'
