# FOSS Python Progress

## Current Version
- Target: 26.2.0
- Last Sync: 2026-07-04
- Last Sync SHA: 8c981b3 (June 22, 2026) - Pose/BonePose/PoseType enhancements

## Porting Status

### Stage: Source Port (Initial Sync) - COMPLETE

### Completed Ports

#### Core Classes (Stage 1)
- A3DObject, INamedObject, SceneObject, Scene, Node, Entity, Transform, GlobalTransform
- Property, PropertyCollection, AssetInfo, CustomObject
- BoundingBox, BoundingBoxExtent (with enum-like values NULL, FINITE, INFINITE)
- PolygonBuilder.InvalidOperationException (stub)

#### Core Classes (Stage 1 - Complete)
- A3DObject
- INamedObject
- SceneObject
- Scene
- Node
- Entity
- Transform
- GlobalTransform
- Property
- PropertyCollection
- AssetInfo
- CustomObject

#### Entities
- Mesh
- Light
- Camera
- Geometry
- Primitive (now properly inherits from Geometry)
- Box, Cylinder, Sphere, Plane, Dish, Circle, Ellipse, Frustum, Pyramid, Torus
- Curve, Line, NurbsCurve, NurbsDirection

#### Animation
- ExtrapolationType
- Interpolation
- WeightedMode
- StepMode
- Extrapolation
- KeyFrame
- KeyframeSequence
- AnimationChannel
- BindPoint
- AnimationNode

#### Animation
- ExtrapolationType
- Interpolation
- WeightedMode
- StepMode
- Extrapolation
- KeyFrame
- KeyframeSequence
- AnimationChannel
- BindPoint
- AnimationNode
- AnimationClip

#### File Format I/O (FOSS Supported)
- OBJ (import/export)
- STL (import/export)
- GLTF (import/export)
- 3MF (import/export)
- FBX (import/export)
- Collada (import/export)

#### Utilities
- Vector2, Vector3, Vector4
- Matrix4
- Quaternion
- BoundingBox
- FVector2, FVector3, FVector4
- ArrayListAdapter (implements IArrayList interface for list-like collections)

#### Materials
- Material
- PhongMaterial
- LambertMaterial
- PbrMaterial

#### Profiles (New in 26.2.0)
- Profile (base class)
- ArbitraryProfile
- CenterLineProfile
- ParameterizedProfile
- Shape profiles: CircleShape, EllipseShape, RectangleShape, HShape, LShape, TShape, UShape, ZShape, CShape
- HollowCircleShape, HollowRectangleShape, TrapeziumShape
- MirroredProfile
- Text, FontFile

#### New in 26.2.0
- PoseType (enum)
- BonePose
- Pose

#### Vertex Elements
- VertexElement (base class with SetIndices and Clear methods)
- VertexElementFVector (helper class with Data property using ArrayListAdapter)
- VertexElementUV, VertexElementVertexColor, VertexElementMaterial, VertexElementNormal, etc.

#### Deformers
- Deformer (base class with owner property)
- SkinDeformer
- MorphTargetDeformer
- Bone

## .NET FOSS Sync

### Last Synced Commit
- 61580ea (June 12, 2026) - Geometry ToMesh() implementation and API signature alignment
### Commits Since Last Sync
- 7460409 - fix: Use PNG icon for nuget package (no code changes)
- 19f0b01 - Merge branch \u0027main\u0027
- a1221bf - chore: Add nuget package logo (no code changes)
- 76ee798 - README updated with correct nuget reference csproj updated with multiple framework version support (no code changes)
- 71581fd - chore: Rename assembly and package to Aspose.3D.FOSS (no code changes)
- 8c981b3 - feat: Enhance Pose class with BonePose/PoseType and fix matrix serialization (COMPLETE - see below)

