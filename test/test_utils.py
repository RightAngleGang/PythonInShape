import pytest
from scripts.utils import get_coords2

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
