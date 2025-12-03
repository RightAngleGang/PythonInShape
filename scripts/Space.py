from scripts.PointManager import PointManager
from scripts.ShapeManager import ShapeManager
from scripts.Point import Point
from scripts.Shape import Shape
from scripts.Polygon import Polygon
from scripts.Circle import Circle
import json



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
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Réinitialiser les managers
        self.pointManager = PointManager()
        self.shapeManager = ShapeManager()

        # ---------- 1) Import des points ----------
        for point_data in data.get("points", []):
            point = Point(
                point_data["name"],
                point_data["x"],
                point_data["y"],
            )
            self.pointManager.add_point(point)

        # ---------- 2) Import des formes ----------
        for shape_data in data.get("shapes", []):
            shape_type = shape_data.get("type")

            # --- POLYGON (Carré, Rectangle, Triangle, Segment, etc.) ---
            if shape_type == "Polygon":
                subtype = shape_data.get("subtype", "Polygon")
                shape = Polygon(shape_data["name"], subtype)

                for point_name in shape_data.get("points", []):
                    point = self.pointManager.find_point_by_name(point_name)
                    if point:
                        shape.add_point(point)
                    else:
                        print(
                            f"Attention: le point '{point_name}' n'existe pas dans "
                            f"l'espace et ne peut pas être ajouté à la forme '{shape.nom}'."
                        )
                self.shapeManager.add_shape(shape)

            # --- CERCLE ---
            elif shape_type == "Circle":
                center_name = shape_data.get("center")
                radius = shape_data.get("radius")

                center_point = self.pointManager.find_point_by_name(center_name)
                if center_point is None:
                    print(
                        f"Attention: le centre '{center_name}' du cercle '{shape_data.get('name')}' "
                        f"n'existe pas dans l'espace. Cercle ignoré."
                    )
                    continue

                shape = Circle(shape_data["name"], center_point, radius)
                self.shapeManager.add_shape(shape)

            # --- SHAPE générique (fallback) ---
            else:
                shape = Shape(shape_data["name"])
                self.shapeManager.add_shape(shape)
