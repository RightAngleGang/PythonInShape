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
    
    def __eq__(self, value: "Polygon") -> bool:
        if not isinstance(value, Polygon):
            return False
        
        for point in self.points:
            if point not in value.points:
                return False
        
        return len(self.points) == len(value.points)


    def add_point(self, point: Point):
        if point in self.points:
            raise ValueError("Le point existe déjà dans ce polygone.")
        self.points.append(point)
<<<<<<< HEAD

    def export_to_json(self):
        """Export le polygone au format JSON"""
        return {
            "type": "Polygon",          # pour savoir quelle classe recréer
            "name": self.nom,
            "subtype": self.type,       # Carré / Rectangle / Triangle / Segment
            "points": [point.nom for point in self.points],
        }
=======
        
    def remove_point(self, point: Point):
        if point in self.points:
            raise ValueError("Le point n'existe pas dans ce polygone.")
        self.points.remove(point)
>>>>>>> 91c6a8a (addming remove point from a polygon & preventing having 2 times the same point)
