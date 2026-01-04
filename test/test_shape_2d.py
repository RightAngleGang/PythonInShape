import builtins
import math
import pytest

from scripts.Space import Space
from scripts.shapes.Point import Point
from scripts.shapes.Polygon import Polygon
from scripts.shapes.Circle import Circle
from scripts.functions.shape_2d import (
  add_segment, add_triangle, add_circle,
  add_polygon, add_carre, add_rectangle
)


def test_add_segment_2d(monkeypatch):
  space = Space()
  pm = space.get_point_manager()
  p1 = Point("A", 0, 0)
  p2 = Point("B", 1, 0)
  pm.add_point(p1)
  pm.add_point(p2)

  seq = iter([p1, p2])
  monkeypatch.setattr(
    "scripts.functions.shape_2d.choose_point",
    lambda *a, **k: next(seq)
  )

  poly = add_segment(space, "S")
  assert isinstance(poly, Polygon)
  assert len(poly.points) == 2


def test_add_triangle_2d(monkeypatch):
  space = Space()
  pm = space.get_point_manager()
  pts = [Point("A", 0, 0), Point("B", 1, 0), Point("C", 0, 1)]
  for p in pts:
    pm.add_point(p)

  seq = iter(pts)
  monkeypatch.setattr(
    "scripts.functions.shape_2d.choose_point",
    lambda *a, **k: next(seq)
  )

  poly = add_triangle(space, "T")
  assert isinstance(poly, Polygon)
  assert len(poly.points) == 3


def test_add_circle_default_orientation(monkeypatch):
  space = Space()

  inputs = iter([
    "0;0;0",   # center
    "2",       # radius
    "1"        # mode = XY
  ])
  monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

  c = add_circle("C", space)
  assert isinstance(c, Circle)
  assert math.isclose(c.radius, 2.0)
  assert c.normal == (0.0, 0.0, 1.0)


def test_add_polygon_3d_from_2d_coords(monkeypatch):
  space = Space()

  inputs = iter([
    "3",          # nb points
    "0;0",        # p0 2D
    "1;0",        # p1 2D
    "0;1",        # p2 2D
    "0;0;0",      # origin 3D
    "0", "0", "1" # normal
  ])
  monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

  poly = add_polygon("P", space)
  assert isinstance(poly, Polygon)
  assert len(poly.points) == 3


def test_add_polygon_invalid_normal_raises(monkeypatch):
  space = Space()

  inputs = iter([
    "3",
    "0;0",
    "1;0",
    "0;1",
    "0;0;0",
    "0", "0", "0"  # normal nul
  ])
  monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

  with pytest.raises(ValueError):
    add_polygon("P", space)


def test_add_carre(monkeypatch):
  space = Space()

  inputs = iter([
    "0;0;0",  # origin
    "2",      # length
    "0",      # theta
    "0"       # phi
  ])
  monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

  poly = add_carre(space, "Q")
  assert isinstance(poly, Polygon)
  assert len(poly.points) == 4


def test_add_rectangle(monkeypatch):
  space = Space()

  inputs = iter([
    "0;0;0",  # origin
    "3",      # length
    "2",      # width
    "0",      # theta
    "0"       # phi
  ])
  monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

  poly = add_rectangle(space, "R")
  assert isinstance(poly, Polygon)
  assert len(poly.points) == 4
