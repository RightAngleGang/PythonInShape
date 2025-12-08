from scripts.Space import Space


def export_space_data(space: Space):
    filename = input("Entrez le nom du fichier pour exporter les données de l'espace (.json) : ")
    filename += ".json" if not filename.endswith(".json") else ""
    try:
        space.export_to_json(filename)
        print(f"Données de l'espace exportées avec succès vers '{filename}'.")
    except Exception as e:
        print(f"Erreur lors de l'exportation des données : {e}")


def import_space_data(space: Space):
    filename = input("Entrez le nom du fichier pour importer les données de l'espace (.json) : ")
    filename += ".json" if not filename.endswith(".json") else ""
    try:
        space.import_from_json(filename)
        print(f"Données de l'espace importées avec succès depuis '{filename}'.")
    except Exception as e:
        print(f"Erreur lors de l'importation des données : {e}")