from scripts.Shape import Shape
from scripts.Point import Point


class Circle(Shape):
    """Ensemble de points formant une forme fermée"""
    point: Point
    radius: float

    def __init__(self, nom: str, point: Point, radius: float):
        super().__init__(nom)
        self.point = point
        self.radius = radius

    def __str__(self):
        return f"{self.nom} (Circle): [origine: {self.point}, rayon: {self.radius}]"

    def export_to_json(self):
        """Export le cercle au format JSON"""
        return {
            "type": "Circle",
            "name": self.nom,
            "center": self.point.nom,
            "radius": self.radius,
        }
