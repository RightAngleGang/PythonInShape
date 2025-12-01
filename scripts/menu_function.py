from scripts.Point import Point
from scripts.Polygon import Polygon
from scripts.Space import Space

def add_point(space: Space):
    tmpStr = str(input("Points format : x.0;y.0 : ")).split(";")
    tmpPoint = Point("tmp1", tmpStr[0], tmpStr[1])
    space.get_point_manager().add_point(tmpPoint)
    print(tmpPoint)

def add_shape(space: Space):
    tmpStr = str(input("Shape name : "))
    polygon = Polygon(tmpStr)
    nb_of_points = int(input("Number of points : "))
    for i in range(nb_of_points):
        point_input = str(input(f"Point tmp{i+1} format : x.0;y.0 : ")).split(";")
        tmpPoint = Point(f"tmp{i+1}", point_input[0], point_input[1])
        space.get_point_manager().add_point(tmpPoint)
        polygon.add_point(tmpPoint)
    space.get_shape_manager().add_shape(polygon)
    print(f"Shape {tmpStr} created with {nb_of_points} points.", end="\n\t")
    print(polygon)

def show_shapes(space: Space):
    shapes = space.get_shape_manager().get_shapes()
    if not shapes:
        print("No shapes available.")
        return
    for shape in shapes:
        print(f"Shape: {shape.nom}")
        for point in shape.points:
            print(f"  Point {point.nom}: ({point.x}, {point.y})")