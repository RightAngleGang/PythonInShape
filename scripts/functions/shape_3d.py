import math
import numpy as np
from scripts.Space import Space
from scripts.shapes.Point import Point
from scripts.shapes.Polygon import Polygon
from scripts.shapes.Sphere import Sphere
from scripts.shapes.Cone import Cone
from scripts.menu_points import choose_point
from scripts.utils import get_coords2, get_coords3, clean_coord

def add_cube(space: Space, tmpStr: str) -> Polygon:
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
        
    return polygon
        
def add_pave_droit(space: Space, tmpStr: str) -> Polygon:
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
    
    return Sphere(tmpStr, centre, radius)

def add_pyramide(space: Space, tmpStr: str) -> Polygon:
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
        
    return polygon

def add_cone(space: Space, tmpStr: str) -> Cone:

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

    return cone
