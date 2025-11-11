from scripts.Polygon import Polygon

class ShapeManager:
    """Espace contenant des formes géométriques"""
    shapes: list[Polygon]
    

    def __init__(self):
        self.shapes = []
    
    def __str__(self):
        pass

    def add_shape(self, shape: Polygon):
        self.shapes.append(shape)
        
    def get_shapes(self) -> list[Polygon]:
        """Retourne la liste des shapes"""
        return self.shapes
    
    def number_of_shapes(self) -> int:
        """Retourne le nombre de shapes"""
        return len(self.shapes)
        
    def remove_shape(self, shape: Polygon):
        """Supprime une forme"""
        self.shapes.remove(shape)
        
    def find_shape_by_name(self, name: str) -> Polygon | None:
        """Recherche une forme par son nom"""
        for shape in self.shapes:
            if shape.nom == name:
                return shape
        return None