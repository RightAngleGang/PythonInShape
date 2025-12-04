from scripts.Point import Point
from scripts.Polygon import Polygon
from scripts.Circle import Circle
from scripts.Space import Space
from scripts.Shape import Shape
from scripts.utils import get_coords2
from scripts.utils import get_coords3
import math


def add_points(space: Space):
    space.get_point_manager().add_name_point(1.2, 3.4)
    space.get_point_manager().add_name_point(5.6, 7.8)
    space.get_point_manager().add_name_point(9.0, 1.2)
    space.get_point_manager().add_name_point(3.4, 5.6)
    space.get_point_manager().add_name_point(7.8, 9.0)
    
    polygon = Polygon("Triangle", "Triangle")
    polygon.add_point(space.get_point_manager().find_point_by_name("P1"))
    polygon.add_point(space.get_point_manager().find_point_by_name("P2"))
    polygon.add_point(space.get_point_manager().find_point_by_name("P3"))
    space.get_shape_manager().add_shape(polygon)

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
        (x0,y0) = get_coords2()
        length = float(input("Longueur du côté du carré : "))
        angle = float(input("Angle du carré (en degrés) : "))

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

            p = Point(f"{tmpStr}{i}", px, py)
            space.get_point_manager().add_point(p)
            polygon.add_point(p)

    # ---------- 4) SEGMENT (2 points) ----------
    elif shapeType == 4:
        polygon = Polygon(tmpStr, "Segment")
        print("Saisissez les 2 points du segment :")
        for i in range(2):
            print(f"Saisir le point {i+1} du segment :")
            (px, py) = get_coords2()

            p = Point(f"{tmpStr}{i}", px, py)
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

