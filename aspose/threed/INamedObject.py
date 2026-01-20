class INamedObject:
    @property
    def name(self) -> str:
        raise NotImplementedError()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"
