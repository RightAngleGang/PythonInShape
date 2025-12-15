from enum import Enum

class ShapeType(Enum):
    unknown = "Shape"
    Circle = "Circle"
    Polygon = "Polygon"
    Segment = "Segment"
    Cone = "Cone"
    Sphere = "Sphere"
    Rectangle = "Rectangle"
    Square = "Square"
    
    def __str__(self) -> str:
        return self.value


PARENTS = {
    ShapeType.Segment: ShapeType.Polygon,
    ShapeType.Rectangle: ShapeType.Polygon,
    ShapeType.Square: ShapeType.Polygon,
}