# Aspose.3D FOSS for Python

A powerful and open-source 3D file format library for Python. Aspose.3D for Python enables developers to create, manipulate, and convert 3D scenes and models programmatically. Supports popular 3D file formats including OBJ, STL, FBX, GLTF, and more.

## Features

- **OBJ Format Support**
  - Import OBJ files with vertices, normals, and texture coordinates
  - Multiple objects and grouping
  - Material loading from MTL files
  - Smoothing groups
  - Configurable coordinate system flipping and scaling
  
- **Scene Management**
  - Create and manipulate 3D scenes
  - Hierarchical node structure
  - Mesh and entity management
  - Material system with Lambert and Phong shading

- **3D Primitives**
  - Vector math (Vector2, Vector3, Vector4, Matrix4, Quaternion)
  - Bounding boxes and transformations
  - Camera and light objects

## Installation

```bash
pip install aspose-3d-foss
```

## Quick Start

```python
from aspose.threed import Scene
from aspose.threed.formats.obj import ObjLoadOptions

# Create a new scene
scene = Scene()

# Import an OBJ file
options = ObjLoadOptions()
options.enable_materials = True
options.flip_coordinate_system = False
scene.open("model.obj", options)

# Access imported data
for node in scene.root_node.child_nodes:
    if node.entity:
        mesh = node.entity
        print(f"Mesh: {node.name}")
        print(f"  Vertices: {len(mesh.control_points)}")
        print(f"  Polygons: {mesh.polygon_count}")
```

## Supported Formats

### Import (Implemented)
- **OBJ** - Wavefront OBJ with full material support
- More formats coming soon...

### Export (Partial)
- **OBJ** - Basic OBJ export (vertices, faces, materials)
- More formats coming soon...

## Examples

See the [examples/](examples/) directory for sample OBJ files and usage examples.

## Documentation

- [API Reference](https://reference.aspose.com/3d/python/) - Complete API documentation
- [Examples](examples/) - Example files and usage

## Python Version Support

- Python 3.7+
- Python 3.8+
- Python 3.9+
- Python 3.10+
- Python 3.11+
- Python 3.12+

## Format-Specific Features

### OBJ Format

**Import Features:**
- Vertices (v)
- Texture coordinates (vt)
- Vertex normals (vn)
- Faces (f) with multiple index formats
- Objects (o)
- Groups (g)
- Materials (usemtl, mtllib)
- Smoothing groups (s)

**Load Options:**
- `flip_coordinate_system` - Swap Y and Z coordinates
- `enable_materials` - Enable/disable material loading
- `scale` - Scale factor for all coordinates
- `normalize_normal` - Normalize normal vectors

**Save Options:**
- `apply_unit_scale` - Apply unit scaling
- `point_cloud` - Export as point cloud
- `verbose` - Verbose output
- `serialize_w` - Include W coordinate
- `enable_materials` - Export materials
- `flip_coordinate_system` - Flip coordinate system

## Architecture

The library is organized into several modules:

- `aspose.threed` - Core scene classes (Scene, Node, Entity)
- `aspose.threed.entities` - 3D entities (Mesh, Camera, Light)
- `aspose.threed.formats` - File format importers and exporters
- `aspose.threed.shading` - Material system
- `aspose.threed.utilities` - Math utilities (vectors, matrices, quaternions)

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Aspose.3D for Python is inspired by the original Aspose.3D API
- OBJ format specification maintained by various 3D software vendors
