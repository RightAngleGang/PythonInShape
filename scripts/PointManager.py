from Point import Point

class PointManager:
    """Espace contenant des formes géométriques"""
    points: list[Point]


    def __init__(self):
        self.points = []

    def add_point(self, point: Point):
        self.points.append(point)
        
    def get_points(self) -> list[Point]:
        """Retourne la liste des points"""
        return self.points
    
    def list_points(self):
        """Liste tous les points dans l'espace"""
        for point in self.points:
            print(f"{point.nom}: ({point.x}, {point.y})")