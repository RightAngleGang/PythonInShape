import math

import pytest

from scripts.shapes.Point import Point


def test_point_init_casts_to_float_and_default_z():
  p = Point("A", 1, "2.5")
  assert p.nom == "A"
  assert isinstance(p.x, float)
  assert isinstance(p.y, float)
  assert isinstance(p.z, float)
  assert p.as_tuple() == (1.0, 2.5, 0.0)


def test_point_str_format_3_decimals():
  p = Point("A", 1, 2.34567, 3.0)
  assert str(p) == "A(1.000;2.346;3.000)"


def test_point_equality_compares_coordinates_only():
  p1 = Point("A", 1, 2, 3)
  p2 = Point("B", 1, 2, 3)
  p3 = Point("C", 1, 2, 4)

  assert p1 == p2
  assert not (p1 == p3)
  assert not (p1 == "not a point")


def test_point_translate_updates_coordinates():
  p = Point("A", 1, 2, 3)
  p.translate(0.5, -2, 10)
  assert p.as_tuple() == (1.5, 0.0, 13.0)

  p.translate(1, 1)
  assert p.as_tuple() == (2.5, 1.0, 13.0)


def test_point_distance_to_2d():
  p1 = Point("A", 0, 0)
  p2 = Point("B", 3, 4)
  assert math.isclose(p1.distance_to(p2), 5.0)


def test_point_distance_to_3d():
  p1 = Point("A", 1, 2, 3)
  p2 = Point("B", 4, 6, 3)
  assert math.isclose(p1.distance_to(p2), 5.0)
