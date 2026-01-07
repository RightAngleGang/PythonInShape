from scripts.PointManager import PointManager
from scripts.ShapeManager import ShapeManager
from scripts.shapes.Point import Point
from scripts.shapes.Shape import Shape
from scripts.shapes.Polygon import Polygon
from scripts.shapes.Circle import Circle
from scripts.shapes.Cone import Cone
from scripts.shapes.Sphere import Sphere



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
        """Export the space data to a JSON file with support for Enums and NumPy"""
        import json
        import numpy as np
        from enum import Enum

        # 1. Collect the raw data
        data = {
            "points": self.pointManager.export_to_json(),
            "shapes": self.shapeManager.export_to_json(),
        }

        # 2. Define a "translator" for non-standard types
        def json_serial(obj):
            """JSON serializer for objects not serializable by default json code"""
            if isinstance(obj, Enum):
                return obj.name  # Converts ShapeType.POLYGON to "POLYGON"
            if isinstance(obj, np.ndarray):
                return obj.tolist() # Converts NumPy arrays to lists
            if isinstance(obj, (np.integer, np.floating)):
                return obj.item()   # Converts np.int64/float64 to standard Python int/float
            return str(obj)         # Fallback to string if all else fails

        # 3. Export to the provided filename
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, default=json_serial)

        # 4. Also export to the three-json-viewer folder for the visualizer
        viewer_path = "three-json-viewer/public/data.json" # Best practice is /public
        try:
            with open(viewer_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, default=json_serial)
        except FileNotFoundError:
            # Fallback if public/ doesn't exist
            with open("three-json-viewer/data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, default=json_serial)

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
            shape_name = shape_data.get("name", "<sans-nom>")

            if shape_type == "Polygon":
                print("Importing Polygon:", shape_name)
                pts_names = shape_data.get("points", [])
                points = [point_map[name] for name in pts_names]
                # ⚠️ adapte la signature de Polygon si besoin
                shape = Polygon(shape_name, points)

            elif shape_type == "Circle":
                print("Importing Circle:", shape_name)
                center_point = point_map[shape_data["center"]]

                normal_data = shape_data.get("normal", {"x": 0.0, "y": 0.0, "z": 1.0})
                normal = (
                    float(normal_data.get("x", 0.0)),
                    float(normal_data.get("y", 0.0)),
                    float(normal_data.get("z", 1.0)),
                )

                shape = Circle(shape_name, center_point, float(shape_data["radius"]), normal)

            elif shape_type == "Cone":
                print("Importing Cone:", shape_name)
                center_point = point_map[shape_data["center"]]
                apex_point = point_map[shape_data["apex"]]
                shape = Cone(shape_name, center_point, float(shape_data["radius"]), apex_point)

            elif shape_type == "Sphere":
                print("Importing Sphere:", shape_name)
                center_point = point_map[shape_data["center"]]
                shape = Sphere(shape_name, center_point, float(shape_data["radius"]))

            else:
                # ✅ fallback SAFE: uniquement si on a bien une liste de points
                if "points" in shape_data:
                    print("Importing Polygon (fallback):", shape_name)
                    pts_names = shape_data.get("points", [])
                    points = [point_map[name] for name in pts_names]
                    shape = Polygon(shape_name, points)
                else:
                    raise ValueError(
                        f"Shape type non géré et sans 'points': type={shape_type}, name={shape_name}"
                    )

            self.shapeManager.add_shape(shape)
