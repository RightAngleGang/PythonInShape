import builtins
import math
import pytest

from scripts.Space import Space
from scripts.shapes.Point import Point
from scripts.shapes.Polygon import Polygon
from scripts.shapes.Sphere import Sphere
from scripts.shapes.Cone import Cone
from scripts.functions.shape_3d import (
  add_cube, add_pave_droit, add_sphere,
  add_pyramide, add_cone
)


def test_add_cube(monkeypatch):
  space = Space()

  inputs = iter([
    "0;0;0",  # origin
    "1",      # edge length
    "0",      # azimut
    "0"       # elevation
  ])
  monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

  poly = add_cube(space, "C")
  assert isinstance(poly, Polygon)
  assert len(poly.points) == 8


def test_add_pave_droit(monkeypatch):
  space = Space()

  inputs = iter([
    "0;0;0",
    "2", "3", "4",  # L W H
    "0", "0"        # azimut, elevation
  ])
  monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

  poly = add_pave_droit(space, "B")
  assert isinstance(poly, Polygon)
  assert len(poly.points) == 8


def test_add_sphere(monkeypatch):
  space = Space()
  pm = space.get_point_manager()
  center = Point("O", 0, 0, 0)
  pm.add_point(center)

  monkeypatch.setattr(
    "scripts.functions.shape_3d.choose_point",
    lambda *a, **k: center
  )
  monkeypatch.setattr(builtins, "input", lambda _: "2")

  s = add_sphere(space, "S")
  assert isinstance(s, Sphere)
  assert s.radius == 2.0
  assert s.point == center


def test_add_pyramide(monkeypatch):
  space = Space()

  inputs = iter([
    "0;0;0",  # origin
    "2",      # base side
    "3",      # height
    "0",      # azimut
    "0"       # elevation
  ])
  monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

  poly = add_pyramide(space, "P")
  assert isinstance(poly, Polygon)
  assert len(poly.points) == 5  # 4 base + apex


def test_add_cone(monkeypatch):
  space = Space()

  inputs = iter([
    "0;0;0",  # base center
    "2",      # radius
    "3",      # height
    "0",      # azimut
    "0"       # elevation
  ])
  monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

  cone = add_cone(space, "K")
  assert isinstance(cone, Cone)
  assert math.isclose(cone.radius, 2.0)
