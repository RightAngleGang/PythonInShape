# main.py
from scripts.Space import Space
import sys
from scripts.menu_function import *

sm = Space()

# --- Boucle générique de menu ---
def menu_loop(title: str, actions: list[tuple[str, callable]]):
    while True:
        print(f"\n{title}")
        for i, (label, _) in enumerate(actions, 1):
            print(f"{i}) {label}")
        print("0) Retour" if title != "=== MENU PRINCIPAL ===" else "0) Quitter")

        choice = input("> ").strip()
        if choice == "0":
            if title == "=== MENU PRINCIPAL ===":
                sys.exit(0)
            return
        try:
            idx = int(choice) - 1
            actions[idx][1]()  # exécute la fonction liée
        except (ValueError, IndexError):
            print("Entrée invalide.")

# --- Actions concrètes ---
ACTIONS_CREATION_POINTS = [
    #("Créer un point", lambda: add_point_shape(sm)),      # si ta fonction ne prend pas sm
    #("Utiliser un point existant", lambda: select_existing_point(sm)),
]

ACTIONS_SHAPE = [
    ("Ajouter un polygone", lambda: add_shape(sm)),
    ("Lister les polygones", lambda: show_shapes(sm)),
    #("Supprimer un polygone", lambda: sm.get_shape_manager().remove_polygon_interactive()),
]

ACTIONS_BASIC = [
    ("Ajouter un point", lambda: add_point(sm)),
    ("Lister les points", lambda: sm.list_points()),
   #("Supprimer un point", lambda: sm.remove_point_interactive()),
    ("Créer / choisir un point", lambda: menu_loop("--- MENU POINTS ---", ACTIONS_CREATION_POINTS)),
    #("Afficher les données de l'espace", lambda: display_space_data(sm)),
    ("Actions de Polygones ▶", lambda: menu_loop("--- MENU POLYGONES ---", ACTIONS_SHAPE)),
]

if __name__ == "__main__":
    menu_loop("=== MENU PRINCIPAL ===", ACTIONS_BASIC)
