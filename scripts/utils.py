from scripts.Space import Space
from scripts.Point import Point

def get_coords2() -> tuple[float, float]:
    """
    Demande à l'utilisateur de saisir des coordonnées au format x;y et les retourne sous forme de tuple de floats.
    Erreur levée (ValueError) si le format est incorrect ou si les valeurs ne sont pas des nombres valides.
    
    :return: Tuple contenant les coordonnées x et y. (x,y)
    :rtype: tuple[float, float]
    """
    tmpStr = str(input("Donner des coordonnées, format x;y : ")).split(";")
    if len(tmpStr) != 2:
        raise ValueError("Le format doit contenir exactement deux valeurs séparées par ';'")
    try:
        return float(tmpStr[0].strip()), float(tmpStr[1].strip())
    except ValueError:
        raise ValueError("Les coordonnées doivent être des nombres valides.")

def get_coords3() -> tuple[float, float, float]:
    """
    Demande à l'utilisateur de saisir des coordonnées au format x;y;z et les retourne sous forme de tuple de floats.
    Erreur levée (ValueError) si le format est incorrect ou si les valeurs ne sont pas des nombres valides.
    
    :return: Tuple contenant les coordonnées x, y et z. (x,y,z)
    :rtype: tuple[float, float, float]
    """
    tmpStr = str(input("Donner des coordonnées, format x;y;z : ")).split(";")
    if len(tmpStr) != 3:
        raise ValueError("Le format doit contenir exactement trois valeurs séparées par ';'")
    try:
        return float(tmpStr[0].strip()), float(tmpStr[1].strip()), float(tmpStr[2].strip())
    except ValueError:
        raise ValueError("Les coordonnées doivent être des nombres valides.")
    
def choose_point(space: Space, pt_func) -> Point:
    """
    Permet à l'utilisateur de choisir ou créer un Point.
    
    :param space: L'espace dans lequel le point doit être choisi/créé.
    :type space: Space
    :param pt_func: La fonction pour créer un point.
    :type pt_func: Callable
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
            try:
                ptname = pt_func()
                return space.get_point_manager().find_point_by_name(ptname)
            except ValueError as e:
                print(f"Erreur lors de la création du point : {e}. Veuillez réessayer.")
        else:
            print("Option invalide. Veuillez choisir 1 ou 2.")