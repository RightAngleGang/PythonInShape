import math

import pytest

from scripts.shapes.Point import Point
from scripts.shapes.Sphere import Sphere
from scripts.shapes.Circle import Circle
from scripts.shapes.Cone import Cone


def test_sphere_volume():
  s = Sphere("S", Point("O", 0, 0, 0), 2)
  expected = (4 / 3) * math.pi * (2 ** 3)
  assert math.isclose(s.volume(), expected)


def test_sphere_str_and_export():
  s = Sphere("S", Point("O", 1, 2, 3), 2)
  assert "S (Sphere)" in str(s)
  j = s.export_to_json()
  assert j == {"type": "Sphere", "name": "S", "center": "O", "radius": 2}


def test_circle_normal_is_normalized():
  c = Circle("C", Point("O", 0, 0, 0), 2, (10, 0, 0))
  assert c.normal == (1.0, 0.0, 0.0)


def test_circle_zero_normal_raises():
  with pytest.raises(ValueError):
    Circle("C", Point("O", 0, 0, 0), 1, (0, 0, 0))


def test_circle_area_and_volume_and_export():
  c = Circle("C", Point("O", 0, 0, 0), 3, (0, 0, 5))
  assert math.isclose(c.area(), math.pi * 9)
  assert c.volume() == 0.0

  j = c.export_to_json()
  assert j["type"] == "Circle"
  assert j["name"] == "C"
  assert j["center"] == "O"
  assert j["radius"] == 3
  assert j["normal"] == {"x": 0.0, "y": 0.0, "z": 1.0}


def test_cone_area_and_volume_and_export():
  base = Point("O", 0, 0, 0)
  apex = Point("A", 0, 0, 4)
  cone = Cone("K", base, 3, apex)

  # base area = pi r^2
  base_area = math.pi * 9
  height = 4.0
  slant = math.sqrt(height**2 + 3**2)
  expected_area = base_area + math.pi * 3 * slant
  expected_volume = (1 / 3) * base_area * height

  assert math.isclose(cone.area(), expected_area)
  assert math.isclose(cone.volume(), expected_volume)

  j = cone.export_to_json()
  assert j == {"type": "Cone", "name": "K", "center": "O", "radius": 3, "apex": "A"}
