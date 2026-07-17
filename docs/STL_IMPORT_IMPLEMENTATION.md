# STL Import/Export Implementation

## Overview
Implemented STL (STereolithography) file format import and export support for both ASCII and binary formats.

## Files Created

### Core Implementation Files

1. **aspose/threed/formats/stl/StlFormat.py**
   - Defines the STL file format
   - Can import and export STL files
   - Provides load and save options

2. **aspose/threed/formats/stl/StlLoadOptions.py**
   - Load options for STL files
   - Properties:
     - `flip_coordinate_system`: bool - Flips Y and Z coordinates
     - `scale`: float - Scales vertex coordinates

3. **aspose/threed/formats/stl/StlSaveOptions.py**
   - Save options for STL files
   - Properties:
     - `flip_coordinate_system`: bool - Flips Y and Z coordinates
     - `scale`: float - Scales vertex coordinates
     - `binary_mode`: bool - Export in binary format (default ASCII)

4. **aspose/threed/formats/stl/StlImporter.py**
   - Implements STL file parsing
   - Supports both ASCII and binary STL formats
   - Creates a single node with a single mesh containing all triangles
   - Reads facet normals from file

5. **aspose/threed/formats/stl/StlExporter.py**
   - Implements STL file writing
   - Supports both ASCII and binary STL formats
   - Triangulates all polygons (triangles, quads, and N-gons)
   - Computes facet normals from triangle geometry

6. **aspose/threed/formats/stl/StlFormatDetector.py**
   - Detects STL format from files and streams
   - Requires .stl extension for reliable detection

7. **aspose/threed/formats/stl/__init__.py**
   - Module initialization
   - Exports all STL classes

### Test Files

8. **tests/test_stl_importer.py**
   - Unit tests for STL importer
   - Tests ASCII and binary parsing
   - Tests coordinate system flipping
   - Tests scaling
   - Tests format properties

9. **tests/test_stl_exporter.py**
   - Unit tests for STL exporter
   - Tests ASCII and binary export
   - Tests quad triangulation
   - Tests coordinate transformations
   - Tests roundtrip (export + import)

10. **tests/test_scene_open_stl.py**
   - Tests Scene.from_file() with STL files
   - Tests Scene.open() with options

11. **tests/test_scene_save_stl.py**
   - Tests Scene.save() to STL files
   - Tests ASCII and binary export
   - Tests roundtrip file operations

## Modified Files

1. **aspose/threed/formats/__init__.py**
   - Added StlLoadOptions and StlSaveOptions exports
   - Added automatic registration of STL importer, exporter, and detector

2. **aspose/threed/FileFormat.py**
   - Updated `get_format_by_extension()` to recognize .stl extension
   - Returns StlFormat for .stl files

3. **aspose/threed/Scene.py**
   - Fixed `open()` method to use `get_format_by_extension()` for file names
   - Fixed `save()` method to properly handle file name-based format detection

## STL Format Support

### ASCII STL Format
- Starts with `solid <name>` keyword
- Each triangle defined with:
  - `facet normal <nx> <ny> <nz>`
  - `outer loop`
  - 3 `vertex <x> <y> <z>` lines
  - `endloop`
  - `endfacet`
- Ends with `endsolid <name>`

### Binary STL Format
- 80 byte header (usually contains model name)
- 4 byte unsigned integer: number of triangles
- Each triangle (50 bytes):
  - 12 floats: normal (3), vertex1 (3), vertex2 (3), vertex3 (3)
  - 2 bytes: attribute count (usually 0)

## Import Features

- ✅ Reads ASCII STL files
- ✅ Reads binary STL files
- ✅ Reads facet normals from file
- ✅ Coordinate system flipping (Y/Z swap)
- ✅ Vertex scaling
- ✅ Automatic format detection from file extension

## Export Features

- ✅ Exports to ASCII STL format
- ✅ Exports to binary STL format
- ✅ Triangulates all polygons:
  - Triangles exported as-is
  - Quads triangulated into 2 triangles
  - N-gons triangulated from first vertex
