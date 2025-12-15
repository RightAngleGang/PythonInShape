import numpy as np

from scripts.Space import Space 
from scripts.shapes.Point import Point
from scripts.shapes.Polygon import Polygon


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

    # ---------- 6) CÔNE ----------
    elif shapeType == 6:
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
