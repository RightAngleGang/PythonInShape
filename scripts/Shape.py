from abc import abstractmethod


class Shape:
    """Forme géométrique de base"""
    nom: str

    def __init__(self, nom: str):
        self.nom = nom

    def __str__(self) -> str:
        return self.nom

    def __eq__(self, value):
        return isinstance(value, Shape) and self.nom == value.nom

    def area(self) -> float:
        """Calcule l'aire de la forme"""
        return 0.0

    @abstractmethod
    def compute() -> float:
        pass
    
    def export_to_json(self):
        return {
            "type": "Shape",
            "name": self.nom,
        }
