def get_coords2() -> tuple[float, float]:
    tmpStr = str(input("Donner des coordonnées, format x;y : ")).split(";")
    return float(tmpStr[0].strip()), float(tmpStr[1].strip())