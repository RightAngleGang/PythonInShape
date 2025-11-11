from scripts.Shape import Shape
from scripts.Point import Point

class Polygon(Shape):
    """Ensemble de points formant une forme fermée"""
    points: list[Point]
    
    
    def __init__(self, nom: str):
        super().__init__(nom)
        self.points = []

    def __str__(self):
        return f"{self.nom} (polygone): [{'; '.join(str(p) for p in self.points)}]"

    def add_point(self, point: Point):
        self.points.append(point)
        