

class Point():
    """Point dans un espace 2D"""
    nom: str
    x: float
    y: float
    
    _count = 0

    def __init__(self, x: float, y: float):
        #self.nom = nom
        self.x = x
        self.y = y
        self.nom = f"p{Point._count}" 
        Point._count += 1

    def __str__(self) -> str:
        return f"{self.nom}({self.x};{self.y})"
    
    def __eq__(self, other: "Point") -> bool:
        pass
    
    def distance_to(self, other: "Point") -> float:
        """Calcule la distance entre ce point et un autre point"""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
    