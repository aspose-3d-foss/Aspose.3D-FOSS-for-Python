#!/usr/bin/env python3
"""Simple test to verify module structure"""

print("Testing module structure...")

try:
    from aspose.threed.utilities import Vector3, Quaternion, Matrix4
    print("✓ Utilities imported successfully")

    v = Vector3(1.0, 2.0, 3.0)
    q = Quaternion(1.0, 0.0, 0.0, 0.0)
    m = Matrix4()

    print(f"  ✓ Created Vector3: {v}")
    print(f"  ✓ Created Quaternion: {q}")
    print(f"  ✓ Created Matrix4: {m}")

except Exception as e:
    print(f"✗ Error importing utilities: {e}")

try:
    from aspose.threed import Scene, Node, Entity, Transform, GlobalTransform
    print("✓ Core classes imported successfully")

except Exception as e:
    print(f"✗ Error importing core classes: {e}")

print("\nModule structure test completed!")
