# main.py
from scripts.Space import Space
import sys
import scripts.menu_function as mf
import scripts.menu_points as mp
import scripts.menu_calcul as mc
import scripts.imp_exp as spaceData
import scripts.three_visualize as threeViz


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
    ("Ajouter une forme 2D", lambda: mf.add_shape(sm)),
    ("Ajouter une forme 3D", lambda: mf.add_shape3D(sm)),
    ("Lister les formes", lambda: mf.show_shapes(sm)),
    ("Modifier une forme", lambda: mf.edit_shape(sm)),
    ("Scale une forme", lambda: mf.scale_shape(sm)),
    ("Déplacer une forme", lambda: mf.move_shape(sm)),
    #("Supprimer une forme", lambda: sm.get_shape_manager().remove_interactive()),
]

ACTIONS_CALC = [
    ("Calculer la distance entre 2 points", lambda: euclidean_distance(sm)),
    ("Calculer le périmètre d'une forme 2D", lambda: mc.get_perimeter(sm)),
    ("Calculer l'aire d'une forme 2D", lambda: mc.get_area(sm)),
    ("Calculer le volume d'une forme 3D", lambda: mc.get_volume(sm)),
]

ACTIONS_DATA = [
    ("Exporter les données de l'espace vers un fichier JSON", lambda: spaceData.export_space_data(sm)),
    ("Importer les données de l'espace depuis un fichier JSON", lambda: spaceData.import_space_data(sm)),
    ("Afficher les données dans three.js", lambda: threeViz.show_data(sm)),
]

ACTIONS_BASIC = [
    ("Gestion des Points ▶", lambda: menu_loop("--- MENU POINTS ---", ACTIONS_GESTION_POINTS)),
    ("Gestion des Formes ▶", lambda: menu_loop("--- MENU FORMES ---", ACTIONS_SHAPE)),
    ("Gestion des données ▶", lambda: menu_loop("--- MENU DONNÉES ---", ACTIONS_DATA)),
    ("Calculs ▶", lambda: menu_loop("--- MENU CALCULS ---", ACTIONS_CALC)),
    ("DEV / ADD POINTS", lambda: mf.add_points(sm)),
]

if __name__ == "__main__":
    menu_loop("=== MENU PRINCIPAL ===", ACTIONS_BASIC)
