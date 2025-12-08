import numpy as np

from scripts.Space import Space 
from scripts.shapes.Point import Point
from scripts.shapes.Polygon import Polygon
from scripts.Cone import Cone
from scripts.utils import get_coords2, get_coords3, clean_coord
import math

from scripts.functions.shape_2d import add_carre, add_rectangle, add_triangle, add_segment, add_circle, add_polygon
from scripts.functions.shape_3d import add_cube, add_pave_droit, add_pyramide, add_sphere, add_cone

def add_points(space: Space):
    space.get_point_manager().add_name_point(1.2, 3.4, 5.6)
    space.get_point_manager().add_name_point(5.6, 7.8, 9.0)
    space.get_point_manager().add_name_point(9.0, 1.2, 3.4)
    space.get_point_manager().add_name_point(3.4, 5.6, 7.8)
    space.get_point_manager().add_name_point(7.8, 9.0, 1.2)

    polygon = Polygon("Triangle", "Triangle")
    polygon.add_point(space.get_point_manager().find_point_by_name("P1"))
    polygon.add_point(space.get_point_manager().find_point_by_name("P2"))
    polygon.add_point(space.get_point_manager().find_point_by_name("P3"))
    space.get_shape_manager().add_shape(polygon)

    # ajout d'une forme pour la démo
    polygon = Polygon("DemoSquare", "Carré")
    p0 = Point("DemoSquare0", 0.0, 0.0)
    p1 = Point("DemoSquare1", 0.0, 1.0)
    p2 = Point("DemoSquare2", 1.0, 1.0)
    p3 = Point("DemoSquare3", 1.0, 0.0)
    for p in (p0, p1, p2, p3):
        space.get_point_manager().add_point(p)
        polygon.add_point(p)
    space.get_shape_manager().add_shape(polygon)

<<<<<<< HEAD
    #ajout d'une pyramide pour la démo
    pyramid = Polygon("DemoPyramid", "Pyramide")
    p0 = Point("DemoPyramid0", 0.0, 0.0, 0.0)
    p1 = Point("DemoPyramid1", 1.0, 0.0, 0.0)
    p2 = Point("DemoPyramid2", 1.0, 1.0, 0.0)
    p3 = Point("DemoPyramid3", 0.0, 1.0, 0.0)
    p4 = Point("DemoPyramid4", 0.5, 0.5, 1.0)
    for p in (p0, p1, p2, p3, p4):
        space.get_point_manager().add_point(p)
        pyramid.add_point(p)
    space.get_shape_manager().add_shape(pyramid)
def clean_coord(v: float, eps: float = 1e-9) -> float:
    return 0.0 if abs(v) < eps else v

def add_segment(space: Space, tmpStr: str, a_3d:bool=False) -> Polygon:
    polygon = Polygon(tmpStr, "Segment")
    print("Saisissez les 2 points du segment :")
    for i in range(2):
        print(f"Saisir le point {i+1} du triangle :")
        p = choose_point(space, allow_2d=True, allow_3d=a_3d)
        polygon.add_point(p)
    return polygon


def add_triangle(space: Space, tmpStr: str, a_3d:bool=False) -> Polygon:
    polygon = Polygon(tmpStr, "Triangle")
    print("Saisissez les 3 points du triangle :")
    for i in range(3):
        print(f"Saisir le point {i+1} du triangle :")
        p = choose_point(space, allow_2d=True, allow_3d=a_3d)
        polygon.add_point(p)
    return polygon

def add_sphere(space: Space, tmpStr: str) -> Sphere:
    print("Saisissez l'origine puis le rayon de la sphere :")
    centre = choose_point(space, allow_3d=True)
    while True:
        try:
            radius = float(input("Rayon : "))
            if radius <= 0:
                print("Le rayon doit être un nombre positif. Veuillez réessayer.")
                continue
            break
        except ValueError:
            print("Entrée invalide. Veuillez saisir un nombre valide pour le rayon.")
    radius = float(input("Rayon : "))

    return Sphere(tmpStr, centre, radius)

