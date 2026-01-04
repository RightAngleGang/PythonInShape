# ===== Makefile pour projet Python =====
# Usage rapide :
#   make venv install        # crée l'env + installe deps
#   make lint test build     # qualité + tests + artefacts dans dist/
#   make cov                 # tests + coverage (terminal + xml)
#   make cov-html            # tests + coverage + rapport HTML
#   make format              # formate le code
#   make clean distclean     # nettoie

.DEFAULT_GOAL := help

# Détection plateforme
ifeq ($(OS),Windows_NT)
  PY := python
  VENV_BIN := venv/Scripts
else
  PY := python3
  VENV_BIN := venv/bin
endif

PIP      := $(VENV_BIN)/pip
PYTHON   := $(VENV_BIN)/python
PYTEST   := $(VENV_BIN)/pytest
BLACK    := $(VENV_BIN)/black
FLAKE8   := $(VENV_BIN)/flake8

REQ_FILE ?= requirements.txt      # deps runtime (optionnel)
REQ_DEV  ?= requirements-dev.txt  # deps dev (optionnel)

# Coverage
COV_DIR   := htmlcov
COV_XML   := coverage.xml
COV_TERM  := term-missing
# source à mesurer : ajuste si besoin (ex: scripts)
COV_SRC   := scripts

.PHONY: help venv install dev format lint test cov cov-html build run clean distclean ci

help:
	@echo "Cibles disponibles :"
	@echo "  venv         - crée l'environnement virtuel"
	@echo "  install      - installe deps (requirements*.txt si présents)"
	@echo "  dev          - installe outils dev (pytest, black, flake8, build, pytest-cov)"
	@echo "  format       - formate le code (black)"
	@echo "  lint         - vérifie le style (black --check, flake8)"
	@echo "  test         - exécute les tests (pytest)"
	@echo "  cov          - exécute les tests + coverage (terminal + xml)"
	@echo "  cov-html     - exécute les tests + coverage + rapport HTML (./$(COV_DIR)/index.html)"
	@echo "  build        - construit wheel + sdist (dist/)"
	@echo "  run          - lance main.py (si présent)"
	@echo "  clean        - supprime caches Python + artefacts coverage"
	@echo "  distclean    - clean + supprime venv, build, dist, egg-info"
	@echo "  ci           - lint + test + build"

venv:
	@echo "🐍 Création venv…"
	$(PY) -m venv venv
	@echo "✅ venv prêt."

install: venv
	@echo "📦 Upgrade pip/wheel…"
	$(PYTHON) -m pip install --upgrade pip wheel
	@echo "📦 Installation du module 'build'…"
	$(PIP) install build
ifneq ("$(wildcard $(REQ_FILE))","")
	@echo "📦 Installation deps depuis $(REQ_FILE)…"
	$(PIP) install -r $(REQ_FILE)
endif
ifneq ("$(wildcard $(REQ_DEV))","")
	@echo "📦 Installation deps dev depuis $(REQ_DEV)…"
	$(PIP) install -r $(REQ_DEV)
endif
	@echo "✅ Dépendances installées."

dev: venv
	@echo "🛠️  Installation outils dev…"
ifneq ("$(wildcard $(REQ_DEV))","")
	$(PIP) install -r $(REQ_DEV)
else
	$(PIP) install pytest pytest-cov black flake8 build
endif
	@echo "✅ Outils dev prêts."

format:
	@echo "Formatage à définir"

lint:
	@echo "Lint à definir"

test:
	@echo "🧪 Tests (pytest)…"
	$(PYTEST) -q

cov:
	@echo "🧪 Tests + coverage…"
	$(PYTEST) -q --cov=$(COV_SRC) --cov-report=$(COV_TERM) --cov-report=xml:$(COV_XML)

cov-html:
	@echo "🧪 Tests + coverage HTML…"
	$(PYTEST) -q --cov=$(COV_SRC) --cov-report=$(COV_TERM) --cov-report=xml:$(COV_XML) --cov-report=html:$(COV_DIR)
	@echo "✅ Rapport HTML : ./$(COV_DIR)/index.html"

build:
	@echo "📦 Build (wheel + sdist)…"
	$(PYTHON) -m build
	@echo "✅ Artefacts dans ./dist/"

run:
	@echo "▶️  Exécution main.py…"
	# Assure que main.py existe
	@if [ ! -f main.py ]; then \
	    echo "❌ main.py introuvable."; \
	    exit 1; \
	fi
	# Vérifie les dépendances avant d'exécuter
	@if [ -f $(REQ_FILE) ]; then \
	    echo "📦 Vérification des dépendances…"; \
	    $(PIP) install -r $(REQ_FILE); \
	fi
	# Exécute le script principal
	$(PYTHON) main.py

clean:
	@echo "🧼 Nettoyage caches…"
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@find . -name "*.pyc" -delete 2>/dev/null || true
	@rm -rf .coverage $(COV_DIR) $(COV_XML) 2>/dev/null || true

distclean: clean
	@echo "🧨 Nettoyage complet…"
	@rm -rf dist build ./*.egg-info venv

ci: lint test build
	@echo "✅ CI locale OK."
