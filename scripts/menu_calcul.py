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
        print("Aucune forme disponible dans l'espace.")
        return
    show_shapes(space)
    shapeIndex = int(input(f"Selectionnez la forme voulu pour avoir son aire/volume (0-{count - 1}) : "))
    
    value = space.get_shape_manager().get_shapes()[shapeIndex].compute()
    print(value)

def get_volume(space: Space):
    pass

# Backwards-compatible alias for the previous misspelled name
get_voulme = get_volume