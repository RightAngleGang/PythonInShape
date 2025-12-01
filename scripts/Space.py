from scripts.PointManager import PointManager
from scripts.ShapeManager import ShapeManager
from scripts.Point import Point
from scripts.Shape import Shape
import json


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

    def export_to_json(self, filename):
        """Export the space data to a JSON file"""
        import json

        data = {
            "points": self.points.export_to_json(),
            "shapes": self.shapes.export_to_json(),
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def import_from_json(self, filename):
        """Importe les données de l'espace depuis un fichier JSON, même format que export_to_json"""
        with open(filename, "r") as f:
            data = json.load(f)

        # Clear existing data
        self.points = PointManager()
        self.shapes = ShapeManager()

        # Import points
        for point_data in data.get("points", []):
            point = Point(
                point_data["name"],
                point_data["x"],
                point_data["y"]
            )
            self.points.add_point(point)

        # Import shapes
        for shape_data in data.get("shapes", []):
            if shape_data.get("type") == "Polygon":
                from scripts.Polygon import Polygon
                shape = Polygon(shape_data["name"])
            else:
                shape = Shape(shape_data["name"])
            for point_name in shape_data.get("points", []):
                point = self.points.find_point_by_name(point_name)
                if point:
                    shape.add_point(point)
                else:
                    print(f"Attention: le point '{point_name}' n'existe pas dans l'espace et ne peut pas être ajouté à la forme '{shape.nom}'.")
            self.shapes.add_shape(shape)