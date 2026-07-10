from typing import List, TypeVar, Generic, Iterable, Iterator

T = TypeVar('T')


class ArrayListAdapter(Generic[T]):
    """Adapter class that wraps List[T] and implements IArrayList[T]."""
    
    def __init__(self, data: List[T] = None):
        if data is None:
            data = []
        self._data = data
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __setitem__(self, index, value):
        self._data[index] = value
    
    def __len__(self):
        return len(self._data)
    
    def __iter__(self) -> Iterator[T]:
        return iter(self._data)
    
    def __contains__(self, item):
        return item in self._data
    
    def __repr__(self):
        return f"ArrayListAdapter({self._data!r})"
    
    def add(self, item: T):
        self._data.append(item)
    
    def append(self, item: T):
        self._data.append(item)
    
    def clear(self):
        self._data.clear()
    
    def remove(self, item: T) -> bool:
        try:
            self._data.remove(item)
            return True
        except ValueError:
            return False
    
    def insert(self, index: int, item: T):
        self._data.insert(index, item)
    
    def remove_at(self, index: int):
        del self._data[index]
    
    def index_of(self, item: T) -> int:
        try:
            return self._data.index(item)
        except ValueError:
            return -1
    
    def to_array(self) -> List[T]:
        return list(self._data)
    
    def add_range(self, collection):
        if collection is None:
            raise ValueError("collection cannot be None")
        self._data.extend(collection)
    
    def __add__(self, other):
        return self._data + other
    
    def __mul__(self, other):
        return self._data * other
    
    def __rmul__(self, other):
        return other * self._data
