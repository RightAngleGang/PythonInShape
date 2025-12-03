import pytest
from scripts.menu_points import add_point, remove_point, move_point, rename_point
from scripts.Space import Space
from scripts.Point import Point



def test_add_point(monkeypatch):
    sm = Space()
    monkeypatch.setattr("builtins.input", lambda _: "3; 4")
    add_point(sm)
    assert f"{sm.get_point_manager()}" == "" # à Compléter
   
def test_remove_point_removes_existing(monkeypatch):
    sm = Space()
    pt = Point("PointA", 1.0, 2.0)
    sm.get_point_manager().add_point(pt)
    monkeypatch.setattr("builtins.input", lambda _: "PointA")
    remove_point(sm)
    assert sm.get_point_manager().find_point_by_name("PointA") is None

def test_remove_point_nonexistent(monkeypatch):
    sm = Space()
    monkeypatch.setattr("builtins.input", lambda _: "NonExistentPoint")
    with pytest.raises(ValueError):
        remove_point(sm)

def test_move_point_changes_coords(monkeypatch):
    sm = Space()
    pt = Point("PointA", 1.0, 2.0)
    sm.get_point_manager().add_point(pt)
    inputs = iter(["PointA", "5;6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    move_point(sm)
    assert pt.x == 5.0
    assert pt.y == 6.0

def test_move_point_nonexistent(monkeypatch):
    sm = Space()
    inputs = iter(["NonExistentPoint", "5;6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert sm.get_point_manager().find_point_by_name("NonExistentPoint") is None
    with pytest.raises(ValueError):
        move_point(sm)
        

def test_rename_point_nonexistent(monkeypatch):
    sm = Space()
    inputs = iter(["NonExistentPoint", "NouveauNom"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert sm.get_point_manager().find_point_by_name("NonExistentPoint") is None
    with pytest.raises(ValueError):
        rename_point(sm)
    

def test_rename_point_changes_name(monkeypatch):
    sm = Space()
    pt = Point("PointA", 1.0, 2.0)
    sm.get_point_manager().add_point(pt)
    inputs = iter(["PointA", "PointB"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    rename_point(sm)
    assert sm.get_point_manager().find_point_by_name("PointB") is not None
    assert sm.get_point_manager().find_point_by_name("PointA") is None
    assert pt.nom == "PointB"

def test_rename_point_to_existing_name(monkeypatch):
    sm = Space()
    pt1 = Point("PointA", 1.0, 2.0)
    pt2 = Point("PointB", 3.0, 4.0)
    sm.get_point_manager().add_point(pt1)
    sm.get_point_manager().add_point(pt2)
    inputs = iter(["PointA", "PointB"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(ValueError):
        rename_point(sm)
