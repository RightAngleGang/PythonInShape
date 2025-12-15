class Point():
    """Point dans un espace 2D ou 3D"""
    nom: str
    x: float
    y: float
    z: float
    

    def __init__(self, nom: str, x: float, y: float, z: float=0.0):
        self.nom = nom
        self.x = float(x)
        self.y = float(y)  
        self.z = float(z)  
    
    def __str__(self) -> str:
        return f"{self.nom}({self.x:.3f};{self.y:.3f};{self.z:.3f})"
    
    def __eq__(self, other: "Point") -> bool:
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def translate(self, dx: float, dy: float, dz: float=0.0) -> None:
        """Translate le point selon les deltas fournis"""
        self.x += dx
        self.y += dy
        self.z += dz

    def distance_to(self, other: "Point") -> float:
        """Calcule la distance entre ce point et un autre point"""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5
    
    