def add_shape3D(space: Space):
    try:
        shapeType = int(input("Type de forme 3D : Cube (1), Pavé droit (2), Pyramide (3) : "))
    except ValueError:
        print("Entrée invalide, merci de saisir un nombre.")
        return

    tmpStr = str(input("Nom de la forme : "))

    # ---------- 1) CUBE ----------
    if shapeType == 1:
        polygon = Polygon(tmpStr, "Cube")

        print("Saisissez le point d'origine du cube (x, y, z)")
        x0, y0, z0 = get_coords3()

        length = float(input("Longueur de l'arête du cube : "))

        azimut = float(input("Angle azimutal dans le plan XY (en degrés) : "))
        elevation = float(input("Angle d'élévation par rapport au plan XY (en degrés) : "))

        azimut_rad = math.radians(azimut)
        elev_rad = math.radians(elevation)

        # Vecteur directeur principal u (orientation de la première arête)
        ux = math.cos(elev_rad) * math.cos(azimut_rad)
        uy = math.cos(elev_rad) * math.sin(azimut_rad)
        uz = math.sin(elev_rad)

        # On choisit un vecteur "quelconque" non colinéaire à u
        if abs(ux) < 0.9:
            ax, ay, az = 1.0, 0.0, 0.0
        else:
            ax, ay, az = 0.0, 1.0, 0.0

        # v = vecteur perpendiculaire à u (normalisé)
        vx = ay * uz - az * uy
        vy = az * ux - ax * uz
        vz = ax * uy - ay * ux
        nv = math.sqrt(vx*vx + vy*vy + vz*vz)
        vx, vy, vz = vx / nv, vy / nv, vz / nv

        # w = u × v (troisième direction orthogonale)
        wx = uy * vz - uz * vy
        wy = uz * vx - ux * vz
        wz = ux * vy - uy * vx

        def make_point(idx, dx, dy, dz):
            return Point(
                f"{tmpStr}{idx}",
                clean_coord(x0 + dx),
                clean_coord(y0 + dy),
                clean_coord(z0 + dz),
            )

        # base (face 0-1-2-3)
        p0 = make_point(0, 0, 0, 0)
        p1 = make_point(1, length * ux,        length * uy,        length * uz)
        p2 = make_point(2, length * (ux+vx),   length * (uy+vy),   length * (uz+vz))
        p3 = make_point(3, length * vx,        length * vy,        length * vz)

        # face du haut (0-1-2-3 + w)
        p4 = make_point(4, length * wx,              length * wy,              length * wz)
        p5 = make_point(5, length * (ux+wx),         length * (uy+wy),         length * (uz+wz))
        p6 = make_point(6, length * (ux+vx+wx),      length * (uy+vy+wy),      length * (uz+vz+wz))
        p7 = make_point(7, length * (vx+wx),         length * (vy+wy),         length * (vz+wz))

        for p in (p0, p1, p2, p3, p4, p5, p6, p7):
            space.get_point_manager().add_point(p)
            polygon.add_point(p)

        space.get_shape_manager().add_shape(polygon)
        print(f"\nForme 3D créée : {polygon}")

    # ---------- 2) PAVÉ DROIT ----------
    elif shapeType == 2:
        polygon = Polygon(tmpStr, "Pavé")

        print("Saisissez le point d'origine du pavé (x, y, z)")
        x0, y0, z0 = get_coords3()

        L = float(input("Longueur : "))
        W = float(input("Largeur : "))
        H = float(input("Hauteur : "))

        azimut = float(input("Angle azimutal dans le plan XY (en degrés) : "))
        elevation = float(input("Angle d'élévation par rapport au plan XY (en degrés) : "))

        azimut_rad = math.radians(azimut)
        elev_rad = math.radians(elevation)

        # Vecteur directeur principal u
        ux = math.cos(elev_rad) * math.cos(azimut_rad)
        uy = math.cos(elev_rad) * math.sin(azimut_rad)
        uz = math.sin(elev_rad)

        # Vecteur non colinéaire pour fabriquer v
        if abs(ux) < 0.9:
            ax, ay, az = 1.0, 0.0, 0.0
        else:
            ax, ay, az = 0.0, 1.0, 0.0

        # v perpendiculaire à u
        vx = ay * uz - az * uy
        vy = az * ux - ax * uz
        vz = ax * uy - ay * ux
        nv = math.sqrt(vx*vx + vy*vy + vz*vz)
        vx, vy, vz = vx / nv, vy / nv, vz / nv

        # w = u × v
        wx = uy * vz - uz * vy
        wy = uz * vx - ux * vz
        wz = ux * vy - uy * vx

        def make_point(idx, dx, dy, dz):
            return Point(
                f"{tmpStr}{idx}",
                clean_coord(x0 + dx),
                clean_coord(y0 + dy),
                clean_coord(z0 + dz),
            )

        # base (0-1-2-3) dans le plan (u, v)
        p0 = make_point(0, 0,          0,          0)
        p1 = make_point(1, L * ux,     L * uy,     L * uz)
        p2 = make_point(2, L * ux + W * vx,
                           L * uy + W * vy,
                           L * uz + W * vz)
        p3 = make_point(3, W * vx,     W * vy,     W * vz)

        # face du haut (translatée de H * w)
        p4 = make_point(4, H * wx,                    H * wy,                    H * wz)
        p5 = make_point(5, L * ux + H * wx,
                           L * uy + H * wy,
                           L * uz + H * wz)
        p6 = make_point(6, L * ux + W * vx + H * wx,
                           L * uy + W * vy + H * wy,
                           L * uz + W * vz + H * wz)
        p7 = make_point(7, W * vx + H * wx,
                           W * vy + H * wy,
                           W * vz + H * wz)

        for p in (p0, p1, p2, p3, p4, p5, p6, p7):
            space.get_point_manager().add_point(p)
            polygon.add_point(p)

        space.get_shape_manager().add_shape(polygon)
        print(f"\nForme 3D créée : {polygon}")

    # ---------- 3) PYRAMIDE À BASE CARRÉE ----------
    elif shapeType == 3:
        polygon = Polygon(tmpStr, "Pyramide")

        print("Saisissez le point d'origine de la base (x, y, z)")
        x0, y0, z0 = get_coords3()

        base_len = float(input("Longueur du côté de la base carrée : "))
        height = float(input("Hauteur de la pyramide ll: "))

        azimut = float(input("Angle azimutal dans le plan XY (en degrés) : "))
        elevation = float(input("Angle d'élévation par rapport au plan XY (en degrés) : "))

        azimut_rad = math.radians(azimut)
        elev_rad = math.radians(elevation)

        # Vecteur directeur principal u
        ux = math.cos(elev_rad) * math.cos(azimut_rad)
        uy = math.cos(elev_rad) * math.sin(azimut_rad)
        uz = math.sin(elev_rad)

        # Vecteur non colinéaire pour fabriquer v
        if abs(ux) < 0.9:
            ax, ay, az = 1.0, 0.0, 0.0
        else:
            ax, ay, az = 0.0, 1.0, 0.0

        # v perpendiculaire à u
        vx = ay * uz - az * uy
        vy = az * ux - ax * uz
        vz = ax * uy - ay * ux
        nv = math.sqrt(vx*vx + vy*vy + vz*vz)
        vx, vy, vz = vx / nv, vy / nv, vz / nv

        # w = u × v
        wx = uy * vz - uz * vy
        wy = uz * vx - ux * vz
        wz = ux * vy - uy * vx

        def make_point(idx, dx, dy, dz):
            return Point(
                f"{tmpStr}{idx}",
                clean_coord(x0 + dx),
                clean_coord(y0 + dy),
                clean_coord(z0 + dz),
            )

        # 4 points de base (carré dans le plan (u, v))
        b0 = make_point(0, 0,                     0,                     0)
        b1 = make_point(1, base_len * ux,         base_len * uy,         base_len * uz)
        b2 = make_point(2, base_len * (ux + vx),  base_len * (uy + vy),  base_len * (uz + vz))
        b3 = make_point(3, base_len * vx,         base_len * vy,         base_len * vz)

        # Centre de la base pour placer le sommet
        cx = x0 + 0.5 * base_len * (ux + vx)
        cy = y0 + 0.5 * base_len * (uy + vy)
        cz = z0 + 0.5 * base_len * (uz + vz)

        apex = Point(
            f"{tmpStr}4",
            clean_coord(cx + height * wx),
            clean_coord(cy + height * wy),
            clean_coord(cz + height * wz),
        )

        for p in (b0, b1, b2, b3, apex):
            space.get_point_manager().add_point(p)
            polygon.add_point(p)

        space.get_shape_manager().add_shape(polygon)
        print(f"\nForme 3D créée : {polygon}")

    else:
        print("Type de forme inconnu. Merci de choisir 1, 2 ou 3.")



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