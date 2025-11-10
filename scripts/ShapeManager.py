from Shape import Shape

class ShapeManager:
    """Espace contenant des formes géométriques"""
    shapes: list[Shape]
    

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape: Shape):
        self.shapes.append(shape)
        
    def get_shapes(self) -> list[Shape]:
        """Retourne la liste des shapes"""
        return self.shapes
    