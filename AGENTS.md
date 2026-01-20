Your job is to implement a python module called org.aspose.threed, this module is used to import and export 3D files, you'll follow user's instruction to implement classes.

The definition of APIs(pyi files) you can find about org.aspose.threed in directory `pyi/aspose/threed`

Each class's pyi definition are defined in directory that's same with its full name, e.g. class `aspose.threed.entities.Mesh` is defined in `pyi/aspose/threed/entities/Mesh.pyi`

You must:

* Use the same interface defined in the pyi files.
* Use the same type hierarchical defined in pyi files.


You must not:
* License related code, this is an open-source module, we don't need licenses
* Importer/Exporter related code, leave them abstract, we'll implement it later.
* Code in module pycore, pydrawing, pyreflection are helpers, we don't need them.
* Implement different API


Directory Structures:

Source files are located in directory `aspose`
Test files are located in directory `tests/`

## Build/Test Commands

Verify Python syntax:
```bash
python3 -m py_compile aspose/threed/<file>.py
```

Run all tests:
```bash
python3 -m unittest discover tests/
```

Run single test file:
```bash
python3 -m unittest tests.test_imports
```

Run single test method:
```bash
python3 -m unittest tests.test_imports.TestClass.test_method
```

Verify module structure:
```bash
python3 tests/verify_module.py
```

## Code Style Guidelines

### File Naming
- All source files use PascalCase: `A3DObject.py`, `Transform.py`, `Matrix4.py`
- All module names use `snake_case`
- Test files use lowercase with underscores: `test_imports.py`

### Imports
- Order: standard library → third-party → local modules
- Use `from typing import TYPE_CHECKING` for circular import prevention
- Forward reference types within TYPE_CHECKING blocks:
```python
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .node import Node
```

### Type Hints
- Use type hints for all method signatures and properties
- Use `Optional[T]` for nullable types
- Return types must match pyi file specifications exactly
- Generic collections: `List[T]`, `Dict[K, V]`, etc.

### Naming Conventions
- Private attributes: `_name`, `_parent_node`, `_entities`
- Public properties: `name`, `parent_node`, `entities`
- Methods: `snake_case` for all method names
- Classes: `PascalCase` for class names
- Constants: `UPPER_SNAKE_CASE` for module-level constants

### Properties
- Use `@property` decorator for getters
- Use `@<property>.setter` decorator for setters
- Properties must match pyi file definitions exactly
- Return copies of mutable collections:
```python
@property
def child_nodes(self) -> List['Node']:
    return list(self._child_nodes)
```

### Method Chaining
- Setters should return `self` for methods where chaining is expected
- Common in Transform class setter methods

### Error Handling
- Abstract methods raise `NotImplementedError` with descriptive message:
```python
def open(self, file_or_stream, options=None):
    raise NotImplementedError("open is not implemented")
```
- Validation errors raise `TypeError` or `ValueError` as appropriate

### Module Exports
- Always define `__all__` in `__init__.py` files
- Export only public API items
- Group related imports:
```python
from .vector2 import Vector2
from .vector3 import Vector3

__all__ = ['Vector2', 'Vector3']
```

### Comments and Documentation
- Do NOT add code comments (no docstrings, no inline comments)
- Keep code self-documenting through clear naming
- PEP 8 formatting is recommended but not enforced

### API Compliance
- All classes must match the interface in corresponding `.pyi` files
- Method names must match exactly (including overloads)
- Property names must match exactly
- Type hints must match pyi specifications
- Constructor signatures must match pyi overloads

### Architecture Rules
- NO license-related code - this is open-source
- NO importer/exporter implementations - leave as abstract (raise NotImplementedError)
- NO animation-related code (unless explicitly requested)
- Follow the exact type hierarchy defined in pyi files
- Base classes extend from correct parent classes
- Use composition for relationships (Node has Entities, not is Entity)

### Testing
- Tests should verify imports work correctly
- Tests should verify basic instantiation
- Tests should verify property access
- Use standard `unittest` framework (pytest is not available)
