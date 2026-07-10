using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Xml.Linq;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;

namespace Aspose.ThreeD.Formats
{
    internal class ColladaReader : IImporter
    {
        public Scene Import(Stream stream, LoadOptions options)
        {
            return Read(stream);
        }

        private static Scene Read(Stream stream)
        {
            var scene = new Scene();
            
            XDocument doc;
            using (var reader = new StreamReader(stream))
            {
                doc = XDocument.Load(reader);
            }

            var ns = doc.Root!.Name.Namespace;

            var upAxis = "Y_UP";
            var assetElement = doc.Root.Element(ns + "asset");
            if (assetElement != null)
            {
                var upAxisElement = assetElement.Element(ns + "up_axis");
                if (upAxisElement != null)
                {
                    upAxis = upAxisElement.Value.Trim();
                }
            }

            var geometryMap = new Dictionary<string, Mesh>();
            var materialMap = new Dictionary<string, Shading.Material>();
            var effectMap = new Dictionary<string, Shading.Material>();
            var nodeMap = new Dictionary<string, Node>();
            var cameraMap = new Dictionary<string, Camera>();

            LoadGeometries(doc, ns, geometryMap);
            LoadMaterials(doc, ns, materialMap, effectMap);
            LoadCameras(doc, ns, cameraMap);
            
            var visualSceneMap = LoadVisualScene(doc, ns, geometryMap, materialMap, effectMap, nodeMap, cameraMap, upAxis);
            
            var sceneElement = doc.Root.Element(ns + "scene");
            if (sceneElement != null)
            {
                var instanceVisualScene = sceneElement.Element(ns + "instance_visual_scene");
                if (instanceVisualScene != null)
                {
                    var url = instanceVisualScene.Attribute("url")?.Value;
                    if (!string.IsNullOrEmpty(url) && url.StartsWith("#"))
                    {
                        var sceneId = url.Substring(1);
                        if (visualSceneMap.TryGetValue(sceneId, out var rootNode))
                        {
                            foreach (var childNode in rootNode.ChildNodes)
                            {
                                scene.RootNode.ChildNodes.Add(childNode);
                            }
                        }
                    }
                }
            }

            return scene;
        }

        private static void LoadGeometries(XDocument doc, XNamespace ns, Dictionary<string, Mesh> geometryMap)
        {
            var libraryGeometries = doc.Root?.Element(ns + "library_geometries");
            if (libraryGeometries == null)
                return;

            foreach (var geometryElement in libraryGeometries.Elements(ns + "geometry"))
            {
                var id = geometryElement.Attribute("id")?.Value;
                if (string.IsNullOrEmpty(id))
                    continue;

                var meshElement = geometryElement.Element(ns + "mesh");
                if (meshElement == null)
                    continue;

                var mesh = ParseMesh(meshElement, ns);
                mesh.Name = geometryElement.Attribute("name")?.Value ?? id;

                geometryMap[id] = mesh;
            }
        }

