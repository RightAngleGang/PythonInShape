from scripts.shapes.Shape import Shape
from scripts.shapes.Point import Point
from scripts.shapes.ShapeType import ShapeType
import numpy as np

class Polygon(Shape):
    """Ensemble de points formant une forme fermée"""
    points: list[Point]
    type: str
    
    def __init__(self, nom: str, type: str, points=None):
        super().__init__(nom)
        self.type = ShapeType.Polygon
        if points is None:
            points = []
        self.points = [point for point in points]
        self.type = type

    def __str__(self):
        return f"{self.nom} ({self.type}): [{'; '.join(str(p) for p in self.points)}]"
    
    def __eq__(self, value: "Polygon") -> bool:
        if not isinstance(value, Polygon):
            return False
        
        for point in self.points:
            if point not in value.points:
                return False
        
        return len(self.points) == len(value.points)

    def compute(self) -> str:
        """
        Calcule l'aire OU le volume en fonction du type de forme.
        Retourne un float (aire ou volume).
        """

        n = len(self.points)

        # ----------- SEGMENT → pas d’aire, pas de volume -----------
        if self.type == "Segment":
            return f"L'air est de 0"

        # ----------- TRIANGLE / CARRÉ / RECTANGLE / POLYGONE 3D -----------
        if self.type in ("Triangle", "Carré", "Rectangle", "Polygone"):
            if n < 3:
                return 0.0
            return self._compute_polygon_area()

        # ----------- PYRAMIDE : volume + aire ----------- 
        if self.type == "Pyramide":
            # convention : point 0 = sommet, points 1..n = base
            if n < 4:
                raise ValueError("Une pyramide doit avoir au moins 4 points")
            return self._compute_pyramid_volume()
        if self.type == "Cube":
            return self._compute_cube_volume()

        if self.type == "Pavé":
            return self._compute_pave_volume()
        # ----------- Par défaut : aire de polygone -----------
        if n >= 3:
            return self._compute_polygon_area()

        return 0.0

    def _compute_cube_volume(self) -> float:
        if len(self.points) < 5:
            raise ValueError("Un cube doit avoir au moins 5 points (p0 + p1 + p3 + p4).")

        p0 = self.points[0]
        p1 = self.points[1]  # p0 + u
        p3 = self.points[3]  # p0 + v
        p4 = self.points[4]  # p0 + w

        v1 = np.array([p1.x - p0.x, p1.y - p0.y, getattr(p1, "z", 0.0) - getattr(p0, "z", 0.0)])
        v2 = np.array([p3.x - p0.x, p3.y - p0.y, getattr(p3, "z", 0.0) - getattr(p0, "z", 0.0)])
        v3 = np.array([p4.x - p0.x, p4.y - p0.y, getattr(p4, "z", 0.0) - getattr(p0, "z", 0.0)])

        volume = abs(np.dot(v1, np.cross(v2, v3)))

        return f"Le volume est {float(volume)}"

    def _compute_pave_volume(self) -> float:
        if len(self.points) < 4:
            raise ValueError("Un pavé doit avoir au moins 4 points.")

        p0 = self.points[0]
        origin = np.array([p0.x, p0.y, getattr(p0, "z", 0.0)])

        # Vecteurs depuis p0 vers les autres points
        vectors = []
        for p in self.points[1:]:
            v = np.array([p.x, p.y, getattr(p, "z", 0.0)]) - origin
            if np.linalg.norm(v) > 1e-9:   # éviter le vecteur nul
                vectors.append(v)

        if len(vectors) < 3:
            raise ValueError("Pas assez de vecteurs non nuls pour définir un pavé.")

        # 1) Choisir v1
        v1 = vectors[0]

        # 2) Chercher v2 non colinéaire avec v1
        v2 = None
        for v in vectors[1:]:
            if np.linalg.norm(np.cross(v1, v)) > 1e-9:  # pas colinéaires
                v2 = v
                break

        if v2 is None:
            raise ValueError("Impossible de trouver deux arêtes non colinéaires pour le pavé.")

        # 3) Chercher v3 qui ne soit pas dans le plan de (v1, v2)
        v3 = None
        for v in vectors[1:]:
            mixed = np.dot(v1, np.cross(v2, v))
            if abs(mixed) > 1e-9:  # produit mixte non nul => 3D
                v3 = v
                mixed_product = mixed
                break

        if v3 is None:
            # Tous les points semblent coplanaires -> volume nul
            return 0.0

        volume = abs(mixed_product)
        return f"Le volume est {float(volume)}"
        

    def _compute_polygon_area(self) -> float:
        n = len(self.points)
        area_vector = np.array([0.0, 0.0, 0.0])

        for i in range(n):
            p_i = self.points[i]
            p_next = self.points[(i + 1) % n]

            v_i = np.array([
                p_i.x,
                p_i.y,
                getattr(p_i, "z", 0.0)
            ])
            v_next = np.array([
                p_next.x,
                p_next.y,
                getattr(p_next, "z", 0.0)
            ])

            area_vector += np.cross(v_i, v_next)

        area = 0.5 * np.linalg.norm(area_vector)
        return f"L'air est {float(area)}", float(area)

    def _compute_pyramid_volume(self) -> float:
        if len(self.points) < 5:
            raise ValueError("Une pyramide carrée doit avoir 5 points (4 base + 1 sommet).")

        base_points = self.points[:4]   # b0,b1,b2,b3
        apex = self.points[4]           # sommet

        # aire de la base
        base_polygon = Polygon(self.nom + "_base", "Polygone")
        base_polygon.points = base_points
        _, area_base = base_polygon._compute_polygon_area()

        # normal du plan de base (3 points de base)
        p1, p2, p3 = base_points[:3]
        v1 = np.array([p2.x - p1.x, p2.y - p1.y, getattr(p2, "z", 0.0) - getattr(p1, "z", 0.0)])
        v2 = np.array([p3.x - p1.x, p3.y - p1.y, getattr(p3, "z", 0.0) - getattr(p1, "z", 0.0)])

        normal = np.cross(v1, v2)
        normal = normal / np.linalg.norm(normal)

        p_apex = np.array([apex.x, apex.y, getattr(apex, "z", 0.0)])
        p1_v   = np.array([p1.x, p1.y, getattr(p1, "z", 0.0)])

        height = abs(np.dot((p_apex - p1_v), normal))

        volume = float((1.0/3.0) * area_base * height)

        return f"Le volume est {float(volume)}"

    def add_point(self, point: Point):
        if point in self.points:
            raise ValueError("Le point existe déjà dans ce polygone.")
        self.points.append(point)
        
    def remove_point(self, point: Point):
        if point not in self.points:
            raise ValueError("Le point n'existe pas dans ce polygone.")
        self.points.remove(point)

    def export_to_json(self):
        """Export le polygone au format JSON"""
        return {
            "type": "Polygon",          # pour savoir quelle classe recréer
            "name": self.nom,
            "subtype": self.type,       # Carré / Rectangle / Triangle / Segment
            "points": [point.nom for point in self.points],
        }
        
