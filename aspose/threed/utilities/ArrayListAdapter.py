from typing import List, Generic, TypeVar, Iterator

T = TypeVar('T')


class ArrayListAdapter(Generic[T]):
    """Adapter class that wraps List[T] and implements IList[T] compatible interface."""

    def __init__(self, data: List[T]):
        """Initialize ArrayListAdapter with a list."""
        if data is None:
            raise ValueError("data cannot be None")
        self._data = data

    def __getitem__(self, index: int) -> T:
        """Get item at index."""
        return self._data[index]

    def __setitem__(self, index: int, value: T):
        """Set item at index."""
        self._data[index] = value

    def __len__(self) -> int:
        """Get the number of items."""
        return len(self._data)

    def __iter__(self) -> Iterator[T]:
        """Iterate over items."""
        return iter(self._data)

    def add(self, item: T):
        """Add an item to the list."""
        self._data.append(item)

    def clear(self):
        """Clear all items."""
        self._data.clear()

    def contains(self, item: T) -> bool:
        """Check if item exists in list."""
        return item in self._data

    def copy_to(self, array: list, array_index: int = 0):
        """Copy items to an array."""
        for i, item in enumerate(self._data):
            if i + array_index >= len(array):
                break
            array[array_index + i] = item

    def remove(self, item: T) -> bool:
        """Remove an item. Returns True if successful."""
        if item in self._data:
            self._data.remove(item)
            return True
        return False

    def index_of(self, item: T) -> int:
        """Get index of item. Returns -1 if not found."""
        try:
            return self._data.index(item)
        except ValueError:
            return -1

    def insert(self, index: int, item: T):
        """Insert item at index."""
        self._data.insert(index, item)

    def remove_at(self, index: int):
        """Remove item at index."""
        del self._data[index]

    def to_array(self) -> List[T]:
        """Convert to list."""
        return list(self._data)

    def add_range(self, items: List[T]):
        """Add multiple items."""
        self._data.extend(items)