        private static Mesh ParseMesh(XElement meshElement, XNamespace ns)
        {
            var mesh = new Mesh();

            var sourceMap = new Dictionary<string, List<float>>();
            var vertexSourceMap = new Dictionary<string, string>();

            foreach (var sourceElement in meshElement.Elements(ns + "source"))
            {
                var sourceId = sourceElement.Attribute("id")?.Value;
                if (string.IsNullOrEmpty(sourceId))
                    continue;

                var floatArray = sourceElement.Element(ns + "float_array");
                if (floatArray == null)
                    continue;

                var values = new List<float>();
                var text = floatArray.Value.Trim();
                if (!string.IsNullOrEmpty(text))
                {
                    var parts = text.Split(new[] { ' ', '\t', '\n', '\r' }, StringSplitOptions.RemoveEmptyEntries);
                    foreach (var part in parts)
                    {
                        if (float.TryParse(part, out var val))
                        {
                            values.Add(val);
                        }
                    }
                }

                sourceMap[sourceId] = values;

                var accessor = sourceElement.Element(ns + "technique_common")?.Element(ns + "accessor");
                if (accessor != null)
                {
                    var sourceAttr = accessor.Attribute("source")?.Value;
                    if (!string.IsNullOrEmpty(sourceAttr) && sourceAttr.StartsWith("#"))
                    {
                        vertexSourceMap[sourceId] = sourceAttr.Substring(1);
                    }
                }
            }

            var verticesElement = meshElement.Element(ns + "vertices");
            if (verticesElement != null)
            {
                var verticesId = verticesElement.Attribute("id")?.Value;
                if (!string.IsNullOrEmpty(verticesId))
                {
                    foreach (var inputElement in verticesElement.Elements(ns + "input"))
                    {
                        var semantic = inputElement.Attribute("semantic")?.Value;
                        var source = inputElement.Attribute("source")?.Value;
                        if (!string.IsNullOrEmpty(semantic) && !string.IsNullOrEmpty(source) && source.StartsWith("#"))
                        {
                            var sourceId = source.Substring(1);
                            if (sourceMap.TryGetValue(sourceId, out var values))
                            {
                                if (semantic == "POSITION")
                                {
                                    for (int i = 0; i < values.Count; i += 3)
                                    {
                                        mesh.ControlPoints.Add(new Vector4(values[i], values[i + 1], values[i + 2], 1.0f));
                                    }
                                }
                            }
                        }
                    }
                }
            }

            foreach (var polylistElement in meshElement.Elements(ns + "polylist"))
            {
                ParsePolylist(polylistElement, mesh, sourceMap, ns);
            }

            foreach (var trianglesElement in meshElement.Elements(ns + "triangles"))
            {
                ParseTriangles(trianglesElement, mesh, sourceMap, ns);
            }

            return mesh;
        }

        private static void ParsePolylist(XElement polylistElement, Mesh mesh, Dictionary<string, List<float>> sourceMap, XNamespace ns)
        {
            var vcount = new List<int>();
            var vcountElement = polylistElement.Element(ns + "vcount");
            if (vcountElement != null)
            {
                var text = vcountElement.Value.Trim();
                if (!string.IsNullOrEmpty(text))
                {
                    var parts = text.Split(new[] { ' ', '\t', '\n', '\r' }, StringSplitOptions.RemoveEmptyEntries);
                    foreach (var part in parts)
                    {
                        if (int.TryParse(part, out var val))
                        {
                            vcount.Add(val);
                        }
                    }
                }
            }

            var pElement = polylistElement.Element(ns + "p");
            if (pElement == null)
                return;

            var indices = ParseIndices(pElement, polylistElement, ns);

            int index = 0;
            foreach (var count in vcount)
            {
                if (count < 3)
                    continue;

                var polygon = new int[count];
                for (int i = 0; i < count; i++)
                {
                    if (index < indices.Length)
                    {
                        polygon[i] = indices[index++];
                    }
                }
                mesh.CreatePolygon(polygon);
            }
        }

        private static void ParseTriangles(XElement trianglesElement, Mesh mesh, Dictionary<string, List<float>> sourceMap, XNamespace ns)
        {
            var countAttr = trianglesElement.Attribute("count");
            var count = countAttr != null ? int.Parse(countAttr.Value) : 0;

            var pElement = trianglesElement.Element(ns + "p");
            if (pElement == null)
                return;

            var indices = ParseIndices(pElement, trianglesElement, ns);

            for (int i = 0; i < count; i++)
            {
                if (i * 3 + 2 >= indices.Length)
                    break;

                mesh.CreatePolygon(indices[i * 3], indices[i * 3 + 1], indices[i * 3 + 2]);
            }
        }

        private static int[] ParseIndices(XElement pElement, XElement parentElement, XNamespace ns)
        {
            var text = pElement.Value.Trim();
            var parts = text.Split(new[] { ' ', '\t', '\n', '\r' }, StringSplitOptions.RemoveEmptyEntries);
            var indices = new int[parts.Length];

            for (int i = 0; i < parts.Length; i++)
            {
                if (int.TryParse(parts[i], out var val))
                {
                    indices[i] = val;
                }
            }

            return indices;
        }

