class Shape:
    """Forme géométrique de base"""
    nom: str
    
    
    def __init__(self, nom: str):
        self.nom = nom

    def __str__(self):
        pass
    
    def __eq__(self, value):
        pass

    def area(self) -> float:
        """Calcule l'aire de la forme"""
        pass