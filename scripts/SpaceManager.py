from Point import Point
from Shape import Shape

class Space:
    """Espace contenant des formes géométriques"""

    points: list[Point]
    shapes: list[Shape]

    def __init__(self):
        self.spaces = {}  # { espace: [ {x, y}, ... ] }

    def add_point(self, point: Point):
        self.points.append(point)