        private static void LoadMaterials(XDocument doc, XNamespace ns, Dictionary<string, Shading.Material> materialMap, Dictionary<string, Shading.Material> effectMap)
        {
            var libraryMaterials = doc.Root?.Element(ns + "library_materials");
            if (libraryMaterials != null)
            {
                foreach (var materialElement in libraryMaterials.Elements(ns + "material"))
                {
                    var id = materialElement.Attribute("id")?.Value;
                    if (string.IsNullOrEmpty(id))
                        continue;

                    var instanceEffect = materialElement.Element(ns + "instance_effect");
                    if (instanceEffect != null)
                    {
                        var url = instanceEffect.Attribute("url")?.Value;
                        if (!string.IsNullOrEmpty(url) && url.StartsWith("#"))
                        {
                            var effectId = url.Substring(1);
                            if (effectMap.TryGetValue(effectId, out var effect))
                            {
                                materialMap[id] = effect;
                            }
                        }
                    }
                }
            }

            var libraryEffects = doc.Root?.Element(ns + "library_effects");
            if (libraryEffects != null)
            {
                foreach (var effectElement in libraryEffects.Elements(ns + "effect"))
                {
                    var id = effectElement.Attribute("id")?.Value;
                    if (string.IsNullOrEmpty(id))
                        continue;

                    var effect = ParseEffect(effectElement, ns);
                    if (effect != null)
                    {
                        effectMap[id] = effect;
                    }
                }
            }
        }

        private static Shading.Material? ParseEffect(XElement effectElement, XNamespace ns)
        {
            var profileCommon = effectElement.Element(ns + "profile_COMMON");
            if (profileCommon == null)
                return null;

            var technique = profileCommon.Element(ns + "technique");
            if (technique == null)
                return null;

            var shaderType = technique.Elements().FirstOrDefault();
            if (shaderType == null)
                return null;

            // Determine material type based on shader type
            Shading.Material material;
            var shaderTypeName = shaderType.Name.LocalName;
            if (shaderTypeName == "phong")
            {
                material = new Shading.PhongMaterial();
            }
            else if (shaderTypeName == "lambert")
            {
                material = new Shading.LambertMaterial();
            }
            else
            {
                // Default to PhongMaterial for other shader types
                material = new Shading.PhongMaterial();
            }

            foreach (var property in shaderType.Elements())
            {
                var colorElement = property.Element(ns + "color");
                if (colorElement != null)
                {
                    var values = colorElement.Value.Trim().Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
                    if (values.Length >= 3)
                    {
                        if (float.TryParse(values[0], out var r) &&
                            float.TryParse(values[1], out var g) &&
                            float.TryParse(values[2], out var b))
                        {
                            if (property.Name.LocalName == "diffuse" && material is Shading.LambertMaterial lambert)
                            {
                                lambert.DiffuseColor = new Vector3(r, g, b);
                            }
                            else if (property.Name.LocalName == "emissive" && material is Shading.LambertMaterial lambert2)
                            {
                                lambert2.EmissiveColor = new Vector3(r, g, b);
                            }
                            else if (property.Name.LocalName == "ambient" && material is Shading.LambertMaterial lambert3)
                            {
                                lambert3.AmbientColor = new Vector3(r, g, b);
                            }
                            else if (property.Name.LocalName == "transparent" && material is Shading.LambertMaterial lambert4)
                            {
                                lambert4.TransparentColor = new Vector3(r, g, b);
                            }
                            else if (property.Name.LocalName == "specular" && material is Shading.PhongMaterial phong)
                            {
                                phong.SpecularColor = new Vector3(r, g, b);
                            }
                        }
                    }
                }
            }

            return material;
        }

