import pytest
import builtins

from scripts.Space import Space
from scripts.menu_calcul import euclidean_distance, get_area, get_volume
from scripts.shapes.Point import Point
from scripts.shapes.Circle import Circle


def test_euclidean_distance_ok(monkeypatch):
  space = Space()
  pm = space.get_point_manager()
  pm.add_point(Point("A", 0, 0))
  pm.add_point(Point("B", 3, 4))

  inputs = iter(["A", "B"])
  monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

  d = euclidean_distance(space)
  assert d == 5.0


def test_euclidean_distance_point_not_found(monkeypatch):
  space = Space()
  monkeypatch.setattr(builtins, "input", lambda _: "X")

  with pytest.raises(ValueError):
    euclidean_distance(space)


def test_get_area_ok(monkeypatch, capsys):
  space = Space()
  pm = space.get_point_manager()
  sm = space.get_shape_manager()

  c = Circle("C", Point("O", 0, 0), 2, (0, 0, 1))
  pm.add_point(c.point)
  sm.add_shape(c)

  monkeypatch.setattr(builtins, "input", lambda _: "C")
  get_area(space)

  out = capsys.readouterr().out
  assert "L'aire de la forme 'C'" in out


def test_get_area_no_shapes():
  space = Space()
  with pytest.raises(ValueError):
    get_area(space)


def test_get_volume_ok(monkeypatch, capsys):
  space = Space()
  pm = space.get_point_manager()
  sm = space.get_shape_manager()

  c = Circle("C", Point("O", 0, 0), 2, (0, 0, 1))
  pm.add_point(c.point)
  sm.add_shape(c)

  monkeypatch.setattr(builtins, "input", lambda _: "C")
  get_volume(space)

  out = capsys.readouterr().out
  assert "Le volume de la forme 'C'" in out