def create_circle(tmpStr: str, space):
    """Crée un cercle 3D orienté dans l’espace avec différentes options."""

    print("Saisissez le centre du cercle :")
    (px, py, pz) = get_coords3()
    radius = float(input("Rayon : "))

    # Création du point centre
    centre = Point(
        f"{tmpStr}0",
        clean_coord(px),
        clean_coord(py),
        clean_coord(pz)
    )
    space.get_point_manager().add_point(centre)

    # Choix de l'orientation du cercle
    print("\nOrientation du cercle :")
    print("  1 - Plan XY (par défaut)")
    print("  2 - Par vecteur normal (nx, ny, nz)")
    print("  3 - Par angles (azimut θ, élévation φ)")
    mode = input("Votre choix [1/2/3] : ").strip()

    # Normal par défaut (cercle dans le plan XY)
    normal = (0.0, 0.0, 1.0)

    if mode == "2":
        print("Saisissez un vecteur normal au plan :")
        nx = float(input("nx : "))
        ny = float(input("ny : "))
        nz = float(input("nz : "))

        norm = math.sqrt(nx*nx + ny*ny + nz*nz)
        if norm == 0:
            print("⚠ Vecteur normal nul → normalisation impossible. Normal = (0,0,1).")
        else:
            normal = (nx / norm, ny / norm, nz / norm)

    elif mode == "3":
        theta = float(input("Azimut θ (°) : "))
        phi   = float(input("Élévation φ (°) : "))

        theta_rad = math.radians(theta)
        phi_rad   = math.radians(phi)

        nx = math.cos(phi_rad) * math.cos(theta_rad)
        ny = math.cos(phi_rad) * math.sin(theta_rad)
        nz = math.sin(phi_rad)

        normal = (nx, ny, nz)

    # Création finale du cercle orienté
    circle = Circle(tmpStr, centre, radius, normal)
    return circle

def create_polygon(tmpStr: str, space: Space):
    """Crée un polygone en 3D à partir :
       - de coordonnées 2D (sx, sy) saisies par l'utilisateur
       - d'un point d'origine 3D
       - d'un vecteur normal définissant le plan du polygone
    """

    # 1) Nombre de sommets
    nb_points_str = input("Combien de points pour le polygone ? ")
    try:
        nb_points = int(nb_points_str)
    except ValueError:
        print("Nombre invalide.")
        return None

    if nb_points < 3:
        print("Un polygone doit avoir au moins 3 points.")
        return None

    print("\n=== Saisie des points en 2D (plan local) ===")
    points_2d = []  # liste des (sx, sy)

    for i in range(nb_points):
        print(f"Point {i+1} :")
        (sx, sy) = get_coords2()
        points_2d.append((sx, sy))

    # 2) Point d'origine pour positionner le polygone dans l'espace
    print("\n=== Position du polygone dans l'espace ===")
    print("Saisissez le point d'origine (3D) du polygone :")
    (x0, y0, z0) = get_coords3()

    origin = Point(f"{tmpStr}_O", clean_coord(x0), clean_coord(y0), clean_coord(z0))
    space.get_point_manager().add_point(origin)

    # 3) Vecteur normal définissant l'orientation du polygone dans l'espace
    print("\nSaisissez un vecteur normal pour orienter le polygone :")
    nx = float(input("nx : "))
    ny = float(input("ny : "))
    nz = float(input("nz : "))

    norm = math.sqrt(nx * nx + ny * ny + nz * nz)
    if norm == 0:
        print("⚠ Vecteur normal nul : impossible de définir un plan.")
        return None

    n = np.array([nx / norm, ny / norm, nz / norm])

    # 4) Construction d'une base orthonormée (u, v) dans le plan
    ref = np.array([0.0, 0.0, 1.0])
    if abs(np.dot(ref, n)) > 0.99:
        ref = np.array([1.0, 0.0, 0.0])

    u = np.cross(n, ref)
    u = u / np.linalg.norm(u)

    v = np.cross(n, u)
    v = v / np.linalg.norm(v)

    # 5) Construction réelle du polygone en 3D
    polygon = Polygon(tmpStr, "Polygone")

    for i, (sx, sy) in enumerate(points_2d):
        px = x0 + sx * u[0] + sy * v[0]
        py = y0 + sx * u[1] + sy * v[1]
        pz = z0 + sx * u[2] + sy * v[2]

        p = Point(f"{tmpStr}{i}", clean_coord(px), clean_coord(py), clean_coord(pz))
        space.get_point_manager().add_point(p)
        polygon.add_point(p)

    return polygon

