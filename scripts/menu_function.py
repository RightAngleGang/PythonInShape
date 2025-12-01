from scripts.Point import Point
from scripts.Polygon import Polygon
from scripts.Circle import Circle
from scripts.Space import Space
from scripts.Shape import Shape
import math

def add_points(space: Space):
    space.get_point_manager().add_name_point(1.2, 3.4)
    space.get_point_manager().add_name_point(5.6, 7.8)
    space.get_point_manager().add_name_point(9.0, 1.2)
    space.get_point_manager().add_name_point(3.4, 5.6)
    space.get_point_manager().add_name_point(7.8, 9.0)
    polygon = Polygon("Triangle")
    polygon.add_point(space.get_point_manager().find_point_by_name("P1"))
    polygon.add_point(space.get_point_manager().find_point_by_name("P2"))
    polygon.add_point(space.get_point_manager().find_point_by_name("P3"))
    space.get_shape_manager().add_shape(polygon)
    
def add_point(space: Space):
    tmpStr = str(input("Points format : x.0;y.0 : ")).split(";")
    space.get_point_manager().add_name_point(tmpStr[0], tmpStr[1])

def add_shape2(space: Space):
    shapeType = str(input("Type of Shape : Square/Rectangle/Triangle/Segment (enter number 1-4)"))
    tmpStr = str(input("Shape name : "))
    polygon = Polygon(tmpStr)
    match int(shapeType):
        case 1:
            point_input = str(input(f"Square origin : x.0;y.0 : ")).split(";")
            length = float(input(f"Length of the Square : "))
            angle = int(input(f"Angle of the Square : "))
            tmpPoint = Point(f"{tmpStr}{0}", float(point_input[0]), float(point_input[1]))
            tmpPoint = Point(f"{tmpStr}{1}", float(point_input[0]), float(point_input[1]))
            tmpPoint = Point(f"{tmpStr}{2}", float(point_input[0]), float(point_input[1]))
            tmpPoint = Point(f"{tmpStr}{3}", float(point_input[0]), float(point_input[1]))
        case 2:
            nb_of_points = 4
        case 3:
            nb_of_points = 3
        case _:
            nb_of_points = 2
    for i in range(nb_of_points):
        point_input = str(input(f"Point tmp{i+1} format : x.0;y.0 : ")).split(";")
        tmpPoint = Point(f"tmp{i+1}", float(point_input[0]), float(point_input[1]))
        space.get_point_manager().add_point(tmpPoint)
        polygon.add_point(tmpPoint)
    space.get_shape_manager().add_shape(polygon)
    print(f"Shape {tmpStr} created with {nb_of_points} points.", end="\n\t")

def clean_coord(v: float, eps: float = 1e-9) -> float:
    return 0.0 if abs(v) < eps else v

