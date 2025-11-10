from Shape import Shape

class Point(Shape):
    """Point dans un espace 2D"""
    x: float
    y: float
    def __init__(self, x: float, y: float, nom: str = ""):
        super().__init__(nom)
        self.x = x
        self.y = y

    def distance_to(self, other: "Point") -> float:
        """Calcule la distance entre ce point et un autre point"""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5