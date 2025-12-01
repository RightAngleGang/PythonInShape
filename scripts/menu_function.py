from scripts.Point import Point
from scripts.Polygon import Polygon
from scripts.Space import Space

def add_points(space: Space):
    space.get_point_manager().add_name_point(1.2, 3.4)
    space.get_point_manager().add_name_point(5.6, 7.8)
    space.get_point_manager().add_name_point(9.0, 1.2)
    space.get_point_manager().add_name_point(3.4, 5.6)
    space.get_point_manager().add_name_point(7.8, 9.0)
    
def add_point(space: Space):
    tmpStr = str(input("Points format : x.0;y.0 : ")).split(";")
    space.get_point_manager().add_name_point(tmpStr[0], tmpStr[1])

def add_shape(space: Space):
    tmpStr = str(input("Shape name : "))
    polygon = Polygon(tmpStr)
    nb_of_points = int(input("Number of points : "))
    for i in range(nb_of_points):
        point_input = str(input(f"Point tmp{i+1} format : x.0;y.0 : ")).split(";")
        tmpPoint = Point(f"tmp{i+1}", float(point_input[0]), float(point_input[1]))
        space.get_point_manager().add_point(tmpPoint)
        polygon.add_point(tmpPoint)
    space.get_shape_manager().add_shape(polygon)
    print(f"Shape {tmpStr} created with {nb_of_points} points.", end="\n\t")

def show_shapes(space: Space):
    shapes = space.get_shape_manager().get_shapes()
    if not shapes:
        print("No shapes available.")
        return
    for shape in shapes:
        print(f"Shape: {shape.nom}")
        for point in shape.points:
            print(f"  Point {point.nom}: ({point.x}, {point.y})")

def euclidean_distance(space : Space):
    tmpP1 = str(input("Nom du 1er point : "))  
    tmpP2 = str(input("Nom du 2eme point : "))  
    p1 = space.get_point_manager().find_point_by_name(tmpP1)
    p2 = space.get_point_manager().find_point_by_name(tmpP2)
    # Vérifications
    if p1 is None:
        print(f"Point '{tmpP1}' introuvable dans l'espace. Impossible de calculer la distance.")
        return
    if p2 is None:
        print(f"Point '{tmpP2}' introuvable dans l'espace. Impossible de calculer la distance.")
        return

    # Calcul de la distance
    print(f"La distance entre les points est : {p1.distance_to(p2)}")

def export_space_data(space: Space):
    filename = input("Entrez le nom du fichier pour exporter les données de l'espace (.json) : ")
    try:
        space.export_to_json(filename)
        print(f"Données de l'espace exportées avec succès vers '{filename}'.")
    except Exception as e:
        print(f"Erreur lors de l'exportation des données : {e}")

def import_space_data(space: Space):
    filename = input("Entrez le nom du fichier pour importer les données de l'espace (.json) : ")
    try:
        space.import_from_json(filename)
        print(f"Données de l'espace importées avec succès depuis '{filename}'.")
    except Exception as e:
        print(f"Erreur lors de l'importation des données : {e}")