from PointManager import PointManager
from ShapeManager import ShapeManager

class Space:
    """Espace contenant des formes géométriques"""
    points: PointManager
    shapes: ShapeManager
    

    def __init__(self):
        self.points = PointManager()
        self.shapes = ShapeManager()

    def get_point_manager(self) -> PointManager:
        """Retourne le gestionnaire de points"""
        return self.points
    
    def get_shape_manager(self) -> ShapeManager:
        """Retourne le gestionnaire de formes"""
        return self.shapes

    def list_points(self):
        """Liste tous les points dans l'espace"""
        self.points.list_points()