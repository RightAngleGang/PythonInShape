import math
import numpy as np
from scripts.Space import Space
from scripts.shapes.Point import Point
from scripts.shapes.Polygon import Polygon
from scripts.shapes.Circle import Circle
from scripts.menu_points import choose_point
from scripts.utils import get_coords2, get_coords3, clean_coord

def add_segment(space: Space, tmpStr: str, a_3d:bool=False) -> Polygon:
    polygon = Polygon(tmpStr, "Segment")
    print("Saisissez les 2 points du segment :")
    for i in range(2):
        print(f"Saisir le point {i+1} du segment :")
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

def add_circle(tmpStr: str, space):
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

def add_polygon(tmpStr: str, space: Space):
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

def add_carre(space: Space, tmpStr: str) -> Polygon:
    polygon = Polygon(tmpStr, "Carré")
    print("Saisissez le point d'origine du carré")
    (x0, y0, z0) = get_coords3()

    length = float(input("Longueur du côté du carré : "))
    theta = float(input("Angle horizontal (azimut θ, en degrés) : "))
    phi = float(input("Angle vertical (élévation φ, en degrés) : "))

    # Conversion radians
    theta = math.radians(theta)
    phi = math.radians(phi)

    # --- Vecteur u (premier côté du carré) ---
    ux = math.cos(phi) * math.cos(theta)
    uy = math.cos(phi) * math.sin(theta)
    uz = math.sin(phi)

    u = np.array([ux, uy, uz])

    # --- Vecteur v (perpendiculaire à u) ---
    # On prend un vecteur de référence pas parallèle à u
    ref = np.array([0, 0, 1])
    if abs(np.dot(ref, u)) > 0.99:  # quasi parallèle → on change
        ref = np.array([0, 1, 0])

    # Produit vectoriel pour obtenir un vecteur perpendiculaire
    v = np.cross(u, ref)
    v = v / np.linalg.norm(v)  # normalisation

    # Multiplication par la longueur du côté
    u *= length
    v *= length

    # --- Points du carré ---
    p0 = Point(f"{tmpStr}0", clean_coord(x0), clean_coord(y0), clean_coord(z0))
    p1 = Point(f"{tmpStr}1", clean_coord(x0 + u[0]), clean_coord(y0 + u[1]), clean_coord(z0 + u[2]))
    p2 = Point(f"{tmpStr}2", clean_coord(x0 + u[0] + v[0]), clean_coord(y0 + u[1] + v[1]),
                clean_coord(z0 + u[2] + v[2]))
    p3 = Point(f"{tmpStr}3", clean_coord(x0 + v[0]), clean_coord(y0 + v[1]), clean_coord(z0 + v[2]))

    for p in (p0, p1, p2, p3):
        space.get_point_manager().add_point(p)
        polygon.add_point(p)
        
    return polygon

def add_rectangle(space: Space, tmpStr: str) -> Polygon:
    
    polygon = Polygon(tmpStr, "Rectangle")
    print("Saisissez le point d'origine du rectangle")
    (x0, y0, z0) = get_coords3()

    length = float(input("Longueur du rectangle (base) : "))
    width = float(input("Largeur du rectangle (hauteur) : "))
    theta = float(input("Angle Horizontal (azimut θ, en degrés) : "))
    phi = float(input("Angle Vertical (élévation φ, en degrés) : "))

    # Conversion en radians
    theta = math.radians(theta)
    phi = math.radians(phi)

    # --- Vecteur u = BASE orientée dans l'espace ---
    ux = math.cos(phi) * math.cos(theta)
    uy = math.cos(phi) * math.sin(theta)
    uz = math.sin(phi)
    u = np.array([ux, uy, uz])
    u = u / np.linalg.norm(u)  # normalisation
    u = u * length  # mise à l'échelle

    # --- Vecteur v = HAUTEUR perpendiculaire à u ---
    # Vecteur de référence pour fabriquer la perpendiculaire
    ref = np.array([0, 0, 1])
    if abs(np.dot(ref, u / length)) > 0.99:
        ref = np.array([0, 1, 0])

    # Produit vectoriel => perpendiculaire
    v = np.cross(u, ref)
    v = v / np.linalg.norm(v)
    v = v * width

    # --- Sommets du rectangle ---
    p0 = Point(f"{tmpStr}0", clean_coord(x0), clean_coord(y0), clean_coord(z0))
    p1 = Point(f"{tmpStr}1", clean_coord(x0 + u[0]), clean_coord(y0 + u[1]), clean_coord(z0 + u[2]))
    p2 = Point(f"{tmpStr}2", clean_coord(x0 + u[0] + v[0]), clean_coord(y0 + u[1] + v[1]),
                clean_coord(z0 + u[2] + v[2]))
    p3 = Point(f"{tmpStr}3", clean_coord(x0 + v[0]), clean_coord(y0 + v[1]), clean_coord(z0 + v[2]))

    for p in (p0, p1, p2, p3):
        space.get_point_manager().add_point(p)
        polygon.add_point(p)
    return polygon