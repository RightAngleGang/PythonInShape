import numpy as np
import math

from scripts.Space import Space 
from scripts.shapes.Shape import Shape
from scripts.shapes.Point import Point
from scripts.shapes.Polygon import Polygon
from scripts.shapes.Circle import Circle
from scripts.shapes.Cone import Cone
from scripts.shapes.Sphere import Sphere

from scripts.shapes.ShapeType import ShapeType


from scripts.functions.shape_2d import add_carre, add_rectangle, add_triangle, add_segment, add_circle, add_polygon
from scripts.functions.shape_3d import add_cube, add_pave_droit, add_pyramide, add_sphere, add_cone
from scripts.menu_points import choose_point
from scripts.utils import get_coords3

def add_points(space: Space):
    space.get_point_manager().add_name_point(1.2, 3.4, 5.6)
    space.get_point_manager().add_name_point(5.6, 7.8, 9.0)
    space.get_point_manager().add_name_point(9.0, 1.2, 3.4)
    space.get_point_manager().add_name_point(3.4, 5.6, 7.8)
    space.get_point_manager().add_name_point(7.8, 9.0, 1.2)

    polygon = Polygon("Triangle")
    polygon.add_point(space.get_point_manager().find_point_by_name("P1"))
    polygon.add_point(space.get_point_manager().find_point_by_name("P2"))
    polygon.add_point(space.get_point_manager().find_point_by_name("P3"))
    space.get_shape_manager().add_shape(polygon)

    # ajout d'une forme pour la démo
    polygon = Polygon(DemoSquare)
    p0 = Point("DemoSquare0", 0.0, 0.0)
    p1 = Point("DemoSquare1", 0.0, 1.0)
    p2 = Point("DemoSquare2", 1.0, 1.0)
    p3 = Point("DemoSquare3", 1.0, 0.0)
    for p in (p0, p1, p2, p3):
        space.get_point_manager().add_point(p)
        polygon.add_point(p)
    space.get_shape_manager().add_shape(polygon)

    #ajout d'une pyramide pour la démo
    pyramid = Polygon("DemoPyramid")
    p0 = Point("DemoPyramid0", 0.0, 0.0, 0.0)
    p1 = Point("DemoPyramid1", 1.0, 0.0, 0.0)
    p2 = Point("DemoPyramid2", 1.0, 1.0, 0.0)
    p3 = Point("DemoPyramid3", 0.0, 1.0, 0.0)
    p4 = Point("DemoPyramid4", 0.5, 0.5, 1.0)
    for p in (p0, p1, p2, p3, p4):
        space.get_point_manager().add_point(p)
        pyramid.add_point(p)
    space.get_shape_manager().add_shape(pyramid)
    
    shape = Shape("Test")
    space.get_shape_manager().add_shape(shape)
    
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
        
    # ---------- 4) SPHERE (1 pt + 1 rayon) ----------
    elif shapeType == 4:
        shape = add_sphere(space, tmpStr)
        
    # ---------- 5) CÔNE (1 pt + 1 rayon + 1 hauteur) ----------
    elif shapeType == 5:
        shape = add_cone(space, tmpStr)

    else:
        print("Type de forme inconnu. Merci de choisir un nombre entre 1 et 5.")
        return
        
    space.get_shape_manager().add_shape(shape)
    print(f"\nForme 3D créée : {shape}")
    

def show_shapes(space: Space):
    sm = space.get_shape_manager()
    if sm.number_of_shapes() == 0:
        print("No shapes available.")
        return
    print(sm)

def edit_shape(space: Space):
    shape_name = input("Enter the name of the shape to edit: ")
    shape = space.get_shape_manager().find_shape_by_name(shape_name)
    if not shape:
        raise ValueError(f"Shape with name '{shape_name}' not found.")

    print(f"Editing shape: {shape}")
    if isinstance(shape, Polygon):
        choice = input("Do you want to add (1) or remove (2) points? ")
        match choice:
            case '1':
                point = choose_point(space)
                shape.add_point(point)
                print(f"Point {point} added to shape '{shape_name}'.")
            case '2':
                point_name = input("Enter the name of the point to remove:")
                point = space.get_point_manager().find_point_by_name(point_name)
                if not point:
                    raise ValueError(f"Point with name '{point_name}' not found.")
                shape.remove_point(point)
                print(f"Point '{point_name}' removed from shape '{shape_name}'.")
            case _:
                print("Invalid choice. No changes made.")
        return
    
    if isinstance(shape, Sphere):
        print("What would you like to edit?")
        allowed_choices = [1, 2]
        print("1. Center Point (change the point)")
        print("2. Radius")
        
        if isinstance(shape, Circle):
            print("3. Normal Vector (orientation)")
            allowed_choices.append(3)
            
            if isinstance(shape, Cone):
                print(f"4. Height (⚠️ Moves {shape.apex})")
                allowed_choices.append(4)
                
        try:
            edit_choice = int(input("Enter the number of the attribute to edit: "))
            if edit_choice not in allowed_choices:
                raise ValueError("Invalid choice.")
        except ValueError:
            print("Invalid input. No changes made.")
            return
        
        match edit_choice:
            case 1:
                new_point = choose_point(space)
                shape.point = new_point
                print(f"Center point updated to {new_point}.")
            case 2:
                try:
                    new_radius = float(input("Enter new radius: "))
                    shape.radius = new_radius
                    print(f"Radius updated to {new_radius}.")
                except ValueError:
                    print("Invalid radius. No changes made.")
            case 3:
                try:
                    theta = float(input("Azimut θ (°) : "))
                    phi   = float(input("Élévation φ (°) : "))

                    theta_rad = math.radians(theta)
                    phi_rad   = math.radians(phi)

                    nx = math.cos(phi_rad) * math.cos(theta_rad)
                    ny = math.cos(phi_rad) * math.sin(theta_rad)
                    nz = math.sin(phi_rad)

                    normal = (nx, ny, nz)
                    
                    shape.normal = normal
                except ValueError:
                    print("Invalid vector components. No changes made.")
            case 4:
                try:
                    # new_height = float(input("Enter new height: "))
                    input("Enter new height: ")
                    print(f"Cette partie n'est pas implémentée.")
                except ValueError:
                    print("Invalid height. No changes made.")

        
        
        
        
    
    print("Shape editing functionality is not yet implemented.")