def create_circle(tmpStr: str, space):
    """Crée un cercle 3D orienté dans l’espace avec différentes options."""

    print("Saisissez le centre du cercle :")
    (px, py, pz) = get_coords3()
    radius = float(input("Rayon : "))

    # Création du point centre
    centre = Point(
        f"{tmpStr}0",
        clean_coord(px),
        clean_coord(py),
        clean_coord(pz)
    )
    space.get_point_manager().add_point(centre)

    # Choix de l'orientation du cercle
    print("\nOrientation du cercle :")
    print("  1 - Plan XY (par défaut)")
    print("  2 - Par vecteur normal (nx, ny, nz)")
    print("  3 - Par angles (azimut θ, élévation φ)")
    mode = input("Votre choix [1/2/3] : ").strip()

    # Normal par défaut (cercle dans le plan XY)
    normal = (0.0, 0.0, 1.0)

    if mode == "2":
        print("Saisissez un vecteur normal au plan :")
        nx = float(input("nx : "))
        ny = float(input("ny : "))
        nz = float(input("nz : "))

        norm = math.sqrt(nx * nx + ny * ny + nz * nz)
        if norm == 0:
            print("⚠ Vecteur normal nul → normalisation impossible. Normal = (0,0,1).")
        else:
            normal = (nx / norm, ny / norm, nz / norm)

    elif mode == "3":
        theta = float(input("Azimut θ (°) : "))
        phi = float(input("Élévation φ (°) : "))

        theta_rad = math.radians(theta)
        phi_rad = math.radians(phi)

        nx = math.cos(phi_rad) * math.cos(theta_rad)
        ny = math.cos(phi_rad) * math.sin(theta_rad)
        nz = math.sin(phi_rad)

        normal = (nx, ny, nz)

    # Création finale du cercle orienté
    circle = Circle(tmpStr, centre, radius, normal)
    return circle


def create_polygon(tmpStr: str, space: Space):
    """Crée un polygone en 3D à partir :
       - de coordonnées 2D (sx, sy) saisies par l'utilisateur
       - d'un point d'origine 3D
       - d'un vecteur normal définissant le plan du polygone
    """

    # 1) Nombre de sommets
    nb_points_str = input("Combien de points pour le polygone ? ")
    try:
        nb_points = int(nb_points_str)
    except ValueError:
        print("Nombre invalide.")
        return None

    if nb_points < 3:
        print("Un polygone doit avoir au moins 3 points.")
        return None

    print("\n=== Saisie des points en 2D (plan local) ===")
    points_2d = []  # liste des (sx, sy)

    for i in range(nb_points):
        print(f"Point {i + 1} :")
        (sx, sy) = get_coords2()
        points_2d.append((sx, sy))

    # 2) Point d'origine pour positionner le polygone dans l'espace
    print("\n=== Position du polygone dans l'espace ===")
    print("Saisissez le point d'origine (3D) du polygone :")
    (x0, y0, z0) = get_coords3()

    origin = Point(f"{tmpStr}_O", clean_coord(x0), clean_coord(y0), clean_coord(z0))
    space.get_point_manager().add_point(origin)

    # 3) Vecteur normal définissant l'orientation du polygone dans l'espace
    print("\nSaisissez un vecteur normal pour orienter le polygone :")
    nx = float(input("nx : "))
    ny = float(input("ny : "))
    nz = float(input("nz : "))

    norm = math.sqrt(nx * nx + ny * ny + nz * nz)
    if norm == 0:
        print("⚠ Vecteur normal nul : impossible de définir un plan.")
        return None

    n = np.array([nx / norm, ny / norm, nz / norm])

    # 4) Construction d'une base orthonormée (u, v) dans le plan
    ref = np.array([0.0, 0.0, 1.0])
    if abs(np.dot(ref, n)) > 0.99:
        ref = np.array([1.0, 0.0, 0.0])

    u = np.cross(n, ref)
    u = u / np.linalg.norm(u)

    v = np.cross(n, u)
    v = v / np.linalg.norm(v)

    # 5) Construction réelle du polygone en 3D
    polygon = Polygon(tmpStr, "Polygone")

    for i, (sx, sy) in enumerate(points_2d):
        px = x0 + sx * u[0] + sy * v[0]
        py = y0 + sx * u[1] + sy * v[1]
        pz = z0 + sx * u[2] + sy * v[2]

        p = Point(f"{tmpStr}{i}", clean_coord(px), clean_coord(py), clean_coord(pz))
        space.get_point_manager().add_point(p)
        polygon.add_point(p)

    return polygon


