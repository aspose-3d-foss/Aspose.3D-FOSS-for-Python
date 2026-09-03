# Aspose.3D FOSS for Python

[![Python versions](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Contributors](https://img.shields.io/github/contributors/aspose-3d-foss/Aspose.3D-FOSS-for-Python.svg)](https://github.com/aspose-3d-foss/Aspose.3D-FOSS-for-Python/graphs/contributors) [![PyPI version](https://img.shields.io/pypi/v/aspose-3d-foss.svg)](https://pypi.org/project/aspose-3d-foss/)

[![Aspose.3D FOSS for Python](https://products.aspose.org/media/3d/python/banner-readme.png)](https://products.aspose.org/3d/python/)

Aspose.3D FOSS for Python is a pure-Python, MIT-licensed library for loading, constructing,
and exporting 3D scenes. It reads and writes OBJ, STL, glTF/GLB, COLLADA, and 3MF files, plus
imports FBX, through a `Scene`/`Node`/`Mesh` object graph, with no native runtime or external
SDK to install.

## Navigation

- [At a Glance](#at-a-glance)
- [Key Capabilities](#key-capabilities)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Quick Start](#quick-start)
- [Additional Examples](#additional-examples)
- [API Reference](#api-reference)
- [Documentation & Resources](#documentation--resources)
- [Scope and Limitations](#scope-and-limitations)
- [Development and Testing](#development-and-testing)
- [License](#license)

## At a Glance

```mermaid
flowchart TD
  subgraph StartingPoints["Starting Points"]
    direction LR
    i1["An existing OBJ, STL, glTF, COLLADA, or 3MF file"]
  end
  PRODUCT["Aspose.3D FOSS for Python"]
  subgraph Capabilities["Core Capabilities"]
    direction LR
    subgraph capl[" "]
      direction TB
      c1["Multi-format scene import (OBJ, STL, glTF, COLLADA, 3MF)"]
      c2["Multi-format scene export (OBJ, STL, glTF, 3MF)"]
      c3["Scene-graph construction and traversal"]
      c4["Mesh authoring and editing"]
    end
    subgraph capr[" "]
      direction TB
      c5["Parameterized primitive geometry"]
      c6["Lambert, Phong, and PBR material assignment"]
      c7["Polygon triangulation"]
      c8["Keyframe animation and skeletal pose data"]
    end
  end
  subgraph Outputs["Outputs"]
    direction TB
    o1["OBJ, STL, glTF, or 3MF file"]
  end
  StartingPoints --> PRODUCT --> Capabilities --> Outputs
```

## Key Capabilities

- Read OBJ, STL, glTF/GLB, COLLADA, and 3MF (the 3D Manufacturing Format used in 3D-printing
  workflows) files with `Scene.open()`, which auto-detects the format from the file extension
  or an explicit `FileFormat`.
- Write scenes back out to OBJ, STL, glTF/GLB, or 3MF with `Scene.save()`, each format backed
  by its own `SaveOptions` subclass (`ObjSaveOptions`, `GltfSaveOptions`, and so on) for
  coordinate flipping, unit scaling, and compression settings (COLLADA export is registered
  but not reachable through `Scene.save()` — see Scope and Limitations).
- Build and traverse a scene graph with `Node.create_child_node()`, `Node.add_entity()`, and
  `Node.child_nodes`; every node carries its own `Transform` (translation, rotation, scale, and
  pivots) independent of whatever entity or material is attached to it.
- Author and edit mesh data directly through `Mesh.control_points`, `Mesh.create_polygon()`, and
  `Mesh.polygons`, or convert an existing mesh with `PolygonModifier.triangulate()`.
- Construct parameterized primitives — `Box`, `Sphere`, `Cylinder`, `Torus`, `Dish`, `Pyramid`,
  and more — and call their own `to_mesh()` to turn them into editable `Mesh` geometry.
- Assign `LambertMaterial`, `PhongMaterial`, or `PbrMaterial` to a node, setting diffuse,
  specular, emissive, and PBR albedo/metallic/roughness color and factor properties directly.
- Triangulate arbitrary polygon data into triangle fans with `PolygonModifier.triangulate()`,
  a real ear-clipping triangulation implementation rather than a naive fan split.
- Build keyframe animation with `AnimationClip`, `AnimationNode`, and `KeyframeSequence`, and
  store skeletal bind-pose data with `Skeleton`, `Bone`, and `Pose`.

## Installation

Install the published package from PyPI (`aspose-3d-foss`, version 26.1.0):

```bash
python3 -m pip install aspose-3d-foss
```

To work from the latest source checkout instead, install it in editable mode:

```bash
git clone https://github.com/aspose-3d-foss/Aspose.3D-FOSS-for-Python.git
cd Aspose.3D-FOSS-for-Python
python3 -m pip install -e .
```

Verify the install:

```bash
python3 -c "from aspose.threed import Scene; print('Aspose.3D FOSS OK')"
```

The package supports Python 3.7, 3.8, 3.9, 3.10, 3.11, and 3.12 on Windows, macOS, and Linux,
with no native dependencies.

## Dependencies

### Required Package Dependencies

No required third-party package dependencies. `setup.py`'s `install_requires` list is empty.

### Native and System Requirements

- Requires Python 3.7 or later (`python_requires=">=3.7"` in `setup.py`).

### Development Dependencies

- `pytest` `>=7.0.0` — test runner installed via the optional `dev` extra
  (`pip install -e ".[dev]"`); the bundled test suite itself is written against the
  standard-library `unittest` framework (see
  [Development and Testing](#development-and-testing)).

## Quick Start

Import an OBJ file and inspect its geometry:

```python
from aspose.threed import Scene
from aspose.threed.formats.obj import ObjLoadOptions

scene = Scene()
options = ObjLoadOptions()
options.enable_materials = True
scene.open("model.obj", options)

for node in scene.root_node.child_nodes:
    if node.entity is not None:
        mesh = node.entity
        print(f"{node.name}: {len(mesh.control_points)} vertices, {mesh.polygon_count} polygons")
```

Build a scene from scratch and export it to glTF:

```python
from aspose.threed import Scene
from aspose.threed.entities import Box
from aspose.threed.shading import LambertMaterial
from aspose.threed.utilities import Vector3

scene = Scene()
box = Box(length=2.0, width=1.0, height=1.0)
material = LambertMaterial()
material.diffuse_color = Vector3(0.2, 0.6, 0.9)

scene.root_node.create_child_node("Crate", entity=box.to_mesh(), material=material)
scene.save("crate.gltf")
```

## Additional Examples

More real, verified snippets are collected below, each demonstrating one operation without
obscuring the primary installation and quick-start path.

### Convert Between Formats

```python
from aspose.threed import Scene

scene = Scene()
scene.open("model.obj")
scene.save("model.glb")
```

<details>
<summary>View Additional Examples</summary>

### Assign a PBR Material to a Primitive

```python
from aspose.threed import Scene
from aspose.threed.entities import Sphere
from aspose.threed.shading import PbrMaterial
from aspose.threed.utilities import Vector3

scene = Scene()
sphere = Sphere()
material = PbrMaterial(albedo=Vector3(0.8, 0.1, 0.1))
material.metallic_factor = 0.9
material.roughness_factor = 0.2

scene.root_node.create_child_node("Ball", entity=sphere.to_mesh(), material=material)
scene.save("ball.stl")
```

### Build a Mesh From Control Points and Export It to glTF

Construct a mesh vertex by vertex, attach a PBR material, write the scene to an in-memory glTF
stream, and read the exported material back out of the glTF JSON:

```python
import io
import json
from aspose.threed import Scene, FileFormat
from aspose.threed.entities import Mesh
from aspose.threed.utilities import Vector3, Vector4
from aspose.threed.formats.gltf import GltfSaveOptions
from aspose.threed.shading import PbrMaterial

scene = Scene()
mesh = Mesh("TestMesh")
mesh.control_points.add(Vector4(0.0, 0.0, 0.0, 1.0))
mesh.control_points.add(Vector4(1.0, 0.0, 0.0, 1.0))
mesh.control_points.add(Vector4(0.0, 1.0, 0.0, 1.0))
mesh.create_polygon(0, 1, 2)

albedo = Vector3(0.8, 0.2, 0.3)
material = PbrMaterial("RedMaterial", albedo)
material.metallic_factor = 0.5
material.roughness_factor = 0.7

node = scene.root_node.create_child_node("TestNode")
node.entity = mesh
node.material = material

stream = io.BytesIO()
# Pass the detected FileFormat into the constructor explicitly: unlike
# StlFormat, GltfFormat.create_save_options() does not set file_format on the
# options it returns, and a bare stream (no filename) gives scene.save()
# nothing else to detect the format from.
options = GltfSaveOptions(FileFormat.get_format_by_extension(".gltf"))
options.binary_mode = False
scene.save(stream, options)

stream.seek(0)
gltf_data = json.loads(stream.read().decode("utf-8"))
print(gltf_data["materials"][0]["pbrMetallicRoughness"])
```

### Triangulate an Imported Mesh

```python
from aspose.threed import Scene
from aspose.threed.entities import PolygonModifier

scene = Scene()
scene.open("model.obj")

for node in scene.root_node.child_nodes:
    if node.entity is not None:
        triangulated = PolygonModifier.triangulate(node.entity)
        if triangulated is not None:
            node.entity = triangulated
```

### Walk the Scene Graph

```python
from aspose.threed import Scene

scene = Scene()
scene.open("model.gltf")

def walk(node, depth=0):
    print("  " * depth + (node.name or "(unnamed)"))
    for child in node.child_nodes:
        walk(child, depth + 1)

walk(scene.root_node)
```

### Position a Node With Transform

```python
from aspose.threed import Scene
from aspose.threed.entities import Cylinder
from aspose.threed.utilities import Vector3

scene = Scene()
cylinder = Cylinder()
node = scene.root_node.create_child_node("Post", entity=cylinder.to_mesh())
node.transform.translation = Vector3(0.0, 1.0, 0.0)
node.transform.scaling = Vector3(0.5, 2.0, 0.5)

scene.save("post.obj")
```

### Build a Mesh and Export It to STL

```python
import io
from aspose.threed import Scene, FileFormat
from aspose.threed.entities import Mesh
from aspose.threed.utilities import Vector4

scene = Scene()
mesh = Mesh("triangle")
mesh.control_points.add(Vector4(0.0, 0.0, 0.0, 1.0))
mesh.control_points.add(Vector4(1.0, 0.0, 0.0, 1.0))
mesh.control_points.add(Vector4(1.0, 1.0, 0.0, 1.0))
mesh.create_polygon(0, 1, 2)

node = scene.root_node.create_child_node("triangle_node")
node.entity = mesh

stream = io.StringIO()
# Use FileFormat.get_format_by_extension(...).create_save_options() rather than
# StlSaveOptions() directly: a default-constructed options object has no
# file_format set, and scene.save() cannot infer the format from a bare stream
# (only filename-based saves fall back to extension detection).
options = FileFormat.get_format_by_extension(".stl").create_save_options()
options.binary_mode = False
scene.save(stream, options)
print(stream.getvalue())
```

### Convert a Parametric Primitive to a Mesh

```python
from aspose.threed.entities import Box

box = Box(10, 20, 30)
mesh = box.to_mesh()
print(f"Control points: {len(mesh.control_points)}")
```

### Import a COLLADA File

```python
from aspose.threed import Scene
from aspose.threed.formats.collada.ColladaLoadOptions import ColladaLoadOptions

scene = Scene()
options = ColladaLoadOptions()
scene.open("model.dae", options)

print(f"Child nodes: {len(scene.root_node.child_nodes)}")
```

### Build a Cube and Export It to 3MF

```python
import io
from aspose.threed import Scene
from aspose.threed.entities import Mesh
from aspose.threed.utilities import Vector4
from aspose.threed.formats import ThreeMfSaveOptions

scene = Scene()
mesh = Mesh("cube")
for point in [
    Vector4(0, 0, 0, 1), Vector4(1, 0, 0, 1), Vector4(1, 1, 0, 1), Vector4(0, 1, 0, 1),
    Vector4(0, 0, 1, 1), Vector4(1, 0, 1, 1), Vector4(1, 1, 1, 1), Vector4(0, 1, 1, 1),
]:
    mesh.control_points.add(point)

mesh.create_polygon(0, 1, 2)
mesh.create_polygon(0, 2, 3)
mesh.create_polygon(4, 7, 6)
mesh.create_polygon(4, 6, 5)
mesh.create_polygon(0, 4, 5)
mesh.create_polygon(0, 5, 1)
mesh.create_polygon(2, 6, 7)
mesh.create_polygon(2, 7, 3)
mesh.create_polygon(0, 3, 7)
mesh.create_polygon(0, 7, 4)
mesh.create_polygon(1, 5, 6)
mesh.create_polygon(1, 6, 2)

node = scene.root_node.create_child_node("cube")
node.entity = mesh

stream = io.BytesIO()
options = ThreeMfSaveOptions()
options.enable_compression = False
scene.save(stream, options)
```

</details>

## API Reference

`Scene` is the primary entry point: `Scene.open()`/`Scene.save()` load and write a scene graph
built from `Node` objects, each of which holds a `Transform`, an optional `Mesh`-derived
`Entity`, and zero or more `Material` instances. The full public class index is listed below by
module.

<details>
<summary>View the Supported Public API Surface</summary>

### Core API

| Class | Description |
|---|---|
| `A3DObject` | A3DObject.find_property returns the property object matching the given name if it exists. |
| `A3dwSaveOptions` | Save options for A3DW. |
| `AlphaSource` | Source of alpha channel for textures. |
| `AmfSaveOptions` | Save options for AMF. |
| `AnimationChannel` | AnimationChannel.component_type specifies the data type of the animated component. |
| `AnimationClip` | AnimationClip.create_animation_node creates a new AnimationNode for the given node name. |
| `AnimationNode` | AnimationNode.find_bind_point returns the BindPoint matching the given target object and name. |
| `ApertureMode` | Camera aperture modes. |
| `ArbitraryProfile` | This class allows you to construct a 2D profile directly from arbitrary curve. |
| `ArrayListAdapter` | Adapter class that wraps List[T] and implements IArrayList[T]. |
| `AssetInfo` | AssetInfo.title stores the title of the 3D asset. |
| `Axis` | The coordinate axis. |
| `AxisSystem` | Axis system is an combination of coordinate system, up vector and front vector. |
| `BasicLoadOptions` | Simple LoadOptions subclass for basic loading options. |
| `BinaryTokenizer` | BinaryTokenizer.tokenize() parses the binary data stream and advances the cursor accordingly. |
| `BindPoint` | BindPoint.add_channel adds a new animation channel with the specified name, value and type, returning True on success. |
| `BlendFactor` | Blend factor specify pixel arithmetic. |
| `Bone` | Bone objects expose weight management via get_weight and set_weight methods, enabling skinning calculations. |
| `BoneLinkMode` | Enum with 3 members: `NORMALIZE`, `ADDITIVE`, `TOTAL_ONE`, describing how a bone's skinning weight is combined with others on the same vertex. |
| `BonePose` | Records one bone's world and local transform matrices inside a `Pose`, added via `Pose.add_bone_pose()`. |
| `BooleanOperand` | This class encapsulates the transformed mesh as Boolean operation's operand. |
| `BooleanOperation` | BooleanOperation.ADD represents a union boolean operation that adds geometry. |
| `BooleanOperator` | Boolean operator allows you to apply Boolean operation on two IMeshConvertible instances. |
| `BoundingBox` | BoundingBox.merge() can combine multiple bounding boxes or geometry to expand the box to include all elements. |
| `BoundingBox2D` | The axis-aligned bounding box for Vector2. |
| `BoundingBoxExtent` | The extent of the bounding box. |
| `Box` | Box.to_mesh() converts the parameterized box primitive into a Mesh for further processing. |
| `CShape` | IFC compatible C-shape profile that defined by parameters. |
| `Camera` | Camera properties near_plane and far_plane define the depth range for the view frustum calculations. |
| `CenterLineProfile` | IFC compatible center line profile. |
| `Circle` | Circle.to_mesh() converts the parameterized circle primitive into a Mesh for further processing. |
| `CircleShape` | IFC compatible circle profile. |
| `ColladaExporter` | ColladaExporter.supports_format returns true if the exporter can handle the given file format. |
| `ColladaFormat` | ColladaFormat.create_load_options creates and returns a Collada load options object for importing. |
| `ColladaFormatDetector` | ColladaFormatDetector.detect determines the 3D file format of a stream, optionally using the file name. |
| `ColladaImporter` | ColladaImporter.supports_format returns True if the specified file format is supported by this importer. |
| `ColladaLoadOptions` | ColladaLoadOptions.flip_coordinate_system determines whether the Y and Z axes are swapped during import. |
| `ColladaPlugin` | ColladaPlugin supplies factory methods to obtain the ColladaFormat, its importer, exporter, and format detector for seamless integration. |
| `ColladaSaveOptions` | ColladaSaveOptions.flip_coordinate_system determines whether the Y and Z axes are swapped when saving. |
| `ColladaTransformStyle` | The node's transformation style of node. |
| `CompareFunction` | Compare function for depth/stencil testing. |
| `ComposeOrder` | The order to compose transform matrix. |
| `CompositeCurve` | A CompositeCurve is consisting of several curve segments. |
| `CoordinateSystem` | The left handed or right handed coordinate system. |
| `CubeFace` | Cube face enumeration. |
| `CullFaceMode` | Cull face mode for face culling. |
| `Curve` | Base class for curve entities, extended by `CompositeCurve`, `NurbsCurve`, `TrimmedCurve`, and `TransformedCurve`. |
| `CurveDimension` | Enum with 2 members, `TWO_DIMENSIONAL` and `THREE_DIMENSIONAL`, describing a curve's coordinate space. |
| `CustomObject` | Stores arbitrary user-defined data as a named `A3DObject`-derived scene object. |
| `Cylinder` | Cylinder.to_mesh() converts the cylinder primitive into a Mesh object for further processing. |
| `Deformer` | Base class for mesh deformers, extended by `SkinDeformer` and `MorphTargetDeformer`. |
| `DescriptorSetUpdater` | Descriptor set updater for shader resources. |
| `Discreet3dsLoadOptions` | Load options for Discreet 3DS. |
| `Discreet3dsSaveOptions` | Save options for Discreet 3DS. |
| `Dish` | Dish.to_mesh() creates a Mesh from a dish primitive, and its radius and height properties control its size. |
| `DracoCompressionLevel` | Compression level for draco file. |
| `DracoFormat` | Google Draco format. |
| `DracoSaveOptions` | Save options for Draco. |
| `DrawOperation` | Draw operation type. |
| `DriverException` | Exception thrown when rendering driver fails. |
| `Ellipse` | Ellipse.to_mesh() converts an ellipse primitive into a Mesh object that can be added to a scene. |
| `EllipseShape` | IFC compatible ellipse profile. |
| `EndPoint` | The end point to trim the curve, can be a parameter value or a Cartesian point. |
| `Entity` | Entity objects expose get_bounding_box() for spatial queries and a full set of property‑management methods (find_property, get_property, set_property, remove_property). |
| `EntityRenderer` | Base class for rendering entities. |
| `EntityRendererFeatures` | Features supported by an entity renderer. |
| `EntityRendererKey` | The key of registered entity renderer. |
| `ExportException` | Exceptions when Aspose.3D failed to export the scene to file. |
| `Exporter` | Exporter objects let you verify format support with supports_format() before calling export() to write a scene to a stream. |
| `Extrapolation` | Extrapolation.type represents the extrapolation mode applied to animation curves. |
| `FMatrix4` | Matrix 4x4 with all component in float type. |
| `FVector2` | FVector2.normalize returns a new FVector2 with the same direction and unit length. |
| `FVector3` | FVector3.zero returns a vector with all components set to 0. |
| `FVector4` | FVector4.x represents the X component of the 4‑dimensional vector. |
| `FbxElement` | FbxElement.add_token adds the given token to the element's token collection. |
| `FbxExporter` | FbxExporter.save saves the given Scene to a file path using specified FbxSaveOptions. |
| `FbxFormat` | FbxFormat.detect(stream, file_name) returns the detected file format, enabling dynamic handling of unknown input files. |
| `FbxFormatDetector` | FbxFormatDetector.detect determines the FBX format of the provided stream, optionally using the file name. |
| `FbxImporter` | FbxImporter.supports_format returns True if the given file format is supported for import. |
| `FbxLoadOptions` | FbxLoadOptions exposes properties such as keep_builtin_global_settings, compatible_mode, file_format, encoding, file_system, lookup_paths, and file_name to customize FBX import behavior. |
| `FbxParser` | FbxParser.parse_value parses the provided token and returns its evaluated value. |
| `FbxPlugin` | FbxPlugin.get_file_format returns the identifier or name of the FBX file format handled by the plugin. |
| `FbxSaveOptions` | FbxSaveOptions provides export_textures, embed_textures, export_legacy_material_properties, and other flags to control how FBX files are written. |
| `FbxScope` | FbxScope.add_element(element) adds a new element to the scope, and get_elements(key) retrieves all elements of the specified type. |
| `FbxTokenizer` | FbxTokenizer.tokenize() returns a list of internal lexical-token objects representing the elements of an FBX file. |
| `FileContentType` | File content type. |
| `FileFormat` | Class with 9 methods and 8 properties and 49 members. |
| `FileFormatType` | File format type. |
| `FileSystem` | File system encapsulation. |
| `FontFile` | Font file contains definitions for glyphs, this is used to create text profile. |
| `FormatDetector` | FormatDetector.detect detects the file format of the provided stream, using the optional file name, and returns a FileFormat. |
| `FrontFace` | Front face winding order. |
| `Frustum` | Frustum.to_mesh() generates a Mesh representation of a viewing frustum, useful for visual debugging of camera volumes. |
| `GLSLSource` | GLSL shader source. |
| `Geometry` | Geometry.create_element creates a VertexElement of the given type, mapping and reference modes. |
| `GlobalTransform` | The GlobalTransform class exposes translation, scale, euler_angles, rotation, and transform_matrix properties for direct manipulation of an entity’s world transform. |
| `GltfEmbeddedImageFormat` | Embedded image format for GLTF. |
| `GltfExporter` | GltfExporter can export a scene to the glTF format and first checks support with supports_format(file_format). |
| `GltfFormat` | GltfFormat.create_load_options creates a GLTF-specific load options object for importing scenes. |
| `GltfFormatDetector` | GltfFormatDetector.detect determines the FileFormat of the provided stream, optionally using the file name. |
| `GltfImporter` | GltfImporter.supports_format returns true when the specified file format can be imported. |
| `GltfLoadOptions` | GltfLoadOptions.flip_tex_coord_v indicates whether to invert the V component of texture coordinates during GLTF import. |
| `GltfPlugin` | GltfPlugin.get_file_format returns the GltfFormat object representing the GLTF file format. |
| `GltfSaveOptions` | GltfSaveOptions.file_format specifies the output file format for saving, using the FileFormat enum. |
| `Group` | A Group represents the logical relationships of Node. |
| `HShape` | IFC compatible H-shape profile. |
| `HalfSpace` | HalfSpace represents a infinity space which is split by a plane, this can be used with BooleanOperator. |
| `HollowCircleShape` | IFC compatible hollow circle profile. |
| `HollowRectangleShape` | IFC compatible hollow rectangular shape with both inner/outer rounding corners. |
| `Html5SaveOptions` | Save options for HTML5. |
| `ImageRenderOptions` | ImageRenderOptions lets you configure rendering parameters such as background_color, enable_shadows, and asset_directories before passing the options to a renderer. |
| `ImportException` | Exception when Aspose.3D failed to open the specified source. |
| `Importer` | Importer.supports_format(file_format) returns true when the specified FileFormat is supported for import. |
| `IndexDataType` | Data type for indices. |
| `InitializationException` | Exception thrown when rendering initialization fails. |
| `InvalidOperationException` | Class extending Exception. |
| `JtLoadOptions` | Load options for JT. |
| `KeyFrame` | KeyFrame.time represents the timestamp of the keyframe in seconds. |
| `KeyframeSequence` | KeyframeSequence lets developers create animation curves with per‑keyframe interpolation and tangent control. |
| `LShape` | IFC compatible L-shape profile that defined by parameters. |
| `LambertMaterial` | The LambertMaterial class provides a full material system, allowing you to set emissive, ambient, diffuse, and transparent colors, as well as assign textures to predefined slots such as MAP_DIFFUSE and MAP_NORMAL. |
| `Light` | The Light class lets you configure lighting parameters such as near_plane, far_plane, aspect, ortho_height, and up direction for scene illumination. |
| `LightType` | Light types. |
| `Line` | A polyline is a path defined by a set of points with control_points, and connected by segments. |
| `LinearExtrusion` | Extrudes a 2D `Profile` into a solid entity along a linear direction; its `to_mesh()` conversion raises `NotImplementedError` in this FOSS build. |
| `LoadOptions` | Base class for every format-specific load-options type, holding a shared `file_name` and `file_system`. |
| `MappingMode` | MappingMode.CONTROL_POINT represents mapping based on each mesh control point individually. |
| `Material` | Material class lets you manage texture maps and custom properties, supporting specular, diffuse, emissive, ambient, and normal maps. |
| `MathUtils` | A set of useful mathematical utilities. |
| `Matrix4` | Matrix4.get_identity() returns a new identity Matrix4 instance that can be used as a starting point for building transformation chains. |
| `Mesh` | Mesh.create_polygon creates a new polygon and returns its index. |
| `Microsoft3MFFormat` | Microsoft 3MF format. |
| `Microsoft3MFSaveOptions` | Save options for Microsoft 3MF. |
| `MirroredProfile` | IFC compatible mirror profile. |
| `MorphTargetChannel` | MorphTargetChannel.get_weight(target) returns the current weight for the specified morph target, and set_weight(target, weight) updates it. |
| `MorphTargetDeformer` | MorphTargetDeformer.get_weight/set_weight (via its channels) control per-target blend weights for shape-key style animation. |
| `Node` | Node.add_entity adds the given Entity to this node's entity collection. |
| `NurbsCurve` | Represents a NURBS curve via control points, knot vectors, and degree; its `evaluate()`/`evaluate_at()` sampling methods raise `NotImplementedError` in this FOSS build. |
| `NurbsDirection` | Describes the knot vector, order, degree, and NURBS type along one parametric direction (U or V) of a `NurbsSurface`. |
| `NurbsSurface` | Represents a NURBS surface via control points and per-direction `NurbsDirection` data; its `to_mesh()` conversion raises `NotImplementedError` in this FOSS build. |
| `NurbsType` | Enum with 3 members, `OPEN`, `CLOSED`, and `PERIODIC`, classifying a NURBS curve or surface direction. |
| `ObjExporter` | ObjExporter.export writes the given Scene to Wavefront OBJ, including per-node materials. |
| `ObjFormat` | ObjFormat.create_load_options creates and returns an ObjLoadOptions instance for importing OBJ files. |
| `ObjFormatDetector` | ObjFormatDetector.detect inspects a stream and reports whether its content is Wavefront OBJ. |
| `ObjImporter` | ObjImporter.import_scene loads OBJ data from a stream into a Scene using ObjLoadOptions. |
| `ObjLoadOptions` | ObjLoadOptions.flip_coordinate_system swaps the Y and Z axes when loading an OBJ file. |
| `ObjPlugin` | ObjPlugin.get_file_format returns the ObjFormat object representing the OBJ file format. |
| `ObjSaveOptions` | ObjSaveOptions.apply_unit_scale applies the scene's unit scaling when saving to OBJ. |
| `ParameterizedProfile` | The base class of all parameterized profiles. |
| `ParseException` | Exception when Aspose.3D failed to parse the input. |
| `Patch` | Patch objects allow creation of custom vertex elements via create_element and create_element_uv methods. |
| `PatchDirection` | Describes the knot vector, degree, and `PatchDirectionType` along one parametric direction of a `Patch`. |
| `PatchDirectionType` | Enum with 5 members: `BEZIER`, `QUADRATIC_BEZIER`, `CARDINAL_SPLINE`, `BASIS_SPLINE`, `LINEAR`. |
| `PbrMaterial` | PbrMaterial supplies a full physically based rendering workflow with albedo, metallic, roughness, occlusion, and emissive textures. |
| `PbrSpecularMaterial` | Material for physically based rendering based on diffuse color/specular/glossiness. |
| `PdfFormat` | Adobe's Portable Document Format. |
| `PdfLightingScheme` | Lighting scheme for PDF export. |
| `PdfLoadOptions` | Load options for PDF. |
| `PdfRenderMode` | Render mode for PDF export. |
| `PdfSaveOptions` | Save options for PDF. |
| `PhongMaterial` | PhongMaterial.specular_color defines the RGB color of the specular highlight. |
| `PixelFormat` | Pixel format for render targets. |
| `PixelMapMode` | Pixel mapping mode. |
| `PixelMapping` | Pixel mapping configuration. |
| `Plane` | The Plane class can be converted to a Mesh by calling its to_mesh() method, enabling further mesh processing. |
| `Plugin` | Plugin.get_exporter() returns an Exporter object that can be used to write supported 3D formats. |
| `PlyFormat` | PLY format. |
| `PlyLoadOptions` | Load options for PLY. |
| `PlySaveOptions` | Save options for PLY. |
| `PointCloud` | Stores unconnected 3D points as a scene entity; its `from_geometry()`/`from_geometry_with_density()` factory methods raise `NotImplementedError` in this FOSS build. |
| `PolygonBuilder` | The PolygonBuilder class lets you construct polygon vertex indices by calling begin(), add_vertex(index) for each vertex, and end() to finalize the polygon. |
| `PolygonMode` | Polygon rendering mode. |
| `PolygonModifier` | PolygonModifier.triangulate can return None, a Mesh object, or a list of triangle index arrays, giving developers flexibility in handling polygon data. |
| `Pose` | Pose.add_bone_pose(node, matrix, local_matrix) records a bone transformation for skeletal animation within a Pose object. |
| `PostProcessing` | Post-processing effect. |
| `PresetShaders` | Predefined shaders. |
| `Primitive` | Base class for parameterized shape entities (`Box`, `Sphere`, `Cylinder`, and similar); the base `to_mesh()` itself raises `NotImplementedError` and is overridden by each real subclass. |
| `Profile` | 2D Profile in xy plane. |
| `ProjectionType` | Camera's projection types. |
| `Property` | Property.get_extra returns the extra attribute identified by the given name. |
| `PropertyCollection` | PropertyCollection.find_property returns the property object matching the given name or None. |
| `PropertyFlags` | Property's flags. |
| `PushConstant` | Push constant for shaders. |
| `Pyramid` | Parameterized pyramid. |
| `Quaternion` | Quaternion.slerp(t, v1, v2) returns an interpolated quaternion for smooth rotation animations. |
| `Rect` | A class to represent the rectangle. |
| `RectangleShape` | IFC compatible rectangle profile. |
| `RectangularTorus` | Parameterized rectangular torus entity. |
| `ReferenceMode` | ReferenceMode.DIRECT represents a reference mode where vertex data is stored directly without indexing. |
| `RelativeRectangle` | Relative rectangle The formula between relative component to absolute value is: Scale * (Reference Width) + offset So if we want it to represent an absolute value, leave all scale fields zero, and use offset fields instead. |
| `RenderFactory` | RenderFactory creates all resources that represented in rendering pipeline. |
| `RenderParameters` | Parameters for rendering. |
| `RenderQueueGroupId` | Render queue group ID. |
| `RenderResource` | Base class for render resources. |
| `RenderStage` | Render stage in the pipeline. |
| `RenderState` | Render state configuration. |
| `Renderer` | The context about renderer. |
| `RendererVariableManager` | Manages renderer variables. |
| `RevolvedAreaSolid` | RevolvedAreaSolid entity. |
| `RotationMode` | The frustum's rotation mode. |
| `RotationOrder` | The order controls which rx ry rz are applied in the transformation matrix. |
| `RvmFormat` | RVM format. |
| `RvmLoadOptions` | Load options for RVM. |
| `RvmSaveOptions` | Save options for RVM. |
| `SPIRVSource` | SPIRV shader source. |
| `SaveOptions` | SaveOptions.export_textures determines if textures are included in the exported file. |
| `Scene` | The Scene class provides a high‑level API for loading, saving, rendering, and animating 3D content. |
| `SceneObject` | SceneObject provides find_property, get_property, and set_property methods to manage custom metadata attached to any scene object. |
| `SemanticAttribute` | Allow user to use their own structure for static declaration of VertexDeclaration. |
| `ShaderException` | Exception thrown when shader compilation/linking fails. |
| `ShaderMaterial` | A shader material allows to describe the material by external rendering engine or shader language. |
| `ShaderProgram` | Shader program. |
| `ShaderSet` | Set of shaders for rendering. |
| `ShaderSource` | Shader source code. |
| `ShaderStage` | Shader stage. |
| `ShaderTechnique` | A technique in shader material describes the concrete rendering details. |
| `ShaderVariable` | Shader variable. |
| `Shape` | Base class for all shape entities. |
| `Skeleton` | The Skeleton is mainly used by CAD software to help designer to manipulate the transformation of skeletal structure, it's usually useless outside the CAD softwares. |
| `SkeletonType` | Skeleton type enum. |
| `SkinDeformer` | Binds a `Skeleton`'s bones to mesh vertices for skeletal-animation skinning. |
| `Sphere` | Sphere.to_mesh() converts the parameterized sphere primitive into a Mesh for further processing. |
| `SplitMeshPolicy` | Share vertex/control point data between sub-meshes or each sub-mesh has its own compacted data. |
| `StencilAction` | Stencil action. |
| `StencilState` | Stencil state configuration. |
| `StlExporter` | StlExporter.supports_format returns True if the given file format is supported for STL export. |
| `StlFormat` | StlFormat.create_load_options creates an STL-specific load options object. |
| `StlFormatDetector` | StlFormatDetector.detect returns the detected FileFormat for a stream (optional file name) or None. |
| `StlImporter` | StlImporter.supports_format returns true when the specified file format can be handled by this importer. |
| `StlLoadOptions` | Load options for STL import, including `flip_coordinate_system` and unit-scale settings. |
| `StlPlugin` | StlPlugin.get_file_format returns the StlFormat object representing the STL file format. |
| `StlSaveOptions` | StlSaveOptions.scale specifies a uniform scaling factor applied to all coordinates during STL export. |
| `SweptAreaSolid` | SweptAreaSolid entity. |
| `TShape` | IFC compatible T-shape defined by parameters. |
| `Text` | Text profile, this profile describes contours using font and text. |
| `Texture` | This class defines the texture from an external file. |
| `TextureBase` | Base class for all texture types. |
| `TextureCodec` | Texture codec. |
| `TextureData` | Texture data. |
| `TextureFilter` | Texture filter type. |
| `TextureMapping` | TextureMapping.AMBIENT represents the ambient texture mapping channel. |
| `TextureSlot` | Texture slot name. |
| `TextureType` | Texture type. |
| `ThreeMfExporter` | ThreeMfExporter.export writes the provided Scene to the given stream using optional export settings. |
| `ThreeMfFormat` | ThreeMfFormat.is_buildable(node) returns a boolean indicating whether a node can be used as a printable build object. |
| `ThreeMfFormatDetector` | ThreeMfFormatDetector.detect determines the 3MF file format from a stream and optional file name, returning a FileFormat. |
| `ThreeMfImporter` | ThreeMfImporter.import_scene(scene, stream, options) reads a 3MF file from a stream and populates the given Scene instance. |
| `ThreeMfLoadOptions` | ThreeMfLoadOptions.flip_coordinate_system swaps Y and Z coordinates when loading a 3MF file. |
| `ThreeMfPlugin` | ThreeMfPlugin.get_file_format returns the ThreeMfFormat object that identifies the 3MF file format. |
| `ThreeMfSaveOptions` | ThreeMfSaveOptions.enable_compression enables compression of the exported 3MF file. |
| `Token` | A single lexical token produced by the FBX tokenizers, exposing its `value`, `text`, and `type`. |
| `TokenType` | The FBX token kinds (`OPEN_BRACKET`, `CLOSE_BRACKET`, `DATA`, `COMMA`, `KEY`); `TokenType.to_string(t)` names a kind. |
| `Torus` | Parameterized torus entity. |
| `Transform` | Transform.set_translation sets the translation components (tx, ty, tz) and returns the Transform. |
| `TransformBuilder` | The TransformBuilder is used to build transform matrix by a chain of transformations. |
| `TransformedCurve` | TransformedCurve entity. |
| `TrapeziumShape` | IFC compatible Trapezium shape defined by parameters. |
| `TriMesh` | TriMesh is a triangle mesh that stores triangles. |
| `TrialException` | This is raised in Scene.Open/Scene.Save when no licenses are applied. |
| `TrimmedCurve` | TrimmedCurve entity. |
| `U3dLoadOptions` | Load options for U3D. |
| `U3dSaveOptions` | Save options for U3D. |
| `UShape` | IFC compatible U-shape defined by parameters. |
| `UsdSaveOptions` | Save options for USD. |
| `Vector2` | Vector2.set sets the vector's x and y components to the provided float values. |
| `Vector3` | Vector3 supports inner and cross products, normalization, angle calculation, and component-wise trigonometric functions. |
| `Vector4` | Vector4.set assigns new component values to the vector's x, y, z, and w fields. |
| `Vertex` | Vertex reference, used to access the raw vertex in TriMesh. |
| `VertexDeclaration` | The declaration of a custom defined vertex's structure. |
| `VertexElement` | VertexElement.set_indices sets the element's index list to the provided integer list. |
| `VertexElementBinormal` | Per-vertex binormal-vector element, storing tangent-space binormal data for each polygon vertex. |
| `VertexElementDoublesTemplate` | A helper class for defining concrete implementations. |
| `VertexElementEdgeCrease` | Defines the edge crease values for specified components. |
| `VertexElementFVector` | VertexElementFVector.set_data replaces the element's data list with the provided FVector4 collection. |
| `VertexElementHole` | Defines the hole information for specified components. |
| `VertexElementIntsTemplate` | A helper class for defining concrete implementations with int data. |
| `VertexElementMaterial` | Defines the material for specified components. |
| `VertexElementNormal` | Per-vertex normal-vector element, storing shading normals for each polygon vertex. |
| `VertexElementPolygonGroup` | Defines the polygon group for specified components. |
| `VertexElementSmoothingGroup` | Per-polygon smoothing-group element, used to control normal generation across adjacent faces. |
| `VertexElementSpecular` | Defines the specular color for specified components. |
| `VertexElementTangent` | VertexElementTangent.set_data(data) assigns tangent vectors to the specified vertices, while set_indices() can map them to polygon vertices when needed. |
| `VertexElementTemplate` | A helper class for defining concrete implementations of vertex elements with typed data. |
| `VertexElementType` | VertexElementType.BINORMAL represents the per-vertex binormal vector used for tangent space calculations. |
| `VertexElementUV` | VertexElementUV.texture_mapping gets or sets the texture mapping mode for the UV element. |
| `VertexElementUserData` | Defines the user data for specified components. |
| `VertexElementVector4` | Defines the vector4 data for specified components. |
| `VertexElementVertexColor` | Per-vertex color element, storing an RGBA color for each polygon vertex. |
| `VertexElementVertexCrease` | Defines the vertex crease values for specified components. |
| `VertexElementVisibility` | Defines the visibility for specified components. |
| `VertexElementWeight` | Defines the weight for specified components. |
| `VertexField` | Vertex's field memory layout description. |
| `VertexFieldDataType` | Vertex field's data type. |
| `VertexFieldSemantic` | The semantic of the vertex field. |
| `Viewport` | Viewport for rendering. |
| `Watermark` | Utility to encode/decode blind watermark to/from a mesh. |
| `WindowHandle` | Window handle for render window. |
| `WrapMode` | Wrap mode for texture coordinates. |
| `XLoadOptions` | Load options for X format. |
| `ZShape` | IFC compatible Z-shape profile that defined by parameters. |

#### Enumerations

| Class | Description |
|---|---|
| `ExtrapolationType` | ExtrapolationType.CONSTANT represents a constant extrapolation that holds the last keyframe value. |
| `Interpolation` | Interpolation.CONSTANT represents a constant interpolation where values do not change over time. |
| `PoseType` | Enum with 2 members, `BIND_POSE` and `SNAPSHOT`, identifying how a `Pose` was captured. |
| `StepMode` | StepMode.PREVIOUS_VALUE represents a step mode that selects the previous value in a sequence. |
| `WeightedMode` | WeightedMode enum values NONE, OUT_WEIGHT, NEXT_IN_WEIGHT, and BOTH let developers specify how vertex weights are applied during mesh processing. |

</details>

## Documentation & Resources

- **[Getting started guide](https://docs.aspose.org/3d/python/)** — installation, walkthroughs, and feature guides for this library.
- **[How-to guides & FAQ](https://kb.aspose.org/3d/python/)** — task-focused answers for common 3D-processing questions.
- **[Full API reference](https://reference.aspose.org/3d/python/)** — the complete, browsable reference for all 305 public types (the [API reference](#api-reference) section above covers the essentials).
- **[Implementation progress notes](docs/foss-python-progress.md)** — current FOSS-edition porting status, in the repository.
- **[Release process](docs/releasing.md)** — how a version of `aspose-3d-foss` is tagged and published to PyPI, in the repository.
- **Internal format-implementation notes** (historical development records, not maintained as user guides): [Scene/Node/Entity/Transform](docs/IMPLEMENTATION_SUMMARY.md), [OBJ importer](docs/OBJ_IMPORTER_IMPLEMENTATION.md), [STL import/export](docs/STL_IMPORT_IMPLEMENTATION.md), [FBX parser](docs/FBX_IMPLEMENTATION_SUMMARY.md), and [PyPI packaging readiness](docs/PYPI_READINESS.md), in the repository.
- Found a bug or have a feature request? [Open an issue](https://github.com/aspose-3d-foss/Aspose.3D-FOSS-for-Python/issues) on GitHub.

## Scope and Limitations

- No file format registers an importer or exporter for PDF, PLY, RVM, U3D, JT, AMF, HTML5,
  A3DW, USD, or Draco in this build — `PdfSaveOptions`, `PlyLoadOptions`, `DracoSaveOptions`,
  and similar option classes exist as public types, but `Scene.open()`/`Scene.save()` cannot
  detect or dispatch any of these extensions, and raise a `RuntimeError` if you try.
- FBX support is experimental. `FbxImporter` has a real, working ASCII/binary tokenizer and
  parser, but no bundled test opens a real `.fbx` fixture through it — the only FBX tests
  exercise the tokenizer directly against hand-written snippets — so treat FBX import as
  lightly verified rather than production-hardened. `FbxExporter.save()`/`save_to_stream()`
  both raise `NotImplementedError` outright, so FBX is import-only at best.
- COLLADA import works, but COLLADA export is not reachable through `Scene.save()`:
  `IOService`'s exporter lookup walks its registered exporters in order and reaches
  `FbxExporter` (whose `supports_format()` is unimplemented and raises unconditionally) before
  it ever reaches `ColladaExporter`, so the lookup itself fails before a real, working
  `ColladaExporter` is ever consulted — reproduced directly against this build.
- Always import a format's load/save options class from its own format submodule (as every
  example in this README does), never from the shared top-level `aspose.threed.formats`
  package — for OBJ, STL, glTF, and COLLADA specifically, the top-level package name resolves
  to a broken duplicate with no working base class, which format detection silently rejects.
  3MF and FBX are unaffected. Import COLLADA classes by their exact file path
  (`aspose.threed.formats.collada.ColladaLoadOptions`, and so on) — that submodule has no
  package-init re-export, so the shorter package-style import used for other formats resolves
  to a module object instead of the class you want.
- `Scene.render()` and the entire `aspose.threed.render` module (`Renderer`, `RenderFactory`,
  `Viewport`, and related classes) raise `NotImplementedError` — this library does not render
  scenes to images.
- `Texture` and `TextureBase` raise `NotImplementedError` on construction, so an image-backed
  texture cannot be created; material color and factor properties (`diffuse_color`,
  `albedo`, `metallic_factor`, and similar) work independently of texture assignment.
- `Watermark.encode_watermark()`/`decode_watermark()` and every `TransformBuilder` method raise
  `NotImplementedError` — build node transforms through `Transform`'s own translation,
  rotation, and scaling properties instead of the fluent `TransformBuilder` chain.
- `Mesh.do_boolean()`, `union()`, `difference()`, and `intersect()` raise `NotImplementedError`
  — Boolean/CSG mesh operations are not implemented, even though `BooleanOperator` and
  `BooleanOperand` exist as configuration holders.
- `NurbsCurve.evaluate()`/`evaluate_at()` and `NurbsSurface.to_mesh()` raise
  `NotImplementedError` — NURBS curves and surfaces can be configured but not sampled or
  converted to a `Mesh`.
- `PointCloud.from_geometry()`/`from_geometry_with_density()` raise `NotImplementedError`, and
  `AxisSystem` raises `NotImplementedError` on every method, including construction.

These limitations don't apply to
[Aspose.3D for Python — Enterprise Edition](https://products.aspose.com/3d/python-net/), which adds the
broader proprietary-format support (PDF, PLY, USD, and more), rendering, and advanced mesh
operations that this FOSS build leaves unimplemented.

## Development and Testing

Install the repository and run the test suite:

```bash
python3 -m pip install -e .
python3 -m unittest discover tests/
```

Run a single test file:

```bash
python -m unittest tests.test_obj_importer
```

The suite covers 33 real test files exercising OBJ, STL, glTF, COLLADA, and 3MF import/export,
polygon triangulation, and format-detection behavior. Build and test commands for autonomous
coding tools are documented in [AGENTS.md](AGENTS.md).

Releases are cut by bumping `version` in `setup.py`, tagging `v<version>`, and publishing a
GitHub Release; the [publish workflow](.github/workflows/publish.yml) then builds the
distribution, checks it, and uploads it to PyPI. The full procedure is in
[docs/releasing.md](docs/releasing.md).

## License

This project is licensed under the [MIT License](LICENSE). The MIT License permits use,
copying, modification, distribution, sublicensing, and commercial use, provided its copyright
and permission notice are retained. The software is provided without warranty.
