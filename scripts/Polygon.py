from scripts.Shape import Shape
from scripts.Point import Point

class Polygon(Shape):
    """Ensemble de points formant une forme fermée"""
    points: list[Point]
    type: str
    
    def __init__(self, nom: str, type: str):
        super().__init__(nom)
        self.points = []
        self.type = type

    def __str__(self):
        return f"{self.nom} ({self.type}): [{'; '.join(str(p) for p in self.points)}]"

    def add_point(self, point: Point):
        self.points.append(point)
        