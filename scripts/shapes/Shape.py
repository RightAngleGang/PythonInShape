from scripts.shape.ShapeType import ShapeType

class Shape:
    """Forme géométrique de base"""
    nom: str
    type: ShapeType

    def __init__(self, nom: str, type=ShapeType.unknown):
        self.nom = nom
        self.type = type

    def __str__(self) -> str:
        return (f"{self.nom} ({self.type}): ?")

    def __eq__(self, value):
        return isinstance(value, Shape) and self.nom == value.nom and self.type == value.type

    def area(self) -> float:
        """Calcule l'aire de la forme"""
        return 0.0

    def export_to_json(self):
        return {
            "type": "{self.type}",
            "name": self.nom,
        }
