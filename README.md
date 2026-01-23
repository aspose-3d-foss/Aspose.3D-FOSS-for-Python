# Aspose.3D FOSS for Python

A powerful and open-source 3D file format library for Python. Aspose.3D for Python enables developers to create, manipulate, and convert 3D scenes and models programmatically. Supports popular 3D file formats including OBJ, STL, FBX, GLTF, and more.

## Features

- **Format Support**
  - OBJ - Import/export with materials, textures, and grouping
  - GLTF - GL Transmission Format with full PBR material support
  - STL - Stereo Lithography format for 3D printing
  - 3MF - 3D Manufacturing Format for modern 3D printing workflows

- **Scene Management**
  - Create and manipulate 3D scenes
  - Hierarchical node structure
  - Mesh and entity management
  - Material system with Lambert, Phong, and PBR materials

- **3D Primitives**
  - Vector math (Vector2, Vector3, Vector4, Matrix4, Quaternion)
  - Bounding boxes and transformations
  - Camera and light objects

- **Mesh Operations**
  - Triangulation support for polygon conversion
  - Mesh manipulation and modification

- **Animation System**
  - Keyframe animation support
  - Animation curves and interpolation

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
- **GLTF** - GL Transmission Format (glTF 2.0)
- **STL** - Stereo Lithography format
- **3MF** - 3D Manufacturing Format
- More formats coming soon...

### Export (Implemented)
- **OBJ** - Export with vertices, faces, and materials
- **GLTF** - Export to glTF 2.0 format
- **STL** - Export to STL format
- **3MF** - Export to 3MF format
- More formats coming soon...

## Documentation

- [API Reference](https://reference.aspose.com/3d/python-net/) - Complete API documentation

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
- Vertices (v), texture coordinates (vt), vertex normals (vn)
- Faces (f) with multiple index formats
- Objects (o), groups (g), smoothing groups (s)
- Materials (usemtl, mtllib)

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

### GLTF Format

**Features:**
- glTF 2.0 specification support
- PBR material system (metallic/roughness workflow)
- Mesh primitives with attributes
- Node hierarchy and transforms
- Texture and image support

### STL Format

**Features:**
- Binary and ASCII STL support
- Triangular mesh representation
- Unit conversion and scaling
- Import for 3D printing workflows

### 3MF Format

**Features:**
- 3D Manufacturing Format 1.2 support
- Rich metadata support
- Production-grade 3D printing
- Color and material support

## Architecture

The library is organized into several modules:

- `aspose.threed` - Core scene classes (Scene, Node, Entity)
- `aspose.threed.entities` - 3D entities (Mesh, Camera, Light)
- `aspose.threed.formats` - File format importers and exporters (OBJ, GLTF, STL, 3MF)
- `aspose.threed.shading` - Material system (Lambert, Phong, PBR materials)
- `aspose.threed.utilities` - Math utilities (vectors, matrices, quaternions)
- `aspose.threed.animation` - Animation system (keyframes, curves)

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Aspose.3D for Python is inspired by the original Aspose.3D API
- 3D format specification maintained by various 3D software vendors
