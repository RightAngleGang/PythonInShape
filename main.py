from scripts.PointManager import SpaceManager
import sys

sm = SpaceManager()

ACTIONS = [
    ("Ajouter un point", lambda: sm.add_point_interactive()),
    ("Lister les points", lambda: sm.list_points()),
    ("Supprimer un point", lambda: sm.remove_point_interactive()),
]
while True:
    print("\n=== MENU POINTS (mémoire) ===")
    for i, (label, _) in enumerate(ACTIONS, 1):
        print(f"{i}) {label}")
    print("0) Quitter")
    choice = input("> ").strip()
    if choice == "0":
        sys.exit(0)
    try:
        i = int(choice) - 1
        ACTIONS[i][1]()  # exécute la fonction liée
    except (ValueError, IndexError):
        print("Entrée invalide.")