        private static void LoadCameras(XDocument doc, XNamespace ns, Dictionary<string, Camera> cameraMap)
        {
            var libraryCameras = doc.Root?.Element(ns + "library_cameras");
            if (libraryCameras == null)
                return;

            foreach (var cameraElement in libraryCameras.Elements(ns + "camera"))
            {
                var id = cameraElement.Attribute("id")?.Value;
                if (string.IsNullOrEmpty(id))
                    continue;

                var camera = new Camera();
                camera.Name = cameraElement.Attribute("name")?.Value ?? id;

                var optics = cameraElement.Element(ns + "optics");
                if (optics == null)
                    continue;

                var techniqueCommon = optics.Element(ns + "technique_common");
                if (techniqueCommon == null)
                    continue;

                var perspective = techniqueCommon.Element(ns + "perspective");
                if (perspective == null)
                {
                    var orthographic = techniqueCommon.Element(ns + "orthographic");
                    if (orthographic != null)
                    {
                        camera.Name = "OrthographicCamera";
                    }
                    continue;
                }

                cameraMap[id] = camera;
            }
        }

        private static Dictionary<string, Node> LoadVisualScene(
            XDocument doc, 
            XNamespace ns, 
            Dictionary<string, Mesh> geometryMap, 
            Dictionary<string, Shading.Material> materialMap, 
            Dictionary<string, Shading.Material> effectMap,
            Dictionary<string, Node> nodeMap,
            Dictionary<string, Camera> cameraMap,
            string upAxis)
        {
            var visualSceneMap = new Dictionary<string, Node>();
            var libraryVisualScenes = doc.Root?.Element(ns + "library_visual_scenes");
            if (libraryVisualScenes == null)
                return visualSceneMap;

            foreach (var visualSceneElement in libraryVisualScenes.Elements(ns + "visual_scene"))
            {
                var id = visualSceneElement.Attribute("id")?.Value;
                if (string.IsNullOrEmpty(id))
                    continue;

                var rootNode = new Node(visualSceneElement.Attribute("name")?.Value ?? id);
                visualSceneMap[id] = rootNode;

                foreach (var nodeElement in visualSceneElement.Elements(ns + "node"))
                {
                    ParseNode(nodeElement, ns, geometryMap, materialMap, effectMap, cameraMap, upAxis, rootNode, nodeMap);
                }
            }

            return visualSceneMap;
        }

        private static void ParseNode(
            XElement nodeElement, 
            XNamespace ns, 
            Dictionary<string, Mesh> geometryMap, 
            Dictionary<string, Shading.Material> materialMap,
            Dictionary<string, Shading.Material> effectMap,
            Dictionary<string, Camera> cameraMap,
            string upAxis,
            Node parentNode,
            Dictionary<string, Node> nodeMap)
        {
            var id = nodeElement.Attribute("id")?.Value;
            var name = nodeElement.Attribute("name")?.Value ?? "Node";

            var node = new Node(name);
            nodeMap[id ?? name] = node;

            if (parentNode != null)
            {
                parentNode.AddChildNode(node);
            }

            var matrix = ParseMatrix(nodeElement, ns);
            var translation = ParseTranslation(nodeElement, ns);
            var rotations = ParseRotation(nodeElement, ns);
            var scale = ParseScale(nodeElement, ns);

            ComposeTransform(node.Transform, matrix, translation, rotations, scale, upAxis);

            foreach (var childNodeElement in nodeElement.Elements(ns + "node"))
            {
                ParseNode(childNodeElement, ns, geometryMap, materialMap, effectMap, cameraMap, upAxis, node, nodeMap);
            }

            foreach (var instanceGeometryElement in nodeElement.Elements(ns + "instance_geometry"))
            {
                ParseInstanceGeometry(instanceGeometryElement, ns, geometryMap, materialMap, effectMap, node, upAxis);
            }

            foreach (var instanceCameraElement in nodeElement.Elements(ns + "instance_camera"))
            {
                ParseInstanceCamera(instanceCameraElement, ns, cameraMap, node);
            }
        }

        private static void ParseMatrixToTransform(Transform transform, Matrix4 matrix)
        {
            transform.Rotation = ConvertMatrixToQuaternion(matrix);
            transform.Translation = new Vector3(new FVector3((float)matrix.m30, (float)matrix.m31, (float)matrix.m32));
            transform.Scaling = new Vector3(1, 1, 1);
        }

