import os
import sys

import pytest


@pytest.fixture(scope="session", autouse=True)
def add_project_root_to_syspath():
  """
  Permet d'importer `scripts.*` quand les tests sont lancés depuis la racine.
  Le dossier `test/` est au même niveau que `scripts/`.
  """
  here = os.path.dirname(__file__)
  project_root = os.path.abspath(os.path.join(here, ".."))
  if project_root not in sys.path:
    sys.path.insert(0, project_root)



