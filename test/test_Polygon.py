import math

import pytest

from scripts.shapes.Point import Point
from scripts.shapes.Polygon import Polygon
from scripts.shapes.ShapeType import ShapeType


def test_polygon_init_defaults_to_empty_points_and_polygon_type():
  poly = Polygon("P")
  assert poly.nom == "P"
  assert poly.type == ShapeType.Polygon
  assert poly.points == []


def test_polygon_supertype_segment_triangle_polygon():
  p1 = Point("A", 0, 0)
  p2 = Point("B", 1, 0)
  p3 = Point("C", 0, 1)

  seg = Polygon("S", points=[p1, p2])
  tri = Polygon("T", points=[p1, p2, p3])
  many = Polygon("M", points=[p1, p2, p3, Point("D", 1, 1), Point("E", 2, 0)])

  assert str(seg).startswith("S (Segment)")
  assert str(tri).startswith("T (Triangle)")
  assert str(many).startswith("M (Polygon)")


def test_polygon_square_detection_non_axis_aligned():
  # Carré tourné de 45° : (0,1), (1,0), (0,-1), (-1,0)
  pts = [
    Point("A", 0, 1),
    Point("B", 1, 0),
    Point("C", 0, -1),
    Point("D", -1, 0),
  ]
  sq = Polygon("Q", points=pts)
  assert "Square" in str(sq)


def test_polygon_rectangle_detection_axis_aligned():
  pts = [
    Point("A", 0, 0),
    Point("B", 3, 0),
    Point("C", 3, 2),
    Point("D", 0, 2),
  ]
  rect = Polygon("R", points=pts)
  assert "Rectangle" in str(rect)


def test_polygon_add_point_and_remove_point():
  a = Point("A", 0, 0)
  b = Point("B", 1, 0)
  c = Point("C", 0, 1)
  poly = Polygon("P", points=[a, b])

  poly.add_point(c)
  assert c in poly.points

  with pytest.raises(ValueError):
    poly.add_point(c)

  poly.remove_point(c)
  assert c not in poly.points

  with pytest.raises(ValueError):
    poly.remove_point(c)


def test_polygon_eq_is_order_insensitive():
  a = Point("A", 0, 0)
  b = Point("B", 1, 0)
  c = Point("C", 0, 1)

  p1 = Polygon("P1", points=[a, b, c])
  p2 = Polygon("P2", points=[c, a, b])
  p3 = Polygon("P3", points=[a, b])

  assert p1 == p2
  assert p1 != p3
  assert p1 != "not a polygon"


def test_polygon_perimeter_edge_cases():
  a = Point("A", 0, 0)
  b = Point("B", 1, 0)

  p0 = Polygon("P0", points=[])
  p1 = Polygon("P1", points=[a])
  p2 = Polygon("P2", points=[a, b])

  assert p0.perimeter() == 0.0
  assert p1.perimeter() == 0.0
  # segment fermé: A->B->A
  assert math.isclose(p2.perimeter(), 2.0)


def test_polygon_area_triangle_uses_cross_product_2d():
  a = Point("A", 0, 0)
  b = Point("B", 4, 0)
  c = Point("C", 0, 3)
  tri = Polygon("T", points=[a, b, c])
  assert math.isclose(tri.area(), 6.0)


def test_polygon_area_triangle_uses_cross_product_3d():
  # Triangle sur plan z=5 : aire doit être identique à la projection 2D
  a = Point("A", 0, 0, 5)
  b = Point("B", 4, 0, 5)
  c = Point("C", 0, 3, 5)
  tri = Polygon("T", points=[a, b, c])
  assert math.isclose(tri.area(), 6.0)


def test_polygon_area_square_and_rectangle():
  # Carré 2x2
  sq = Polygon("Q", points=[
    Point("A", 0, 0),
    Point("B", 2, 0),
    Point("C", 2, 2),
    Point("D", 0, 2),
  ])
  assert math.isclose(sq.area(), 4.0)

  # Rectangle 3x2
  rect = Polygon("R", points=[
    Point("A", 0, 0),
    Point("B", 3, 0),
    Point("C", 3, 2),
    Point("D", 0, 2),
  ])
  assert math.isclose(rect.area(), 6.0)


def test_polygon_area_shoelace_general_polygon():
  # Pentagone simple (non auto-intersectant)
  pts = [
    Point("A", 0, 0),
    Point("B", 2, 0),
    Point("C", 3, 1),
    Point("D", 1, 3),
    Point("E", 0, 2),
  ]
  poly = Polygon("P", points=pts)

  # Shoelace calculé à la main / attendu : 6.0
  assert math.isclose(poly.area(), 6.0)


def test_polygon_export_to_json_contains_names_and_subtype_enum():
  pts = [
    Point("A", 0, 0),
    Point("B", 3, 0),
    Point("C", 3, 2),
    Point("D", 0, 2),
  ]
  rect = Polygon("R", points=pts)
  j = rect.export_to_json()

  assert j["type"] == "Polygon"
  assert j["name"] == "R"
  # subtype = self.type (toujours Polygon dans ce code)
  assert j["subtype"] == ShapeType.Polygon
  assert j["points"] == ["A", "B", "C", "D"]