        private static Quaternion ConvertMatrixToQuaternion(Matrix4 matrix)
        {
            float trace = (float)(matrix.m00 + matrix.m11 + matrix.m22);
            float x, y, z, w;

            if (trace > 0)
            {
                float s = (float)Math.Sqrt(trace + 1.0);
                w = s * 0.5f;
                s = 0.5f / s;
                x = (float)(matrix.m21 - matrix.m12) * s;
                y = (float)(matrix.m02 - matrix.m20) * s;
                z = (float)(matrix.m10 - matrix.m01) * s;
            }
            else if (matrix.m00 > matrix.m11 && matrix.m00 > matrix.m22)
            {
                float s = (float)Math.Sqrt(1.0 + matrix.m00 - matrix.m11 - matrix.m22);
                x = s * 0.5f;
                s = 0.5f / s;
                y = (float)(matrix.m01 + matrix.m10) * s;
                z = (float)(matrix.m02 + matrix.m20) * s;
                w = (float)(matrix.m21 - matrix.m12) * s;
            }
            else if (matrix.m11 > matrix.m22)
            {
                float s = (float)Math.Sqrt(1.0 + matrix.m11 - matrix.m00 - matrix.m22);
                y = s * 0.5f;
                s = 0.5f / s;
                x = (float)(matrix.m01 + matrix.m10) * s;
                z = (float)(matrix.m12 + matrix.m21) * s;
                w = (float)(matrix.m02 - matrix.m20) * s;
            }
            else
            {
                float s = (float)Math.Sqrt(1.0 + matrix.m22 - matrix.m00 - matrix.m11);
                z = s * 0.5f;
                s = 0.5f / s;
                x = (float)(matrix.m02 + matrix.m20) * s;
                y = (float)(matrix.m12 + matrix.m21) * s;
                w = (float)(matrix.m10 - matrix.m01) * s;
            }

            return new Quaternion(x, y, z, w);
        }

        private static Matrix4? ParseMatrix(XElement nodeElement, XNamespace ns)
        {
            var matrixElement = nodeElement.Element(ns + "matrix");
            if (matrixElement == null)
                return null;

            var values = matrixElement.Value.Trim().Split(new[] { ' ', '\t', '\n', '\r' }, StringSplitOptions.RemoveEmptyEntries);
            if (values.Length < 16)
                return null;

            var m = new float[16];
            for (int i = 0; i < 16; i++)
            {
                if (float.TryParse(values[i], out var val))
                {
                    m[i] = val;
                }
            }

            var fmatrix = new FMatrix4(m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[13], m[14], m[15]);
            var matrix = new Matrix4(fmatrix.m00, fmatrix.m01, fmatrix.m02, fmatrix.m03, fmatrix.m10, fmatrix.m11, fmatrix.m12, fmatrix.m13, fmatrix.m20, fmatrix.m21, fmatrix.m22, fmatrix.m23, fmatrix.m30, fmatrix.m31, fmatrix.m32, fmatrix.m33);

            return matrix;
        }

        private static Vector3? ParseTranslation(XElement nodeElement, XNamespace ns)
        {
            var translateElement = nodeElement.Element(ns + "translate");
            if (translateElement == null)
                return null;

            var values = translateElement.Value.Trim().Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
            if (values.Length < 3)
                return null;

            var x = float.Parse(values[0]);
            var y = float.Parse(values[1]);
            var z = float.Parse(values[2]);

            return new Vector3(x, y, z);
        }

        private static List<Quaternion> ParseRotation(XElement nodeElement, XNamespace ns)
        {
            var rotations = new List<Quaternion>();

            foreach (var rotateElement in nodeElement.Elements(ns + "rotate"))
            {
                var values = rotateElement.Value.Trim().Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
                if (values.Length < 4)
                    continue;

                var axis = new Vector3(float.Parse(values[0]), float.Parse(values[1]), float.Parse(values[2]));
                var angle = float.Parse(values[3]) * (float)Math.PI / 180.0f;
                
                float sinHalfAngle = (float)Math.Sin(angle / 2.0);
                float cosHalfAngle = (float)Math.Cos(angle / 2.0);
                
                Quaternion q = new Quaternion(
                    (float)axis.X * sinHalfAngle,
                    (float)axis.Y * sinHalfAngle,
                    (float)axis.Z * sinHalfAngle,
                    cosHalfAngle
                );
                
                rotations.Add(q);
            }

            return rotations;
        }

