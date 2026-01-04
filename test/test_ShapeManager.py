from scripts.ShapeManager import ShapeManager
from scripts.shapes.Shape import Shape
from scripts.shapes.ShapeType import ShapeType


def test_shape_manager_init_empty():
  sm = ShapeManager()
  assert sm.number_of_shapes() == 0
  assert sm.get_shapes() == []


def test_shape_manager_add_and_find_shape():
  sm = ShapeManager()
  s = Shape("S", ShapeType.Circle)
  sm.add_shape(s)

  assert sm.number_of_shapes() == 1
  assert sm.find_shape_by_name("S") == s
  assert sm.find_shape_by_name("X") is None


def test_shape_manager_remove_shape():
  sm = ShapeManager()
  s = Shape("S")
  sm.add_shape(s)
  sm.remove_shape(s)

  assert sm.number_of_shapes() == 0


def test_shape_manager_export_to_json():
  sm = ShapeManager()
  s1 = Shape("A")
  s2 = Shape("B", ShapeType.Polygon)
  sm.add_shape(s1)
  sm.add_shape(s2)

  data = sm.export_to_json()
  assert data == [s1.export_to_json(), s2.export_to_json()]
