from scripts.Space import Space
from scripts.utils import get_coords2, get_coords3
# from scripts.shapes.Shape import Shape
from scripts.shapes.Polygon import Polygon
from scripts.shapes.Point import Point
from scripts.shapes.Circle import Circle
    
def add_point_2d(space: Space):
    """
    Ajoute un point dans l'espace aux coordonnées spécifiées par l'utilisateur. Nom choisi par le gestionnaire de points.
    
    :param space:
    :type space: Space
    """
    x,y = get_coords2()
    pname = space.get_point_manager().add_name_point(x, y)
    print(f"Point '{pname}' ajouté aux coordonnées ({x}; {y}).")
    return pname
    
def add_point_3d(space: Space):
    """
    Ajoute un point dans l'espace aux coordonnées spécifiées par l'utilisateur. Nom choisi par le gestionnaire de points.
    
    :param space:
    :type space: Space
    """
    x,y,z = get_coords3()
    pname = space.get_point_manager().add_name_point(x, y, z)
    print(f"Point '{pname}' ajouté aux coordonnées ({x}; {y}; {z}).")
    return pname
    

def remove_point(space: Space):
    """
    Supprime un point de l'espace en demandant son nom à l'utilisateur.
    
    :param space: 
    :type space: Space
    """
    tmpStr = str(input("Nom du point à supprimer : "))
    point = space.get_point_manager().find_point_by_name(tmpStr)
    if point:
        for shape in space.get_shape_manager().get_shapes():
            if isinstance(shape, Polygon) and point in shape.points:
                shape.remove_point(point)
            if isinstance(shape, Circle) and point.nom == shape.point.nom:
                raise ValueError(f"Le point '{tmpStr}' est le centre du Cercle <{shape.nom}>. Suppression impossible.")
            # Ajouter autres formes
        space.get_point_manager().remove_point(point)
        print(f"Point '{tmpStr}' supprimé avec succès.")
    else:
        raise ValueError(f"Point '{tmpStr}' introuvable. Suppression impossible.")
        
def move_point_2d(space: Space):
    """
    Déplace un point dans l'espace en demandant son nom et les nouvelles coordonnées à l'utilisateur.
    
    :param space: Description
    :type space: Space
    """
    tmpStr = str(input("Nom du point à déplacer : "))
    point = space.get_point_manager().find_point_by_name(tmpStr)
    if point:
        print(f"Point actuel : {point}")
        new_x, new_y = get_coords2()
        point.x = new_x
        point.y = new_y
        print(f"Point '{tmpStr}' déplacé vers ({new_x}; {new_y}).")
    else:
        raise ValueError(f"Point '{tmpStr}' introuvable. Déplacement impossible.")


def move_point_3d(space: Space):
    """
    Déplace un point dans l'espace en demandant son nom et les nouvelles coordonnées à l'utilisateur.
    
    :param space: Description
    :type space: Space
    """
    tmpStr = str(input("Nom du point à déplacer : "))
    point = space.get_point_manager().find_point_by_name(tmpStr)
    if point:
        print(f"Point actuel : {point}")
        new_x, new_y, new_z = get_coords3()
        point.x = new_x
        point.y = new_y
        point.z = new_z
        print(f"Point '{tmpStr}' déplacé vers ({new_x}; {new_y}; {new_z}).")
    else:
        raise ValueError(f"Point '{tmpStr}' introuvable. Déplacement impossible.")
        
def rename_point(space: Space):
    """
    Renomme un point dans l'espace en demandant son nom actuel et le nouveau nom à l'utilisateur.
    
    :param space:
    :type space: Space
    """
    tmpStr = str(input("Nom du point à renommer : "))
    point = space.get_point_manager().find_point_by_name(tmpStr)
    if point:
        new_name = str(input("Nouveau nom du point : "))
        verify_point = space.get_point_manager().find_point_by_name(new_name)
        if verify_point:
            raise ValueError(f"Le nom '{new_name}' est déjà utilisé. Renommage impossible.")
        point.nom = new_name
        print(f"Point renommé en '{new_name}'.")
    else:
        raise ValueError(f"Point '{tmpStr}' introuvable. Renommage impossible.")
    
    
def choose_point(space: Space, allow_2d: bool=False, allow_3d: bool=False) -> Point:
    """
    Permet à l'utilisateur de choisir ou créer un Point.
    
    :param space: L'espace dans lequel le point doit être choisi/créé.
    :type space: Space
    :param allow_2d: Indique si la création de points 2D est permise. Par défaut False.
    :type allow_2d: bool
    :param allow_3d: Indique si la création de points 3D est permise. Par défaut False.
    :type allow_3d: bool
    :return: Le point choisi ou créé.
    :rtype: Point
    """
    while True:
        print("1. Choisir un point existant")
        print("2. Créer un nouveau point")
        choice = input("Choisissez une option (1 ou 2) : ")
        if choice == '1':
            ptname = str(input("Donner le nom du point : "))
            pt = space.get_point_manager().find_point_by_name(ptname)
            if pt is None:
                print(f"Aucun point trouvé avec le nom '{ptname}'. Veuillez réessayer.")
                continue
            return pt
        elif choice == '2':
            if not (allow_2d or allow_3d):
                raise AssertionError("Aucune option de création de point n'est permise pour cette action.")
            
            if not(allow_2d and allow_3d): # une seule option est permise
                if allow_2d:
                    ptname = add_point_2d(space)
                else:
                    ptname = add_point_3d(space)
                    
            else: # les deux options sont permises
                print("Créer un point 2D ou 3D ?")
                print("1. Point 2D")
                print("2. Point 3D")
                subchoice = input("Choisissez une option (1 ou 2) : ")
                if subchoice == '1':
                    ptname = add_point_2d(space)
                elif subchoice == '2':
                    ptname = add_point_3d(space)
            pt = space.get_point_manager().find_point_by_name(ptname)
            if pt is None:
                print(f"Erreur lors de la création du point '{ptname}'. Veuillez réessayer.")
                continue
            return pt
        else:
            print("Option invalide. Veuillez choisir 1 ou 2.")