        private static Vector3? ParseScale(XElement nodeElement, XNamespace ns)
        {
            var scaleElement = nodeElement.Element(ns + "scale");
            if (scaleElement == null)
                return null;

            var values = scaleElement.Value.Trim().Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
            if (values.Length < 3)
                return null;

            return new Vector3(float.Parse(values[0]), float.Parse(values[1]), float.Parse(values[2]));
        }

        private static void ComposeTransform(Transform transform, Matrix4? matrix, Vector3? translation, List<Quaternion> rotations, Vector3? scale, string upAxis)
        {
            if (matrix.HasValue)
            {
                ParseMatrixToTransform(transform, matrix.Value);
                return;
            }

            Matrix4 finalMatrix = Matrix4.Identity;

            if (scale.HasValue)
            {
                finalMatrix = finalMatrix * Matrix4.Scale(new Vector3(scale.Value.X, scale.Value.Y, scale.Value.Z));
            }

            foreach (var rotation in rotations)
            {
                finalMatrix = finalMatrix * Matrix4.Rotate(rotation);
            }

            if (translation.HasValue)
            {
                var translated = translation.Value;
                if (upAxis == "Z_UP")
                {
                    var temp = translated.Y;
                    translated.Y = -translated.Z;
                    translated.Z = temp;
                }
                finalMatrix = finalMatrix * Matrix4.Translate(translated.X, translated.Y, translated.Z);
            }

            ParseMatrixToTransform(transform, finalMatrix);
        }

        private static void ParseInstanceGeometry(
            XElement instanceGeometryElement, 
            XNamespace ns, 
            Dictionary<string, Mesh> geometryMap,
            Dictionary<string, Shading.Material> materialMap,
            Dictionary<string, Shading.Material> effectMap,
            Node node,
            string upAxis)
        {
            var url = instanceGeometryElement.Attribute("url")?.Value;
            if (string.IsNullOrEmpty(url) || !url.StartsWith("#"))
                return;

            var geometryId = url.Substring(1);
            if (!geometryMap.TryGetValue(geometryId, out var mesh))
                return;

            var meshClone = new Mesh(mesh.Name);
            foreach (var cp in mesh.ControlPoints)
            {
                meshClone.ControlPoints.Add(cp);
            }
            foreach (var poly in mesh.Polygons)
            {
                meshClone.CreatePolygon(poly);
            }
            foreach (var element in mesh.VertexElements)
            {
                meshClone.VertexElements.Add(element);
            }

            var bindMaterial = instanceGeometryElement.Element(ns + "bind_material");
            if (bindMaterial != null)
            {
                var techniqueCommon = bindMaterial.Element(ns + "technique_common");
                if (techniqueCommon != null)
                {
                    foreach (var instanceMaterial in techniqueCommon.Elements(ns + "instance_material"))
                    {
                        var symbol = instanceMaterial.Attribute("symbol")?.Value;
                        var target = instanceMaterial.Attribute("target")?.Value;
                        if (!string.IsNullOrEmpty(symbol) && !string.IsNullOrEmpty(target) && target.StartsWith("#"))
                        {
                            var materialId = target.Substring(1);
                            if (materialMap.TryGetValue(materialId, out var material))
                            {
                                node.Material = material;
                            }
                            else if (effectMap.TryGetValue(materialId, out var effect))
                            {
                                node.Material = effect;
                            }
                        }
                    }
                }
            }

            node.AddEntity(meshClone);
        }

        private static void ParseInstanceCamera(XElement instanceCameraElement, XNamespace ns, Dictionary<string, Camera> cameraMap, Node node)
        {
            var url = instanceCameraElement.Attribute("url")?.Value;
            if (string.IsNullOrEmpty(url) || !url.StartsWith("#"))
                return;

            var cameraId = url.Substring(1);
            if (cameraMap.TryGetValue(cameraId, out var camera))
            {
                node.AddEntity(camera);
            }
        }
    }
}
