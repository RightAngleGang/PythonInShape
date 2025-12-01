from scripts.Point import Point
from scripts.Polygon import Polygon
from scripts.Space import Space
from scripts.utils import get_coords2
    
def add_point(space: Space):
    coords = get_coords2()
    space.get_point_manager().add_name_point(coords[0], coords[1])

def remove_point(space: Space):
    tmpStr = str(input("Nom du point à supprimer : "))
    point = space.get_point_manager().find_point_by_name(tmpStr)
    if point:
        for shape in space.get_shape_manager().get_shapes():
            if isinstance(shape, Polygon) and point in shape.points:
                shape.remove_point(point)
            # Ajout d'autres types de formes si nécessaire
        space.get_point_manager().remove_point(point)
        print(f"Point '{tmpStr}' supprimé avec succès.")
    else:
        print(f"Point '{tmpStr}' introuvable. Suppression impossible.")
        
def move_point(space: Space):
    tmpStr = str(input("Nom du point à déplacer : "))
    point = space.get_point_manager().find_point_by_name(tmpStr)
    if point:
        print(f"Point actuel : {point}")
        new_x, new_y = get_coords2()
        point.x = new_x
        point.y = new_y
        print(f"Point '{tmpStr}' déplacé vers ({new_x}; {new_y}).")
    else:
        print(f"Point '{tmpStr}' introuvable.")
        
def rename_point(space: Space):
    tmpStr = str(input("Nom du point à renommer : "))
    point = space.get_point_manager().find_point_by_name(tmpStr)
    if point:
        new_name = str(input("Nouveau nom du point : "))
        point.nom = new_name
        print(f"Point renommé en '{new_name}'.")
    else:
        print(f"Point '{tmpStr}' introuvable.")