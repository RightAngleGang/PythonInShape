from scripts.PointManager import PointManager
from scripts.ShapeManager import ShapeManager
from scripts.shapes.Point import Point
from scripts.shapes.Shape import Shape
from scripts.shapes.Polygon import Polygon
from scripts.shapes.Circle import Circle



class Space:
    """Espace contenant des formes géométriques"""

    pointManager: PointManager
    shapeManager: ShapeManager

    def __init__(self):
        self.pointManager = PointManager()
        self.shapeManager = ShapeManager()

    def get_point_manager(self) -> PointManager:
        """Retourne le gestionnaire de points"""
        return self.pointManager

    def get_shape_manager(self) -> ShapeManager:
        """Retourne le gestionnaire de formes"""
        return self.shapeManager

    def list_points(self):
        """Liste tous les points dans l'espace"""
        self.pointManager.list_points()

    def export_to_json(self, filename):
        """Export the space data to a JSON file"""
        import json

        data = {
            "points": self.pointManager.export_to_json(),
            "shapes": self.shapeManager.export_to_json(),
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def import_from_json(self, filename):
        """Importe les données de l'espace depuis un fichier JSON, même format que export_to_json"""
        import json

        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Clear existing data
        self.pointManager = PointManager()
        self.shapeManager = ShapeManager()

        # Import points
        point_map = {}
        for point_data in data.get("points", []):
            point = Point(
                point_data["name"], point_data["x"], point_data["y"], point_data.get("z", 0)
            )
            self.pointManager.add_point(point)
            point_map[point.nom] = point

        # Import shapes
        for shape_data in data.get("shapes", []):
            shape_type = shape_data.get("type")
            if shape_type == "Polygon":
                points = [point_map[name] for name in shape_data["points"]]
                shape = Polygon(shape_data["name"],"Polygon", points)
            elif shape_type == "Circle":
                center_point = point_map[shape_data["center"]]
                shape = Circle(shape_data["name"], center_point, shape_data["radius"])
            elif shape_type == "Cone":
                center_point = point_map[shape_data["center"]]
                apex_point = point_map[shape_data["apex"]]
                shape = Cone(shape_data["name"], center_point, shape_data["radius"], apex_point)
            else:
                shape = Shape(shape_data["name"])
            self.shapeManager.add_shape(shape)