### Changes Ported from Commit 8c981b3
- **Pose class**: Added `PoseType` property and `BonePoses` collection
- **BonePose class**: New class for skinning poses with `node`, `matrix`, `is_local` properties
- **PoseType enum**: New enum with `BIND_POSE` and `SNAPSHOT` values
- **FMatrix4**: Added `__mul__` operator methods for `FVector4`, `FVector3`, `int/float`, and `FMatrix4`
- **IOExtension**: Added `write()` method for Matrix4, FMatrix4, FVector2, FVector3, FVector4, Vector2, Vector3, Vector4
### Changes Ported from Commits
- **Geometry**: Added `deformers` property and `GetDeformers<T>()` method
- **Geometry**: Changed `ControlPoints` to use `ArrayListAdapter` instead of plain list
- **VertexElement**: Added `SetIndices()` and `Clear()` methods with proper indices handling
- **VertexElementFVector**: Added `Data` property using `ArrayListAdapter`
- **Primitive**: Fixed inheritance from `Geometry` (was incorrectly inheriting from `Entity`)
- **Mesh**: Removed override of `deformers` property that returned empty list
- **ArrayList**: Added `ArrayListAdapter` class that wraps `List[T]` and implements IArrayList-like interface

## API Classification

### Category 1: Excluded (Not Implemented)
- License: License class
- Metered: Metered class
- Trial: TrialException
- DRM: All DRM-related functionality

### Category 2: Stub (Raises NotImplementedError)
- Scene.render()
- ImageRenderOptions

### Category 3: Full Implementation
- All core classes, entities, file format I/O, utilities, materials, and Pose/BonePose/PoseType

## Deviations from .NET FOSS

### Pose Class Implementation
- The .NET FOSS uses `IList<BonePose>` for BonePoses property
- Python implementation uses `List[BonePose]` (Pythonic typing)
- Both `AddBonePose` overloads are ported (using default argument)

### PoseType Enum
- .NET: `BindPose`, `Snapshot`
- Python: `BIND_POSE`, `SNAPSHOT` (Pythonic constant naming)

### FMatrix4 Operators
- Ported `__mul__` for `FVector4`, `FVector3`, `int/float`, and `FMatrix4`
- Ported `__rmul__` for reverse multiplication

### IOExtension
- Added `write()` static method for all matrix and vector types

## Tests
- Total Tests: 101
- Passing: 101
- Failing: 0

## Deviations from .NET FOSS

### ArrayListAdapter
- Python implementation of `ArrayListAdapter` wraps a Python `list` and provides IArrayList-like interface
- The .NET FOSS uses `IArrayList<T>` interface with `ArrayListAdapter<T>` implementation
- Python uses direct class without explicit interface

### Primitive Inheritance
- .NET FOSS: `Primitive : Geometry`
- Python FOSS: Fixed to match .NET (was incorrectly `Primitive : Entity`)

### ControlPoints Property
- .NET FOSS: Returns `IArrayList<Vector4>` via `ArrayListAdapter`
- Python FOSS: Returns `ArrayListAdapter[Vector4]`

### Deformers Property
- .NET FOSS: Returns `IList<Deformer>` (direct list)
- Python FOSS: Returns `List[Deformer]`

### Pose Class Implementation
- The .NET FOSS uses `IList<BonePose>` for BonePoses property
- Python implementation uses `List[BonePose]` (Pythonic typing)
- Both `AddBonePose` overloads are ported

### PoseType Enum
- .NET: `BindPose`, `Snapshot`
- Python: `BIND_POSE`, `SNAPSHOT` (Pythonic constant naming)

### Boolean Types
- New types ported: `BooleanOperand`, `BooleanOperator`, `BooleanOperation`

### Commit 61580ea (June 12, 2026)
- **Torus**: Changed from `Curve` to `Primitive`, implemented `ToMesh()` method with proper torus geometry
- **RectangularTorus**: Changed from `Curve` to `Primitive`, implemented `ToMesh()` method with rectangular cross-section
- **BasicLoadOptions**: Added concrete `LoadOptions` subclass
- **VertexElementTemplate**: Generic abstract base class for typed vertex elements
- **VertexElementDoublesTemplate**: Updated to inherit from `VertexElementTemplate[float]`
- **VertexElementIntsTemplate**: Updated to inherit from `VertexElementTemplate[int]`
- **VertexElementTemplate**: Exported in `aspose.threed.entities` package

## Next Steps
1. Continue monitoring .NET FOSS for new commits
2. Port any new types as they are added
3. Update pyproject.toml version to 26.2.0 when .NET FOSS version is bumped
