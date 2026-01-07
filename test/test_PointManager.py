import pytest

from scripts.PointManager import PointManager
from scripts.shapes.Point import Point


def test_point_manager_init_empty():
  pm = PointManager()
  assert pm.number_of_points() == 0
  assert pm.get_points() == []


def test_point_manager_add_point_and_find():
  pm = PointManager()
  p = Point("A", 1, 2, 3)
  pm.add_point(p)

  assert pm.number_of_points() == 1
  assert pm.find_point_by_name("A") == p
  assert pm.find_point_by_name("B") is None


def test_point_manager_add_duplicate_name_raises():
  pm = PointManager()
  pm.add_point(Point("A", 0, 0))
  with pytest.raises(ValueError):
    pm.add_point(Point("A", 1, 1))


def test_point_manager_add_name_point_increments_pid():
  pm = PointManager()
  name1 = pm.add_name_point(0, 0)
  name2 = pm.add_name_point(1, 1, 1)

  assert name1 == "P1"
  assert name2 == "P2"
  assert pm.number_of_points() == 2


def test_point_manager_add_name_point_pid_not_incremented_on_failure(monkeypatch):
  pm = PointManager()

  # force duplicate by faking find
  def fake_find(_):
    return Point("P1", 0, 0)

  monkeypatch.setattr(pm, "find_point_by_name", fake_find)

  with pytest.raises(ValueError):
    pm.add_name_point(0, 0)

  assert pm.pid == 1


def test_point_manager_remove_point():
  pm = PointManager()
  p = Point("A", 0, 0)
  pm.add_point(p)
  pm.remove_point(p)

  assert pm.number_of_points() == 0


def test_point_manager_export_to_json():
  pm = PointManager()
  pm.add_point(Point("A", 1, 2))
  pm.add_point(Point("B", 3, 4, 5))

  data = pm.export_to_json()
  assert data == [
    {"name": "A", "x": 1.0, "y": 2.0, "z": 0.0},
    {"name": "B", "x": 3.0, "y": 4.0, "z": 5.0},
  ]
