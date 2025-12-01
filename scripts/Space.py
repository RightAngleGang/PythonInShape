from scripts.PointManager import PointManager
from scripts.ShapeManager import ShapeManager

class Space:
    """Espace contenant des formes géométriques"""
    pointManager: PointManager
    shapeManager: ShapeManager
    

    def __init__(self):
        self.points = PointManager()
        self.shapes = ShapeManager()

    def get_point_manager(self) -> PointManager:
        """Retourne le gestionnaire de points"""
        return self.pointManager
    
    def get_shape_manager(self) -> ShapeManager:
        """Retourne le gestionnaire de formes"""
        return self.shapeManager

    def list_points(self):
        """Liste tous les points dans l'espace"""
        self.pointManager.list_points()