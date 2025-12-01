import pytest
from scripts.menu_function import get_coords2, add_point, remove_point, move_point, rename_point
from scripts.Space import Space

def test_get_coords2_returns_tuple(monkeypatch):
    # Mock input to return valid coordinates
    inputs = iter(["1;2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    coords = get_coords2()
    assert isinstance(coords, tuple)
    assert coords == (1.0, 2.0)

def test_get_coords2_invalid_input(monkeypatch):
    # Mock input to return invalid coordinates
    inputs = iter(["a;4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(ValueError):
        get_coords2()


def test_add_point():
    sm = Space()
    monkeypatch.setattr("builtins.input", lambda _: "PointA")
    monkeypatch.setattr("scripts.menu_function.get_coords2", lambda: (3.0, 4.0))
    add_point(sm)
    assert f"{sm.get_point_manager()}" == ""
    

# def test_add_point_duplicate_name():

# def test_remove_point_removes_existing():

# def test_remove_point_nonexistent():

# def test_move_point_changes_coords():

# def test_move_point_nonexistent():

# def test_rename_point_changes_name():

# def test_rename_point_to_existing_name():
