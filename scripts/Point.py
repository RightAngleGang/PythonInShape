

class Point():
    """Point dans un espace 2D"""
    nom: str
    x: float
    y: float
    
    
    def __init__(self, nom: str,  x: float, y: float):
        self.nom = nom
        self.x = x
        self.y = y

    def __str__(self) -> str:
        pass
    
    def __eq__(self, other: "Point") -> bool:
        pass
    
    def distance_to(self, other: "Point") -> float:
        """Calcule la distance entre ce point et un autre point"""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
    