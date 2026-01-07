import builtins
import pytest

from scripts.utils import get_coords2, get_coords3, clean_coord


def test_get_coords2_valid(monkeypatch):
  monkeypatch.setattr(builtins, "input", lambda _: "1; 2.5")
  assert get_coords2() == (1.0, 2.5)


def test_get_coords2_invalid_format(monkeypatch):
  monkeypatch.setattr(builtins, "input", lambda _: "1;2;3")
  with pytest.raises(ValueError):
    get_coords2()


def test_get_coords2_invalid_number(monkeypatch):
  monkeypatch.setattr(builtins, "input", lambda _: "a;b")
  with pytest.raises(ValueError):
    get_coords2()


def test_get_coords3_valid(monkeypatch):
  monkeypatch.setattr(builtins, "input", lambda _: "1;2;3")
  assert get_coords3() == (1.0, 2.0, 3.0)


def test_get_coords3_invalid_format(monkeypatch):
  monkeypatch.setattr(builtins, "input", lambda _: "1;2")
  with pytest.raises(ValueError):
    get_coords3()


def test_clean_coord_threshold():
  assert clean_coord(1e-12) == 0.0
  assert clean_coord(-1e-12) == 0.0
  assert clean_coord(1e-6) == 1e-6
