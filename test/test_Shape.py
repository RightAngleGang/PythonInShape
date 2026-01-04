import pytest

from scripts.shapes.Shape import Shape
from scripts.shapes.ShapeType import ShapeType


def test_shapetype_str_is_value():
  assert str(ShapeType.unknown) == "Shape"
  assert str(ShapeType.Square) == "Square"


def test_shape_init_defaults_to_unknown_type():
  s = Shape("S")
  assert s.nom == "S"
  assert s.type == ShapeType.unknown


def test_shape_equality_name_and_type():
  s1 = Shape("S", ShapeType.Polygon)
  s2 = Shape("S", ShapeType.Polygon)
  s3 = Shape("S", ShapeType.Circle)
  s4 = Shape("T", ShapeType.Polygon)

  assert s1 == s2
  assert s1 != s3
  assert s1 != s4
  assert s1 != "not a shape"


def test_shape_area_and_volume_default_zero():
  s = Shape("S")
  assert s.area() == 0.0
  assert s.volume() == 0.0


@pytest.mark.xfail(reason="export_to_json retourne une string littérale '{self.type}' (pas une f-string).")
def test_shape_export_to_json_expected_type_string():
  s = Shape("S", ShapeType.Circle)
  j = s.export_to_json()
  assert j["type"] == "Circle"


def test_shape_export_to_json_current_behavior():
  s = Shape("S", ShapeType.Circle)
  j = s.export_to_json()
  assert j["name"] == "S"
  assert j["type"] == "{self.type}"


def test_shape_is_a_direct_type():
  s = Shape("S", ShapeType.Polygon)
  assert s.is_a(ShapeType.Polygon) is True
  assert s.is_a(ShapeType.Square) is False


def test_shape_is_a_via_parents():
  # Une forme de type Square doit être reconnue comme Polygon via PARENTS
  s = Shape("S", ShapeType.Square)
  assert s.is_a(ShapeType.Square) is True
  assert s.is_a(ShapeType.Polygon) is True
  assert s.is_a(ShapeType.Rectangle) is False