=======
>>>>>>> 4a8c4e1 (♻️ Functions to add 2D shapes moved)
def add_shape(space: Space):
    try:
        shapeType = int(input("Type de forme : Carré/Rectangle/Triangle/Segment/Cercle (entrez un nombre 1-5) : "))
    except ValueError:
        print("Entrée invalide, merci de saisir un nombre entre 1 et 5.")
        return

    tmpStr = str(input("Nom de la forme : "))

    # ---------- 1) CARRÉ ----------
    if shapeType == 1:
        shape = add_carre(space, tmpStr)

    # ---------- 2) RECTANGLE ----------
    elif shapeType == 2:
        shape = add_rectangle(space, tmpStr)

    # ---------- 3) TRIANGLE (3 points) ----------
    elif shapeType == 3:
        shape = add_triangle(space, tmpStr)

    # ---------- 4) SEGMENT (2 points) ----------
    elif shapeType == 4:
        shape = add_segment(space, tmpStr)

    # ---------- 4) SEGMENT (2 points) ----------
    elif shapeType == 4:
        shape = add_segment(space, tmpStr)

    # ---------- 5) CERCLE ----------
    elif shapeType == 5:
        shape = add_circle(tmpStr, space)

    else:
        shape = add_polygon(tmpStr, space)

    space.get_shape_manager().add_shape(shape)
    print(f"\nForme créée : {shape}")

def add_shape3D(space: Space):
    try:
        shapeType = int(input("Type de forme 3D : Cube (1), Pavé droit (2), Pyramide (3), Sphere (4), Cône (5) : "))
    except ValueError:
        print("Entrée invalide, merci de saisir un nombre.")
        return

    tmpStr = str(input("Nom de la forme : "))

    # ---------- 1) CUBE ----------
    if shapeType == 1:
        shape = add_cube(space, tmpStr)


    # ---------- 2) PAVÉ DROIT ----------
    elif shapeType == 2:
        shape = add_pave_droit(space, tmpStr)

    # ---------- 3) PYRAMIDE À BASE CARRÉE ----------
    elif shapeType == 3:
        shape = add_pyramide(space, tmpStr)

<<<<<<< HEAD
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
        # ---------- 6) CÔNE ----------
    elif shapeType == 6:
        cone = Shape("Cone")

        print("Saisissez le point d'origine (centre de la base) du cône (x, y, z)")
        x0, y0, z0 = get_coords3()

        radius = float(input("Rayon de la base du cône : "))
        height = float(input("Hauteur du cône (dans la direction w) : "))

        azimut = float(input("Angle azimutal dans le plan XY (en degrés, direction u) : "))
        elevation = float(input("Angle d'élévation par rapport au plan XY (en degrés, définit w) : "))

        azimut_rad = math.radians(azimut)
        elev_rad = math.radians(elevation)

        # ----- VECTEURS u, v, w -----

        # u = direction de référence dans le plan de la base
        ux = math.cos(elev_rad) * math.cos(azimut_rad)
        uy = math.cos(elev_rad) * math.sin(azimut_rad)
        uz = math.sin(elev_rad)

        # vecteur non-colinéaire
        if abs(ux) < 0.9:
            ax, ay, az = 1.0, 0.0, 0.0
        else:
            ax, ay, az = 0.0, 1.0, 0.0

        # v = perpendiculaire à u (normalisée)
        vx = ay * uz - az * uy
        vy = az * ux - ax * uz
        vz = ax * uy - ay * ux
        nv = math.sqrt(vx*vx + vy*vy + vz*vz)
        vx, vy, vz = vx / nv, vy / nv, vz / nv

        # w = u × v
        wx = uy * vz - uz * vy
        wy = uz * vx - ux * vz
        wz = ux * vy - uy * vx

        # ----- BASE DU CÔNE : un Circle -----

        center_point = Point(
            f"{tmpStr}_base",
            clean_coord(x0),
            clean_coord(y0),
            clean_coord(z0)
        )


        # ----- SOMMET DU CÔNE -----

        apex = Point(
            f"{tmpStr}_apex",
            clean_coord(x0 + height * wx),
            clean_coord(y0 + height * wy),
            clean_coord(z0 + height * wz),
        )
        cone = Cone(f"{tmpStr}", center_point, radius, apex)
        space.get_point_manager().add_point(apex)
        space.get_point_manager().add_point(center_point)
        space.get_shape_manager().add_shape(cone)
        print(f"\nForme 3D créée : {cone}")
    # ---------- 4) SEGMENT ----------
=======
    # ---------- 4) SPHERE (1 pt + 1 rayon) ----------
>>>>>>> 37c6332 (♻️ Moved functions to add 3D shapes)
    elif shapeType == 4:
        shape = add_sphere(space, tmpStr)
        
    # ---------- 5) CÔNE (1 pt + 1 rayon + 1 hauteur) ----------
    elif shapeType == 5:
        shape = add_cone(space, tmpStr)

    else:
        print("Type de forme inconnu. Merci de choisir un nombre entre 1 et 5.")
        
    space.get_shape_manager().add_shape(shape)
    print(f"\nForme 3D créée : {shape}")
    

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


