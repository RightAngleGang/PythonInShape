from scripts.shapes.Shape import Shape
from scripts.shapes.Point import Point
from scripts.shapes.ShapeType import ShapeType
import math

class Polygon(Shape):
    """Ensemble de points formant une forme fermée"""
    points: list[Point]
    
    def __init__(self, nom: str, points=None):
        super().__init__(nom, ShapeType.Polygon)
        if points is None:
            points = []
        self.points = [point for point in points]

    def _supertype(self):
        """Définit le supertype du polygone en fonction de son type"""
        
        match len(self.points):
            # Segment → 2 points
            case 2:
                return ShapeType.Segment
            
            # Triangle → 3 points
            case 3:
                return ShapeType.Triangle
            
            # Carré / Rectangle → 4 points
            case 4:
                p1, p2, p3, p4 = self.points
                # tous les côtés égaux
                # diagonales égales
                # fonctionne même pour les polygones non alignés avec les axes
                if math.isclose(p1.distance_to(p2), p2.distance_to(p3)) and \
                    math.isclose(p2.distance_to(p3), p3.distance_to(p4)) and \
                    math.isclose(p3.distance_to(p4), p4.distance_to(p1)) and \
                    math.isclose(p1.distance_to(p3), p2.distance_to(p4)) :

                    return ShapeType.Square
                
                elif self.is_rectangle(p1, p2, p3, p4):
                    return ShapeType.Rectangle
            
            case _:        
                return ShapeType.Polygon
    
    def is_rectangle(self, p1, p2, p3, p4):
        """
        Vérifie si les points p1, p2, p3, p4 forment un rectangle.
        L'ordre des points doit être consécutif.
        """
        
        # 1. Calcul des vecteurs entre les points
        # Cette fonction retourne un tuple (dx, dy, dz) représentant le vecteur
        def vecteur(a, b):
            return (b.x - a.x, b.y - a.y, b.z - a.z)

        # 2. Le produit scalaire ne change pas car 'vecteur' retourne un tuple
        def produit_scalaire(v1, v2):
            return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

        # 3. Calcul des vecteurs clés
        vec_p1_p2 = vecteur(p1, p2)
        vec_p4_p3 = vecteur(p4, p3)
        vec_p1_p4 = vecteur(p1, p4)

        # 4. Vérification : Est-ce un Parallélogramme ?
        tol = 1e-9
        parallelogramme = (
            math.isclose(vec_p1_p2[0], vec_p4_p3[0], abs_tol=tol) and
            math.isclose(vec_p1_p2[1], vec_p4_p3[1], abs_tol=tol) and
            math.isclose(vec_p1_p2[2], vec_p4_p3[2], abs_tol=tol)
        )

        if not parallelogramme:
            return False

        # 5. Vérification : Est-ce un Rectangle ?
        dot_prod = produit_scalaire(vec_p1_p2, vec_p1_p4)
        angle_droit = math.isclose(dot_prod, 0.0, abs_tol=tol)

        if not angle_droit:
            return False

        return True
        

    def __str__(self):
        return f"{self.nom} ({self._supertype()}): [{'; '.join(str(p) for p in self.points)}]"
    
    def __eq__(self, value: "Polygon") -> bool:
        if not isinstance(value, Polygon):
            return False
        
        for point in self.points:
            if point not in value.points:
                return False
        
        return len(self.points) == len(value.points)


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
        
    def perimeter(self) -> float:
        """Calcul du périmètre du polygone"""
        n = len(self.points)
        if n < 2:
            return 0.0  # Pas de périmètre pour un point seul
        
        perimeter = 0.0
        for i in range(n):
            j = (i + 1) % n  # Pour boucler au début
            perimeter += self.points[i].distance_to(self.points[j])
        return perimeter
        
    def area(self) -> float:
        """Calcul de l'aire du polygone.

        Utilise une formule spécifique pour les triangles, carrés et rectangles,
        et la formule de Shoelace pour le cas général d'un polygone.
        """
        n = len(self.points)
        if n < 3:
            return 0.0  # Pas de surface si forme colinéaire

        match self._supertype():
            case ShapeType.Triangle:
                return self._triangle_area()
            case ShapeType.Square:
                p1, p2 = self.points[0], self.points[1]
                return p1.distance_to(p2) ** 2
            case ShapeType.Rectangle:
                p1, p2, p3 = self.points[0], self.points[1], self.points[2]
                side1 = p1.distance_to(p2)
                side2 = p2.distance_to(p3)
                return side1 * side2
        
        # Cas général pour les polygones
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += self.points[i].x * self.points[j].y
            area -= self.points[j].x * self.points[i].y
        return abs(area) / 2.0
        
    def _triangle_area(self):
        """
        Calcule l'aire du triangle formé par p1, p2, p3 via le produit vectoriel.
        Fonctionne en 2D (z=0) et en 3D.
        """
        p1, p2, p3 = self.points
        # 1. Calculer les deux vecteurs AB et AC
        # AB = p2 - p1
        ab_x = p2.x - p1.x
        ab_y = p2.y - p1.y
        ab_z = p2.z - p1.z

        # AC = p3 - p1
        ac_x = p3.x - p1.x
        ac_y = p3.y - p1.y
        ac_z = p3.z - p1.z

        # 2. Calculer le Produit Vectoriel (Cross Product) : CP = AB ^ AC
        # Formule : (y1*z2 - z1*y2,  z1*x2 - x1*z2,  x1*y2 - y1*x2)
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x

        # 3. Calculer la Norme du vecteur résultant
        # ||CP|| = sqrt(x² + y² + z²)
        norme = math.sqrt(cp_x**2 + cp_y**2 + cp_z**2)

        # 4. L'aire est la moitié de la norme
        return 0.5 * norme