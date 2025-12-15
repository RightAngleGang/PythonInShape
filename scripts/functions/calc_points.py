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
