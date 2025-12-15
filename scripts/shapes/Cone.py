from scripts.shapes.Circle import Circle
from scripts.shapes.Point import Point
import math

class Cone(Circle):
    """Cône dans l'espace 3D avec une base circulaire et un sommet"""
    apex: Point
    def __init__(self, nom: str, point: Point, radius: float, apex: Point):
        super().__init__(nom, point, radius, (1, 1, 1))
        self.apex = apex

    def __str__(self):
        return f"{self.nom} (Cone): [origine: {self.point}, rayon: {self.radius}, apex: {self.apex}]"

    def area(self) -> float:
        aire_base = super().area()
        hauteur = self.apex.distance_to(self.point)
        generatrice = math.sqrt(hauteur**2 + self.radius**2)
        aire_nappe = math.pi * self.radius * generatrice
        return aire_base + aire_nappe
    
    def volume(self) -> float:
        aire_base = super().area()
        hauteur = self.apex.distance_to(self.point)
        return (1/3) * aire_base * hauteur

    def export_to_json(self):
        """Export le Cone au format JSON"""
        return {
            "type": "Cone",
            "name": self.nom,
            "center": self.point.nom,
            "radius": self.radius,
            "apex": self.apex.nom
        }