def add_shape(space: Space):
    shapeType = int(input("Type de forme : Carré/Rectangle/Triangle/Segment/Cercle (entrez un nombre 1-5) : "))
    tmpStr = str(input("Nom de la forme : "))
    polygon = Shape(tmpStr)

    match shapeType:
        # ---------- 1) CARRÉ ----------
        case 1:
            polygon = Polygon(tmpStr, "Carré")
            point_input = str(input("Origine du carré (x.0;y.0) : ")).split(";")
            length = float(input("Longueur du côté du carré : "))
            angle = float(input("Angle du carré (en degrés) : "))

            x0 = float(point_input[0])
            y0 = float(point_input[1])

            angle_rad = math.radians(angle)

            # Vecteur principal (côté orienté)
            ux = math.cos(angle_rad)
            uy = math.sin(angle_rad)

            # Vecteur perpendiculaire (autre côté)
            vx = math.cos(angle_rad + math.pi / 2)
            vy = math.sin(angle_rad + math.pi / 2)

            # 4 sommets du carré (coordonnées nettoyées)
            p0 = Point(f"{tmpStr}0", clean_coord(x0), clean_coord(y0))
            p1 = Point(f"{tmpStr}1", clean_coord(x0 + length * ux), clean_coord(y0 + length * uy))
            p2 = Point(f"{tmpStr}2", clean_coord(x0 + length * ux + length * vx),
                                     clean_coord(y0 + length * uy + length * vy))
            p3 = Point(f"{tmpStr}3", clean_coord(x0 + length * vx), clean_coord(y0 + length * vy))

            for p in (p0, p1, p2, p3):
                space.get_point_manager().add_point(p)
                polygon.add_point(p)

        # ---------- 2) RECTANGLE ----------
        case 2:
            polygon = Polygon(tmpStr, "Rectangle")
            point_input = str(input("Origine du rectangle (x.0;y.0) : ")).split(";")
            length = float(input("Longueur du rectangle (base) : "))
            width = float(input("Largeur du rectangle (hauteur) : "))
            angle = float(input("Angle du rectangle (en degrés) : "))

            x0 = float(point_input[0])
            y0 = float(point_input[1])

            angle_rad = math.radians(angle)

            # Vecteur base
            ux = math.cos(angle_rad)
            uy = math.sin(angle_rad)

            # Vecteur hauteur (perpendiculaire)
            vx = math.cos(angle_rad + math.pi / 2)
            vy = math.sin(angle_rad + math.pi / 2)

            p0 = Point(f"{tmpStr}0", clean_coord(x0), clean_coord(y0))
            p1 = Point(f"{tmpStr}1", clean_coord(x0 + length * ux), clean_coord(y0 + length * uy))
            p2 = Point(f"{tmpStr}2",
                       clean_coord(x0 + length * ux + width * vx),
                       clean_coord(y0 + length * uy + width * vy))
            p3 = Point(f"{tmpStr}3", clean_coord(x0 + width * vx), clean_coord(y0 + width * vy))

            for p in (p0, p1, p2, p3):
                space.get_point_manager().add_point(p)
                polygon.add_point(p)

        # ---------- 3) TRIANGLE (3 points) ----------
        case 3:
            polygon = Polygon(tmpStr, "Triangle")
            print("Saisissez les 3 points du triangle :")
            for i in range(3):
                point_input = str(input(f"Point {i+1} du triangle (x.0;y.0) : ")).split(";")
                px = float(point_input[0])
                py = float(point_input[1])

                p = Point(f"{tmpStr}{i}", clean_coord(px), clean_coord(py))
                space.get_point_manager().add_point(p)
                polygon.add_point(p)

        # ---------- 4) SEGMENT (2 points) ----------
        case 4:
            polygon = Polygon(tmpStr, "Segment")
            print("Saisissez les 2 points du segment :")
            for i in range(2):
                point_input = str(input(f"Point {i+1} du segment (x.0;y.0) : ")).split(";")
                px = float(point_input[0])
                py = float(point_input[1])

                p = Point(f"{tmpStr}{i}", clean_coord(px), clean_coord(py))
                space.get_point_manager().add_point(p)
                polygon.add_point(p)

        # ---------- 5) CERCLE ----------
        case _:
            print("Saisissez l'origine puis le rayon du cercle :")
            point_input = str(input("Centre du cercle (x.0;y.0) : ")).split(";")
            px = float(point_input[0])
            py = float(point_input[1])
            radius = float(input("Rayon : "))

            centre = Point(f"{tmpStr}0", clean_coord(px), clean_coord(py))
            space.get_point_manager().add_point(centre)

            polygon = Circle(tmpStr, centre, radius)

    space.get_shape_manager().add_shape(polygon)
    print()
    print(f"Forme créé : {polygon}")



def show_shapes(space: Space):
    shapes = space.get_shape_manager().get_shapes()
    if not shapes:
        print("No shapes available.")
        return
    for shape in shapes:
        print(shape)


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