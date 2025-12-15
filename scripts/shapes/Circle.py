import math

from scripts.shapes.Sphere import Sphere
from scripts.shapes.Point import Point

class Circle(Sphere):
    """Cercle dans l'espace 3D"""
    normal: tuple[float, float, float]  # vecteur normal au plan du cercle

    def __init__(self, nom: str, point: Point, radius: float,
                 normal: tuple[float, float, float]):
        super().__init__(nom, point, radius)
        # Normalisation de la normale
        nx, ny, nz = normal
        norm = math.sqrt(nx*nx + ny*ny + nz*nz)
        if norm == 0:
            raise ValueError("Le vecteur normal ne peut pas être nul")
        self.normal = (nx / norm, ny / norm, nz / norm)

    def __str__(self):
        return (
            f"{self.nom} (Circle3D): "
            f"[centre: {self.point}, rayon: {self.radius}, "
            f"normal: {self.normal}]"
        )
        
    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def compute(self) -> str:
        return f"L'air est {math.pi * (self.radius ** 2)}"
    
    def export_to_json(self):
        """Export le cercle au format JSON"""
        return {
            "type": "Circle",
            "name": self.nom,
            "center": self.point.nom,
            "radius": self.radius,
            "normal": {
                "x": self.normal[0],
                "y": self.normal[1],
                "z": self.normal[2],
            },
        }
