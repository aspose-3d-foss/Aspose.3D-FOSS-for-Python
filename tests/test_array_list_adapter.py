import unittest

from aspose.threed.entities import VertexElementTemplate
from aspose.threed.entities.VertexElementDoublesTemplate import VertexElementDoublesTemplate
from aspose.threed.entities.VertexElementIntsTemplate import VertexElementIntsTemplate


class ArrayListAdapterTests(unittest.TestCase):
    def test_array_list_adapter_float(self):
        element = VertexElementTemplate[float]()
        element.set_data([1.0, 2.0, 3.0, 4.0])

        data = element.data
        self.assertEqual(4, len(data))
        self.assertEqual(1.0, data[0])
        self.assertEqual(2.0, data[1])
        self.assertEqual(3.0, data[2])
        self.assertEqual(4.0, data[3])

    def test_array_list_adapter_double(self):
        element = VertexElementDoublesTemplate()
        element.set_data([1.0, 2.0, 3.0, 4.0])

        data = element.data
        self.assertEqual(4, len(data))
        self.assertEqual(1.0, data[0])
        self.assertEqual(2.0, data[1])
        self.assertEqual(3.0, data[2])
        self.assertEqual(4.0, data[3])

    def test_array_list_adapter_int(self):
        element = VertexElementIntsTemplate()
        element.set_data([1, 2, 3, 4])

        data = element.data
        self.assertEqual(4, len(data))
        self.assertEqual(1, data[0])
        self.assertEqual(2, data[1])
        self.assertEqual(3, data[2])
        self.assertEqual(4, data[3])

    def test_array_list_adapter_modify(self):
        element = VertexElementTemplate[float]()
        element.set_data([1.0, 2.0, 3.0, 4.0])

        data = element.data
        data[1] = 10.0
        self.assertEqual(10.0, data[1])
        self.assertEqual(10.0, element.data[1])

    def test_array_list_adapter_add(self):
        element = VertexElementTemplate[float]()
        element.data.add(1.0)
        element.data.add(2.0)
        element.data.add(3.0)

        self.assertEqual(3, len(element.data))
        self.assertEqual(1.0, element.data[0])
        self.assertEqual(2.0, element.data[1])
        self.assertEqual(3.0, element.data[2])

    def test_array_list_adapter_contains(self):
        element = VertexElementTemplate[float]()
        element.set_data([1.0, 2.0, 3.0, 4.0])

        self.assertTrue(element.data.contains(2.0))
        self.assertFalse(element.data.contains(5.0))

    def test_array_list_adapter_remove(self):
        element = VertexElementTemplate[float]()
        element.set_data([1.0, 2.0, 3.0, 4.0])

        result = element.data.remove(2.0)
        self.assertTrue(result)
        self.assertEqual(3, len(element.data))
        self.assertFalse(element.data.contains(2.0))

    def test_array_list_adapter_clear(self):
        element = VertexElementTemplate[float]()
        element.set_data([1.0, 2.0, 3.0, 4.0])

        element.data.clear()
        self.assertEqual(0, len(element.data))

    def test_array_list_adapter_index_of(self):
        element = VertexElementTemplate[float]()
        element.set_data([1.0, 2.0, 3.0, 4.0])

        self.assertEqual(0, element.data.index_of(1.0))
        self.assertEqual(2, element.data.index_of(3.0))
        self.assertEqual(-1, element.data.index_of(10.0))

    def test_array_list_adapter_insert(self):
        element = VertexElementTemplate[float]()
        element.set_data([1.0, 3.0, 4.0])

        element.data.insert(1, 2.0)
        self.assertEqual(4, len(element.data))
        self.assertEqual(2.0, element.data[1])

    def test_array_list_adapter_remove_at(self):
        element = VertexElementTemplate[float]()
        element.set_data([1.0, 2.0, 3.0, 4.0])

        element.data.remove_at(1)
        self.assertEqual(3, len(element.data))
        self.assertFalse(element.data.contains(2.0))

    def test_array_list_adapter_copy_to(self):
        element = VertexElementTemplate[float]()
        element.set_data([1.0, 2.0, 3.0, 4.0])

        array = [0.0] * 4
        element.data.copy_to(array)
        self.assertEqual(1.0, array[0])
        self.assertEqual(2.0, array[1])
        self.assertEqual(3.0, array[2])
        self.assertEqual(4.0, array[3])

    def test_array_list_adapter_to_array(self):
        element = VertexElementTemplate[float]()
        element.set_data([1.0, 2.0, 3.0, 4.0])

        arr = element.data.to_array()
        self.assertEqual(4, len(arr))
        self.assertEqual(1.0, arr[0])
        self.assertEqual(2.0, arr[1])
        self.assertEqual(3.0, arr[2])
        self.assertEqual(4.0, arr[3])

    def test_array_list_adapter_add_range(self):
        element = VertexElementTemplate[float]()
        element.data.add_range([1.0, 2.0, 3.0, 4.0])

        self.assertEqual(4, len(element.data))
        self.assertEqual(1.0, element.data[0])
        self.assertEqual(2.0, element.data[1])
        self.assertEqual(3.0, element.data[2])
        self.assertEqual(4.0, element.data[3])

    def test_array_list_adapter_iterate(self):
        element = VertexElementTemplate[float]()
        element.set_data([1.0, 2.0, 3.0, 4.0])

        result = list(element.data)
        self.assertEqual([1.0, 2.0, 3.0, 4.0], result)


if __name__ == '__main__':
    unittest.main()
