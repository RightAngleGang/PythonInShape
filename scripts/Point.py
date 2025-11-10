from Shape import Shape

class Point(Shape):
    """Point dans un espace 2D"""
    x: float
    y: float
    def __init__(self, x: float, y: float, nom: str = ""):
        super().__init__(nom)
        self.x = x
        self.y = y