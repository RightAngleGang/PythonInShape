import pytest
from pathlib import Path

import scripts.three_visualize as tv
from scripts.Space import Space


def test_is_port_open_false():
  assert tv._is_port_open("127.0.0.1", 65500) is False


def test_show_data_viewer_not_found(monkeypatch):
  space = Space()

  monkeypatch.setattr(Path, "cwd", lambda: Path("/nonexistent"))

  with pytest.raises(FileNotFoundError):
    tv.show_data(space)


def test_show_data_export_and_open_browser(monkeypatch, tmp_path):
  space = Space()

  # fake project root with viewer
  viewer = tmp_path / "three-json-viewer"
  public = viewer / "public"
  public.mkdir(parents=True)

  monkeypatch.setattr(Path, "cwd", lambda: tmp_path)

  # export_to_json mock
  exported = {}

  def fake_export(path):
    exported["path"] = path

  monkeypatch.setattr(space, "export_to_json", fake_export)

  # simulate server already running
  monkeypatch.setattr(tv, "_is_port_open", lambda h, p, timeout=0.25: True)

  # prevent browser open
  opened = {}
  monkeypatch.setattr(tv.webbrowser, "open", lambda url: opened.setdefault("url", url))

  tv.show_data(space)

  assert "data.json" in exported["path"]
  assert opened["url"].startswith("http://localhost")


def test_show_data_starts_vite_if_not_running(monkeypatch, tmp_path):
  space = Space()

  viewer = tmp_path / "three-json-viewer"
  (viewer / "public").mkdir(parents=True)

  monkeypatch.setattr(Path, "cwd", lambda: tmp_path)

  monkeypatch.setattr(space, "export_to_json", lambda _: None)

  # first call: port closed, then open
  calls = {"n": 0}

  def fake_port(host, port, timeout=0.25):
    calls["n"] += 1
    return calls["n"] > 2

  monkeypatch.setattr(tv, "_is_port_open", fake_port)

  class DummyProc:
    stdout = None

  monkeypatch.setattr(tv.subprocess, "Popen", lambda *a, **k: DummyProc())
  monkeypatch.setattr(tv.webbrowser, "open", lambda _: None)

  tv.show_data(space)
