

class Point():
    """Point dans un espace 2D"""
    nom: str
    x: float
    y: float
    

    def __init__(self, nom: str, x: float, y: float):
        self.nom = nom
        self.x = float(x)
        self.y = float(y)  
    
    def __str3__(self) -> str:
        return f"{self.nom}({self.x};{self.y})"
    
    def __eq__(self, other: "Point") -> bool:
        pass
    
    def distance_to(self, other: "Point") -> float:
        """Calcule la distance entre ce point et un autre point"""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
    