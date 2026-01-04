from scripts.shapes.Shape import Shape

class ShapeManager:
    """Espace contenant des formes géométriques"""
    shapes: list[Shape]
    

    def __init__(self):
        self.shapes = []
    
    def __str__(self) -> str:
        sep = ";\n\t"
        return f"Shapes({self.number_of_shapes()}): [\n\t{sep.join([str(shape) for shape in self.shapes])}\n]"

    def add_shape(self, shape: Shape):
        self.shapes.append(shape)
        
    def get_shapes(self) -> list[Shape]:
        """Retourne la liste des shapes"""
        return self.shapes
    
    def number_of_shapes(self) -> int:
        """Retourne le nombre de shapes"""
        return len(self.shapes)
        
    def remove_shape(self, shape: Shape):
        """Supprime une forme"""
        self.shapes.remove(shape)
        
    def find_shape_by_name(self, name: str):
        """Recherche une forme par son nom"""
        for shape in self.shapes:
            if shape.nom == name:
                return shape
        return None

    def export_to_json(self):
        """Export the shapes to a JSON-serializable list"""
        return [shape.export_to_json() for shape in self.shapes]
