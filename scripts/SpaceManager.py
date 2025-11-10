import sys
from pathlib import Path

# Add parent directory to path to import Point
sys.path.insert(0, str(Path(__file__).parent.parent))

from Point import Point

class Space:
    """Espace contenant des formes géométriques"""

    def __init__(self):
        self.points = []  # list of Point objects

    def add_point(self, point: Point):
        self.points.append(point)

    def add_point_interactive(self):
        """Add a point interactively by asking for x and y coordinates"""
        try:
            x = float(input("Entrez la coordonnée x: "))
            y = float(input("Entrez la coordonnée y: "))
            point = Point(x, y)
            self.add_point(point)
            print(f"Point ajouté: {point}")
        except ValueError:
            print("Erreur: Veuillez entrer des nombres valides.")

    def list_points(self):
        """List all points in the space"""
        if not self.points:
            print("Aucun point dans l'espace.")
        else:
            print(f"\n{len(self.points)} point(s) dans l'espace:")
            for i, point in enumerate(self.points, 1):
                print(f"  {i}. {point}")

    def remove_point_interactive(self):
        """Remove a point interactively by asking for its index"""
        if not self.points:
            print("Aucun point à supprimer.")
            return
        
        self.list_points()
        try:
            index = int(input("\nEntrez le numéro du point à supprimer: ")) - 1
            if 0 <= index < len(self.points):
                removed = self.points.pop(index)
                print(f"Point supprimé: {removed}")
            else:
                print("Erreur: Numéro de point invalide.")
        except ValueError:
            print("Erreur: Veuillez entrer un numéro valide.")