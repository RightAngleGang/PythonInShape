import pytest
import builtins

from scripts.Space import Space
from scripts.menu_points import (
  add_point, remove_point, move_point,
  rename_point, translate_point, choose_point
)
from scripts.shapes.Point import Point
from scripts.shapes.Circle import Circle


def test_add_point(monkeypatch):
  space = Space()
  monkeypatch.setattr(builtins, "input", lambda _: "1;2;3")

  name = add_point(space)
  assert name == "P1"
  assert space.get_point_manager().find_point_by_name("P1") is not None


def test_remove_point_ok(monkeypatch):
  space = Space()
  pm = space.get_point_manager()
  p = Point("A", 0, 0)
  pm.add_point(p)

  monkeypatch.setattr(builtins, "input", lambda _: "A")
  remove_point(space)

  assert pm.find_point_by_name("A") is None


def test_remove_point_used_as_circle_center_raises(monkeypatch):
  space = Space()
  pm = space.get_point_manager()
  sm = space.get_shape_manager()

  p = Point("O", 0, 0)
  pm.add_point(p)
  c = Circle("C", p, 1, (0, 0, 1))
  sm.add_shape(c)

  monkeypatch.setattr(builtins, "input", lambda _: "O")
  with pytest.raises(ValueError):
    remove_point(space)


def test_move_point(monkeypatch):
  space = Space()
  pm = space.get_point_manager()
  p = Point("A", 1, 1, 1)
  pm.add_point(p)

  inputs = iter(["A", "2;3;4"])
  monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

  move_point(space)
  assert p.as_tuple() == (2.0, 3.0, 4.0)


def test_rename_point(monkeypatch):
  space = Space()
  pm = space.get_point_manager()
  p = Point("A", 0, 0)
  pm.add_point(p)

  inputs = iter(["A", "B"])
  monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

  rename_point(space)
  assert pm.find_point_by_name("B") == p


def test_translate_point(monkeypatch):
  space = Space()
  pm = space.get_point_manager()
  p = Point("A", 1, 1, 1)
  pm.add_point(p)

  inputs = iter(["A", "1;2;3"])
  monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

  translate_point(space)
  assert p.as_tuple() == (2.0, 3.0, 4.0)


def test_choose_point_existing(monkeypatch):
  space = Space()
  pm = space.get_point_manager()
  p = Point("A", 0, 0)
  pm.add_point(p)

  inputs = iter(["1", "A"])
  monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

  out = choose_point(space)
  assert out == p
