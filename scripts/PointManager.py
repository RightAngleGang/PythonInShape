from scripts.Point import Point

class PointManager:
    """Espace contenant des formes géométriques"""
    points: list[Point]


    def __init__(self):
        self.points = []

    def __str__(self):
        pass

    def add_point(self, point: Point):
        if point in self.points:
            return
        if self.find_point_by_name(point.nom) is not None:
            raise ValueError(f"Un point avec le nom '{point.nom}' existe déjà.")
        self.points.append(point)

    def add_name_point(self, x: float, y: float) -> str:
        pid = self.number_of_points() + 1
        point = Point(f"P{pid}", x, y)
        self.add_point(point)
        return point.nom
        
    def get_points(self) -> list[Point]:
        """Retourne la liste des points"""
        return self.points
    
    def number_of_points(self) -> int:
        """Retourne le nombre de points"""
        return len(self.points)

    def remove_point(self, point: Point):
        """Supprime un point"""
        self.points.remove(point)

    def find_point_by_name(self, name: str):
        """Recherche un point par son nom"""
        for point in self.points:
            if point.nom == name:
                return point
        return None


    def list_points(self, separator: str = "\n"):
        """Liste tous les points dans l'espace"""
        print(separator.join([str(point) for point in self.points]))