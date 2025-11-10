# menu.py


import subprocess
import importlib.util

# --- Fonction utilitaire pour exécuter un script Python interne ---
def run_python_function(script_path: str, func_name: str):
    """Charge un fichier Python et exécute la fonction donnée."""
    try:
        # Charger dynamiquement le module depuis son chemin
        spec = importlib.util.spec_from_file_location("dynamic_module", script_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Récupérer la fonction et l’appeler
        func = getattr(module, func_name)
        func()
    except Exception as e:
        print(f"Erreur lors de l’exécution de {func_name} dans {script_path}: {e}")

# --- Liste des actions disponibles ---
ACTIONS = [
    ("Dire bonjour (scripts/hello.py)", "python_func:scripts/hello.py:dire_bonjour"),
    ("Hello (bash script)", "bash scripts/hello.sh"),
]

# --- Fonction d’exécution générique ---
def run(cmd: str):
    if cmd.startswith("python_func:"):
        _, path, func = cmd.split(":", 2)
        run_python_function(path, func)
    else:
        subprocess.run(cmd, shell=True, check=False)

# --- Boucle principale ---
while True:
    print("\n=== Runner ===")
    for i, (label, _) in enumerate(ACTIONS, 1):
        print(f"{i}) {label}")
    print("0) Quitter")
    choice = input("> ")

    if choice == "0":
        break
    try:
        i = int(choice) - 1
        run(ACTIONS[i][1])
    except Exception as e:
        print("Erreur:", e)