def _scale_point_about(p: Point, cx: float, cy: float, cz: float, s: float):
    x, y, z = p.as_tuple()
    nx = cx + s * (x - cx)
    ny = cy + s * (y - cy)
    nz = cz + s * (z - cz)
    p.x = nx
    p.y = ny
    p.z = nz

def _shape_points(shape: Shape) -> list[Point]:
    """Retourne la liste des points qui définissent la forme."""
    if isinstance(shape, Polygon):
        return list(shape.points)

    # Circle / Sphere ont un point "centre"
    if isinstance(shape, (Circle, Sphere)):
        return [shape.point]

    # Cone : centre de base + apex (d'après ton code de création)
    if isinstance(shape, Cone):
        pts = []
        if hasattr(shape, "point"):  # au cas où
            pts.append(shape.point)
        if hasattr(shape, "apex"):
            pts.append(shape.apex)
        # certains cones peuvent stocker center_point
        if hasattr(shape, "center_point"):
            pts.append(shape.center_point)
        # dédoublonnage
        uniq = []
        seen = set()
        for p in pts:
            if p is None:
                continue
            key = id(p)
            if key not in seen:
                seen.add(key)
                uniq.append(p)
        return uniq

    return []


def move_shape(space: Space):
    """Déplace une forme (translation)."""
    shape_name = input("Nom de la forme à déplacer : ").strip()
    shape = space.get_shape_manager().find_shape_by_name(shape_name)
    if not shape:
        print(f"Shape '{shape_name}' introuvable.")
        return

    print("Vecteur de translation :")
    try:
        dx, dy, dz = get_coords3()
    except ValueError as e:
        print(f"Erreur de coordonnées : {e}")
        print("La forme n'a pas été déplacée. Veuillez réessayer avec des coordonnées valides.")
        return

    pts = _shape_points(shape)

    if not pts:
        # Aucun point associé à cette forme : type non supporté ou forme vide
        print(f"Aucun point trouvé pour la forme '{shape_name}'. "
              f"Translation non appliquée (type non supporté ou forme sans points).")
        return

    # Polygon => tous les points
    for p in pts:
        p.translate(dx, dy, dz)

    # si shape a des attributs "radius" (Circle/Sphere/Cone) => pas affecté par translation
    print(f"✅ Forme '{shape_name}' déplacée de ({dx}, {dy}, {dz}).")
    print(f"Nouvelle forme : {shape}")


def scale_shape(space: Space):
    """Scale une forme (mise à l’échelle) autour d’un pivot."""
    shape_name = input("Nom de la forme à scale : ").strip()
    shape = space.get_shape_manager().find_shape_by_name(shape_name)
    if not shape:
        print(f"Shape '{shape_name}' introuvable.")
        return

    try:
        s = float(input("Facteur de scale (ex: 2 = double, 0.5 = moitié) : "))
        if s <= 0:
            print("Le facteur doit être > 0.")
            return
    except ValueError:
        print("Entrée invalide (facteur).")
        return

    # Choix pivot
    print("Pivot du scale :")
    print("  1 - Centre automatique (recommandé)")
    print("  2 - Choisir un point existant (dans l'espace)")
    print("  3 - Coordonnées (x,y,z)")
    mode = input("Votre choix [1/2/3] : ").strip()

    # --- déterminer pivot (cx,cy,cz) ---
    cx = cy = cz = 0.0

    if mode == "2":
        pivot = choose_point(space)
        cx, cy, cz = pivot.as_tuple()

    elif mode == "3":
        print("Coordonnées du pivot :")
        cx, cy, cz = get_coords3()

    else:
        # centre automatique
        if isinstance(shape, Polygon) and shape.points:
            xs, ys, zs = [], [], []
            for p in shape.points:
                x, y, z = p.as_tuple()
                xs.append(x); ys.append(y); zs.append(z)
            cx = sum(xs) / len(xs)
            cy = sum(ys) / len(ys)
            cz = sum(zs) / len(zs)

        elif isinstance(shape, (Circle, Sphere)):
            cx, cy, cz = shape.point.as_tuple()

        elif isinstance(shape, Cone):
            # pivot = centre de base si on l’a
            if hasattr(shape, "point"):
                cx, cy, cz = shape.point.as_tuple()
            elif hasattr(shape, "center_point"):
                cx, cy, cz = shape.center_point.as_tuple()
            else:
                # fallback: apex si rien d'autre
                cx, cy, cz = shape.apex.as_tuple()

        else:
            # fallback global
            cx = cy = cz = 0.0

    # --- scale les points géométriques ---
    pts = _shape_points(shape)
    for p in pts:
        _scale_point_about(p, cx, cy, cz, s)

    # --- scale aussi les dimensions (radius) si nécessaire ---
    # Circle / Sphere / Cone ont un radius
    if hasattr(shape, "radius"):
        shape.radius = float(shape.radius) * s

    print(f"✅ Forme '{shape_name}' scalée par {s} autour de ({cx}, {cy}, {cz}).")
    print(f"Nouvelle forme : {shape}")
