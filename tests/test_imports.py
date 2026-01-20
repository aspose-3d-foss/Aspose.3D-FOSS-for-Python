#!/usr/bin/env python3
"""
Simple test to verify module imports
"""

print("Testing module imports...")

try:
    from aspose.threed import Scene, Node, Entity, Light
    from aspose.threed.utilities import Vector3, Matrix4

    scene = Scene()
    node = Node("test_node")
    print(f"Scene created: {scene}")
    print(f"Node created: {node}")

    vec = Vector3(1.0, 2.0, 3.0)
    print(f"Vector3 created: {vec}")

    mat = Matrix4()
    print(f"Matrix4 created: {mat}")

    light = Light("test_light")
    print(f"Light created: {light}")

    print("Module imports successful!")
except Exception as e:
    print(f"Error importing: {e}")