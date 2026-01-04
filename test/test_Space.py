import json
import os
import pytest

from scripts.Space import Space
from scripts.shapes.Point import Point
from scripts.shapes.Polygon import Polygon
from scripts.shapes.Circle import Circle
from scripts.shapes.Sphere import Sphere
from scripts.shapes.Cone import Cone


def test_space_init_has_managers():
  space = Space()
  assert space.get_point_manager() is not None
  assert space.get_shape_manager() is not None


def test_space_export_and_import_roundtrip(tmp_path):
  space = Space()

  # points
  pm = space.get_point_manager()
  a = Point("A", 0, 0)
  b = Point("B", 3, 0)
  c = Point("C", 0, 4)
  pm.add_point(a)
  pm.add_point(b)
  pm.add_point(c)

  # shapes
  sm = space.get_shape_manager()
  poly = Polygon("T", points=[a, b, c])
  circ = Circle("C1", a, 2, (0, 0, 1))
  sph = Sphere("S1", b, 1)
  cone = Cone("K1", a, 1, c)

  sm.add_shape(poly)
  sm.add_shape(circ)
  sm.add_shape(sph)
  sm.add_shape(cone)

  # export
  out = tmp_path / "space.json"
  space.export_to_json(out)
  assert out.exists()

  # import
  space2 = Space()
  space2.import_from_json(out)

  pm2 = space2.get_point_manager()
  sm2 = space2.get_shape_manager()

  assert pm2.number_of_points() == 3
  assert sm2.number_of_shapes() == 4

  assert pm2.find_point_by_name("A") is not None
  assert sm2.find_shape_by_name("T") is not None
  assert sm2.find_shape_by_name("C1") is not None
  assert sm2.find_shape_by_name("S1") is not None
  assert sm2.find_shape_by_name("K1") is not None


def test_space_import_unknown_shape_type_without_points_raises(tmp_path):
  bad = {
    "points": [{"name": "A", "x": 0, "y": 0, "z": 0}],
    "shapes": [{"type": "Unknown", "name": "X"}],
  }
  p = tmp_path / "bad.json"
  p.write_text(json.dumps(bad))

  space = Space()
  with pytest.raises(ValueError):
    space.import_from_json(p)
