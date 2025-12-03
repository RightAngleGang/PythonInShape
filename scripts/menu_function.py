from scripts.Point import Point
from scripts.Polygon import Polygon
from scripts.Circle import Circle
from scripts.Space import Space
from scripts.Shape import Shape
from scripts.utils import get_coords2
import math


def add_points(space: Space):
    space.get_point_manager().add_name_point(1.2, 3.4)
    space.get_point_manager().add_name_point(5.6, 7.8)
    space.get_point_manager().add_name_point(9.0, 1.2)
    space.get_point_manager().add_name_point(3.4, 5.6)
    space.get_point_manager().add_name_point(7.8, 9.0)

    #ajout d'une forme pour la démo
    polygon = Polygon("DemoSquare", "Carré")
    p0 = Point("DemoSquare0", 0.0, 0.0)
    p1 = Point("DemoSquare1", 0.0, 1.0)
    p2 = Point("DemoSquare2", 1.0, 1.0)
    p3 = Point("DemoSquare3", 1.0, 0.0)
    for p in (p0, p1, p2, p3):
        space.get_point_manager().add_point(p)
        polygon.add_point(p)
    space.get_shape_manager().add_shape(polygon)


def clean_coord(v: float, eps: float = 1e-9) -> float:
    return 0.0 if abs(v) < eps else v


def add_shape(space: Space):
    try:
        shapeType = int(input("Type de forme : Carré/Rectangle/Triangle/Segment/Cercle (entrez un nombre 1-5) : "))
    except ValueError:
        print("Entrée invalide, merci de saisir un nombre entre 1 et 5.")
        return

    tmpStr = str(input("Nom de la forme : "))

    # ---------- 1) CARRÉ ----------
    if shapeType == 1:
        polygon = Polygon(tmpStr, "Carré")
        print("Saisissez le point d'origine du carré")
        point_input = get_coords2()
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
        p2 = Point(
            f"{tmpStr}2",
            clean_coord(x0 + length * ux + length * vx),
            clean_coord(y0 + length * uy + length * vy),
        )
        p3 = Point(f"{tmpStr}3", clean_coord(x0 + length * vx), clean_coord(y0 + length * vy))

        for p in (p0, p1, p2, p3):
            space.get_point_manager().add_point(p)
            polygon.add_point(p)

    # ---------- 2) RECTANGLE ----------
    elif shapeType == 2:
        polygon = Polygon(tmpStr, "Rectangle")
        print("Saisissez le point d'origine du rectangle")
        (x0, y0) = get_coords2()
        length = float(input("Longueur du rectangle (base) : "))
        width = float(input("Largeur du rectangle (hauteur) : "))
        angle = float(input("Angle du rectangle (en degrés) : "))

        angle_rad = math.radians(angle)

        # Vecteur base
        ux = math.cos(angle_rad)
        uy = math.sin(angle_rad)

        # Vecteur hauteur (perpendiculaire)
        vx = math.cos(angle_rad + math.pi / 2)
        vy = math.sin(angle_rad + math.pi / 2)

        p0 = Point(f"{tmpStr}0", clean_coord(x0), clean_coord(y0))
        p1 = Point(f"{tmpStr}1", clean_coord(x0 + length * ux), clean_coord(y0 + length * uy))
        p2 = Point(
            f"{tmpStr}2",
            clean_coord(x0 + length * ux + width * vx),
            clean_coord(y0 + length * uy + width * vy),
        )
        p3 = Point(f"{tmpStr}3", clean_coord(x0 + width * vx), clean_coord(y0 + width * vy))

        for p in (p0, p1, p2, p3):
            space.get_point_manager().add_point(p)
            polygon.add_point(p)

    # ---------- 3) TRIANGLE (3 points) ----------
    elif shapeType == 3:
        polygon = Polygon(tmpStr, "Triangle")
        print("Saisissez les 3 points du triangle :")
        for i in range(3):
            print(f"Saisir le point {i+1} du triangle :")
            (px, py) = get_coords2()

            p = Point(f"{tmpStr}{i}", clean_coord(px), clean_coord(py))
            space.get_point_manager().add_point(p)
            polygon.add_point(p)

    # ---------- 4) SEGMENT (2 points) ----------
    elif shapeType == 4:
        polygon = Polygon(tmpStr, "Segment")
        print("Saisissez les 2 points du segment :")
        for i in range(2):
            print(f"Saisir le point {i+1} du segment :")
            (px, py) = get_coords2()

            p = Point(f"{tmpStr}{i}", clean_coord(px), clean_coord(py))
            space.get_point_manager().add_point(p)
            polygon.add_point(p)

    # ---------- 5) CERCLE ----------
    elif shapeType == 5:
        print("Saisissez l'origine puis le rayon du cercle :")
        (px, py) = get_coords2()
        radius = float(input("Rayon : "))

        centre = Point(f"{tmpStr}0", clean_coord(px), clean_coord(py))
        space.get_point_manager().add_point(centre)

        polygon = Circle(tmpStr, centre, radius)

    else:
        polygon = Polygon(tmpStr, "Polygone")
        tmpStr = str(input("Combien de points pour la forme polygonale : "))
        for i in range(int(tmpStr)):
            print(f"Saisir le point {i+1} du polygone :")
            (px, py) = get_coords2()

            p = Point(f"{tmpStr}{i}", px, py)
            space.get_point_manager().add_point(p)
            polygon.add_point(p)

    space.get_shape_manager().add_shape(polygon)
    print(f"\nForme créée : {polygon}")


def show_shapes(space: Space):
    shapes = space.get_shape_manager().get_shapes()
    if not shapes:
        print("No shapes available.")
        return
    for shape in shapes:
        print(shape)


def euclidean_distance(space: Space):
    tmpP1 = str(input("Nom du 1er point : "))
    tmpP2 = str(input("Nom du 2eme point : "))
    p1 = space.get_point_manager().find_point_by_name(tmpP1)
    p2 = space.get_point_manager().find_point_by_name(tmpP2)

    if p1 is None:
        print(f"Point '{tmpP1}' introuvable dans l'espace. Impossible de calculer la distance.")
        return
    if p2 is None:
        print(f"Point '{tmpP2}' introuvable dans l'espace. Impossible de calculer la distance.")
        return
    print(f"La distance entre les points est : {p1.distance_to(p2)}")
