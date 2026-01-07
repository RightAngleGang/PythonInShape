import builtins

from scripts.imp_exp import export_space_data, import_space_data
from scripts.Space import Space


def test_export_space_data_adds_json_extension(monkeypatch):
  space = Space()
  called = {}

  def fake_export(filename):
    called["filename"] = filename

  monkeypatch.setattr(space, "export_to_json", fake_export)
  monkeypatch.setattr(builtins, "input", lambda _: "testfile")

  export_space_data(space)

  assert called["filename"] == "testfile.json"


def test_export_space_data_keeps_json_extension(monkeypatch):
  space = Space()
  called = {}

  monkeypatch.setattr(space, "export_to_json", lambda f: called.setdefault("f", f))
  monkeypatch.setattr(builtins, "input", lambda _: "data.json")

  export_space_data(space)

  assert called["f"] == "data.json"


def test_export_space_data_handles_exception(monkeypatch, capsys):
  space = Space()

  def fail(_):
    raise RuntimeError("boom")

  monkeypatch.setattr(space, "export_to_json", fail)
  monkeypatch.setattr(builtins, "input", lambda _: "x")

  export_space_data(space)
  out = capsys.readouterr().out

  assert "Erreur lors de l'exportation" in out


def test_import_space_data_adds_json_extension(monkeypatch):
  space = Space()
  called = {}

  monkeypatch.setattr(space, "import_from_json", lambda f: called.setdefault("f", f))
  monkeypatch.setattr(builtins, "input", lambda _: "importfile")

  import_space_data(space)

  assert called["f"] == "importfile.json"


def test_import_space_data_handles_exception(monkeypatch, capsys):
  space = Space()

  def fail(_):
    raise RuntimeError("boom")

  monkeypatch.setattr(space, "import_from_json", fail)
  monkeypatch.setattr(builtins, "input", lambda _: "x")

  import_space_data(space)
  out = capsys.readouterr().out

  assert "Erreur lors de l'importation" in out
