from enum import Enum, auto

class ShapeType(Enum):
    unknown = "Shape"
    Circle = "Circle"
    Polygon = "Polygon"
    Segment = "Segment"
    Cone = "Cone"
    Sphere = "Sphere"
    
    def __str__(self) -> str:
        return self.value
  
