import scripts.shapes.ShapeType as st

class Shape:
    """Forme géométrique de base"""
    nom: str
    type: st.ShapeType

    def __init__(self, nom: str, type=st.ShapeType.unknown):
        self.nom = nom
        self.type = type

    def __str__(self) -> str:
        return (f"{self.nom} ({self.type}): ?")

    def __eq__(self, value):
        return isinstance(value, Shape) and self.nom == value.nom and self.type == value.type

    def area(self) -> float:
        """Calcule l'aire de la forme"""
        return 0.0
    
    def volume(self) -> float:
        """Calcule le volume de la forme"""
        return 0.0

    def export_to_json(self):
        return {
            "type": "{self.type}",
            "name": self.nom,
        }
        
    def is_a(self, toCheck: st.ShapeType) -> bool:
        """Vérifie si la forme est d'un type donné"""
        current = self.type
        if current == toCheck:
            return True
        while current in st.PARENTS:
            current = st.PARENTS[current]
            if current == toCheck:
                return True
        return False
