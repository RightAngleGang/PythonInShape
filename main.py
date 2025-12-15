# main.py
from scripts.Space import Space
import sys
from scripts.menu_function import *
import scripts.menu_points as mp
from scripts.functions.calc_points import euclidean_distance
import scripts.imp_exp as spaceData


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
            print(ValueError)
# --- Actions concrètes ---
ACTIONS_CREATION_POINTS = [
    #("Créer un point", lambda: add_point_shape(sm)),      # si ta fonction ne prend pas sm
    #("Utiliser un point existant", lambda: select_existing_point(sm)),
]

ACTIONS_GESTION_POINTS = [
    ("Ajouter un point", lambda: mp.add_point(sm)),
    ("Déplacer un point", lambda: mp.move_point(sm)),
    ("Translater un point", lambda: mp.translate_point(sm)),
    ("Lister les points", lambda: sm.list_points()),
    ("Renommer un point", lambda: mp.rename_point(sm)),
    ("Supprimer un point", lambda: mp.remove_point(sm)),
]

ACTIONS_SHAPE = [
    ("Ajouter une forme 2D", lambda: add_shape(sm)),
    ("Ajouter une forme 3D", lambda: add_shape3D(sm)),
    ("Lister les formes", lambda: show_shapes(sm)),
    ("Modifier une forme", lambda: edit_shape(sm)),
    #("Supprimer une forme", lambda: sm.get_shape_manager().remove_interactive()),
]

ACTIONS_CALC = [
    ("Calculer la distance entre 2 points", lambda: euclidean_distance(sm)),
]

ACTIONS_DATA = [
    ("Exporter les données de l'espace vers un fichier JSON", lambda: spaceData.export_space_data(sm)),
    ("Importer les données de l'espace depuis un fichier JSON", lambda: spaceData.import_space_data(sm)),
]

ACTIONS_BASIC = [
    ("Gestion des Points ▶", lambda: menu_loop("--- MENU POINTS ---", ACTIONS_GESTION_POINTS)),
    ("Gestion des Formes ▶", lambda: menu_loop("--- MENU FORMES ---", ACTIONS_SHAPE)),
    ("Gestion des données ▶", lambda: menu_loop("--- MENU DONNÉES ---", ACTIONS_DATA)),
    ("Calculs ▶", lambda: menu_loop("--- MENU CALCULS ---", ACTIONS_CALC)),
    ("DEV / ADD POINTS", lambda: add_points(sm)),
]

if __name__ == "__main__":
    menu_loop("=== MENU PRINCIPAL ===", ACTIONS_BASIC)
