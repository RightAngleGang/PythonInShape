from sympy import false

from Shape import Shape

class Point():
    """Point dans un espace 2D"""
    x: float
    y: float
    nom: str
    def __init__(self, x: float, y: float, nom: str):
        self.x = x
        self.y = y
        self.nom = nom


    def distance_to(self, other: "Point") -> float:
        """Calcule la distance entre ce point et un autre point"""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5