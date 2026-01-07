from scripts.Space import Space 

def euclidean_distance(space: Space):
    tmpP1 = str(input("Nom du 1er point : "))
    tmpP2 = str(input("Nom du 2eme point : "))
    p1 = space.get_point_manager().find_point_by_name(tmpP1)
    p2 = space.get_point_manager().find_point_by_name(tmpP2)

    if p1 is None:
        raise ValueError(f"Point '{tmpP1}' introuvable dans l'espace. Impossible de calculer la distance.")
    if p2 is None:
        raise ValueError(f"Point '{tmpP2}' introuvable dans l'espace. Impossible de calculer la distance.")
    
    return p1.distance_to(p2) 


def get_area(space: Space):
    count = len(space.get_shape_manager().get_shapes())
    if count == 0:
        raise ValueError("Aucune forme disponible dans l'espace.")
    
    tmpStr = str(input("Choisir une forme : "))
    shape = space.get_shape_manager().find_shape_by_name(tmpStr)
    if shape is None:
        raise ValueError("Forme non trouvée.")
    
    area = shape.area()
    
    print(f"L'aire de la forme '{shape.nom}' est : {area}")
    
    
def get_volume(space: Space):
    count = len(space.get_shape_manager().get_shapes())
    if count == 0:
        raise ValueError("Aucune forme disponible dans l'espace.")
    
    tmpStr = str(input("Choisir une forme : "))
    shape = space.get_shape_manager().find_shape_by_name(tmpStr)
    if shape is None:
        raise ValueError("Forme non trouvée.")
    
    area = shape.volume()
    
    print(f"Le volume de la forme '{shape.nom}' est : {area}")

def get_perimeter(space: Space):
    count = len(space.get_shape_manager().get_shapes())
    if count == 0:
        raise ValueError("Aucune forme disponible dans l'espace.")
    
    tmpStr = str(input("Choisir une forme : "))
    shape = space.get_shape_manager().find_shape_by_name(tmpStr)
    if shape is None:
        raise ValueError("Forme non trouvée.")
    
    perimeter = shape.perimeter()
    
    print(f"Le périmètre de la forme '{shape.nom}' est : {perimeter}")