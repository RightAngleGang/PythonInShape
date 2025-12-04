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
    Demande à l'utilisateur de saisir des coordonnées au format x;y et les retourne sous forme de tuple de floats.
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