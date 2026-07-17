# Aspose.3D FOSS for Python

A powerful, free, and open-source 3D file format library for Python. Aspose.3D FOSS for Python enables developers to create, manipulate, and convert 3D scenes and models programmatically. It supports popular 3D file formats including OBJ, STL, glTF, 3MF, and more, and is released under the permissive **MIT License**.

> 🏠 **Aspose.3D FOSS** lives on [aspose.org](https://products.aspose.org/3d/python/) — Aspose's home for free, open-source file-format libraries. The full commercial edition, [Aspose.3D for Python via .NET](https://products.aspose.com/3d/python-net/), is available on [aspose.com](https://products.aspose.com/3d).

## About Aspose.3D FOSS

Aspose.3D FOSS is the free, open-source edition of Aspose.3D. It shares the same public API design as the commercial Aspose.3D On-Premise library, so you can:

- **Build and ship 3D applications at no cost** under a permissive MIT License.
- **Start free and grow without rewriting code** — code written against the FOSS edition works with the commercial edition.
- **Upgrade only when you need to** — when you require the broader feature set, higher performance, or proprietary format support of the [commercial On-Premise edition](https://products.aspose.com/3d/python-net/), simply swap in the commercial package, no API rewrites required.

The FOSS edition focuses on the most widely used open 3D formats. The commercial edition additionally covers proprietary and high-performance scenarios such as rendering, advanced mesh operations, and formats like FBX, USD, PDF, and more.

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

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

## Resources

### Aspose.3D FOSS — free & open source (aspose.org)
- [Aspose.3D FOSS for Python](https://products.aspose.org/3d/python/) — product page
- [Aspose.3D FOSS family](https://products.aspose.org/3d/) — all platforms (Python, .NET, Java, TypeScript)
- [Aspose FOSS documentation](https://docs.aspose.org/) — guides for all open-source libraries
- [Aspose FOSS blog](https://blog.aspose.org/) — tutorials and announcements

### Aspose.3D — commercial On-Premise edition (aspose.com)
- [Aspose.3D for Python via .NET](https://products.aspose.com/3d/python-net/) — full-featured commercial edition
- [Aspose.3D product family](https://products.aspose.com/3d) — overview
- [Developer documentation](https://docs.aspose.com/3d/python-net/) — API guides
- [API reference](https://reference.aspose.com/3d/python-net/) — complete API documentation
- [Download / free trial](https://downloads.aspose.com/3d) — get the commercial package

### Community & support
- [Aspose.3D support forum](https://forum.aspose.com/c/3d/19) — questions and help
- [Free online 3D apps](https://products.aspose.app/3d/) — convert and view 3D files in your browser

## Acknowledgments

- Aspose.3D FOSS is inspired by the Aspose.3D API.
- 3D format specifications are maintained by various 3D software vendors and standards bodies.
