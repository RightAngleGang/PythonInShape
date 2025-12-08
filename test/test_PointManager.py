from scripts.Point import Point
from scripts.PointManager import PointManager

def test_add_point():
    pm = PointManager()
    pm.add_point(Point("sqduids", 1, 2))
    assert pm.number_of_points() == 1
    assert pm.find_point_by_name("sqduids").x == 1
    assert pm.find_point_by_name("sqduids").y == 2
    assert f"{pm}" == "[sqduids(1;2)]"
    
def test_remove_point():
    pm = PointManager()
    pm.add_point(Point("sqduids", 1, 2))
    pm.remove_point("sqduids")
    assert pm.number_of_points() == 0
    assert pm.find_point_by_name("sqduids") is None
    assert f"{pm}" == "[]"
    
def test_multiple_points():
    pm = PointManager()
    pm.add_point(Point("point1", 1, 2))
    pm.add_point(Point("point2", 3, 4))
    pm.add_point(Point("point3", 5, 6))
    assert pm.number_of_points() == 3
    assert f"{pm}" == "[point1(1.0;2.0); point2(3.0;4.0); point3(5.0;6.0)]"
    
def test_find_nonexistent_point():
    pm = PointManager()
    pm.add_point(Point("existing", 1, 2))
    assert pm.find_point_by_name("nonexistent") is None
    
