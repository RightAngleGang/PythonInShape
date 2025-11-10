from Point import Point

class PointManager:
    """Espace contenant des formes géométriques"""
    points: list[Point]


    def __init__(self):
        self.points = []
    
    def __str__(self):
        pass

    def add_point(self, point: Point):
        self.points.append(point)
        
    def get_points(self) -> list[Point]:
        """Retourne la liste des points"""
        return self.points
    
    def number_of_points(self) -> int:
        """Retourne le nombre de points"""
        return len(self.points)
        
    def remove_point(self, point: Point):
        """Supprime un point"""
        self.points.remove(point)
        
    def find_point_by_name(self, name: str) -> Point | None:
        """Recherche un point par son nom"""
        for point in self.points:
            if point.nom == name:
                return point
        return None
    
    