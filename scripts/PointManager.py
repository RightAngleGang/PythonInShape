from scripts.shapes.Point import Point

class PointManager:
    """Gestionnaire de points dans un espace 2D"""
    points: list[Point]
    pid: int


    def __init__(self):
        self.points = []
        self.pid = 1
    def __str__(self):
        return f"Points({self.number_of_points()}): [" + "; ".join([str(point) for point in self.points]) + "]"

    def add_point(self, point: Point):
        if self.find_point_by_name(point.nom) is not None:
            raise ValueError(f"Un point avec le nom '{point.nom}' existe déjà.")
        self.points.append(point)

    def add_name_point(self, x: float, y: float, z: float=0) -> str:
        """Ajoute un point avec un nom généré automatiquement et retourne son nom"""
        point = Point(f"P{self.pid}", x, y, z)
        try:
            self.add_point(point)
            self.pid += 1  # Only increment if addition succeeds
        except ValueError as e:
            raise ValueError(f"Erreur lors de l'ajout du point<{point}>: {e}")
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

    def export_to_json(self):
        """Export the points to a JSON-serializable list"""
        return [
            {"name": point.nom, "x": point.x, "y": point.y, "z": point.z}
            for point in self.points
        ]