- ✅ Computes facet normals from triangle geometry
- ✅ Coordinate system flipping (Y/Z swap)
- ✅ Vertex scaling
- ✅ Collects all meshes from scene

## Test Results

All tests pass (39 tests):
- STL Import: 9 tests
- STL Export: 9 tests
- Scene Open: 3 tests
- Scene Save: 4 tests
- All other tests: 14 tests

Example file verification:
- stl_ascii.stl: 2000 polygons, 6000 vertices (import ✓)
- stl_binary.stl: 2000 polygons, 6000 vertices (import ✓)
- Roundtrip ASCII: 2000 polygons, 6000 vertices (export + import ✓)
- Roundtrip Binary: 2000 polygons, 6000 vertices (export + import ✓)

## Scene Structure

Imported/Exported STL files produce:
```
Scene
└── root_node
    └── <mesh_name>  (Node)
        └── Mesh  (Entity)
            ├── 6000 control points
            └── 2000 polygons (triangles)
```

Exactly as specified: one node under root node with a single Mesh instance.

## Usage Examples

### Using Scene.from_file() (Import)
```python
from aspose.threed import Scene

scene = Scene.from_file('model.stl')
# Scene has 1 child node with 1 mesh
```

### Using Scene.open() with options (Import)
```python
from aspose.threed import Scene
from aspose.threed.formats.stl import StlLoadOptions

scene = Scene()
options = StlLoadOptions()
options.scale = 0.5
options.flip_coordinate_system = True

scene.open('model.stl', options)
```

### Using Scene.save() (Export)
```python
from aspose.threed import Scene
from aspose.threed.formats.stl import StlSaveOptions, StlFormat

scene = Scene()

# Export as ASCII
options = StlFormat().create_save_options()
options.binary_mode = False
scene.save('output_ascii.stl', options)

# Export as binary
options = StlFormat().create_save_options()
options.binary_mode = True
scene.save('output_binary.stl', options)
```

### Direct exporter usage (Export)
```python
from aspose.threed import Scene
from aspose.threed.formats.stl import StlExporter, StlSaveOptions, StlFormat

scene = Scene()

exporter = StlExporter()
options = StlFormat().create_save_options()
options.binary_mode = True

with open('output.stl', 'wb') as f:
    exporter.export(scene, f, options)
```

## Notes

1. **Triangulation**: STL only supports triangles, so all polygons are automatically triangulated during export:
   - 3-vertex polygons → 1 triangle
   - 4-vertex polygons → 2 triangles
   - N-vertex polygons → N-2 triangles

2. **Normals**: During export, normals are computed from triangle geometry using cross-product. During import, normals from the file are preserved.

3. **Coordinate System**: The `flip_coordinate_system` option swaps Y and Z coordinates, which is useful when working with different coordinate system conventions.

4. **Binary vs ASCII**: Binary format is more compact but less human-readable. ASCII format is text-based and can be edited manually.

5. **Multiple Meshes**: When exporting, all meshes in the scene are collected and written to a single STL file. When importing, all triangles go into a single mesh.
Scene
└── root_node
    └── <mesh_name>  (Node)
        └── Mesh  (Entity)
            ├── 6000 control points
            └── 2000 polygons (triangles)
```

Exactly as specified: one node under root node with a single Mesh instance.

## Usage Examples

### Using Scene.from_file()
```python
from aspose.threed import Scene

scene = Scene.from_file('model.stl')
# Scene has 1 child node with 1 mesh
```

### Using Scene.open() with options
```python
from aspose.threed import Scene
from aspose.threed.formats.stl import StlLoadOptions

scene = Scene()
options = StlLoadOptions()
options.scale = 0.5
options.flip_coordinate_system = True

scene.open('model.stl', options)
```

### Direct importer usage
```python
from aspose.threed import Scene
from aspose.threed.formats.stl import StlImporter, StlLoadOptions

scene = Scene()
importer = StlImporter()
options = StlLoadOptions()

with open('model.stl', 'rb') as f:
    importer.import_scene(scene, f, options)
```
