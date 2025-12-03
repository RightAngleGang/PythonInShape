def get_coords2() -> tuple[float, float]:
    tmpStr = str(input("Donner des coordonnées, format x;y : ")).split(";")
    if len(tmpStr) != 2:
        raise ValueError("Le format doit contenir exactement deux valeurs séparées par ';'")
    return float(tmpStr[0].strip()), float(tmpStr[1].strip())