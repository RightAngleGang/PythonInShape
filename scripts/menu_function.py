from scripts.Point import Point
from scripts.Polygon import Polygon
from scripts.Space import Space

def add_point(space: Space):
    tmpStr = str(input("Points format : x.0;y.0")).split(";")
    tmpPoint = Point(tmpStr[0], tmpStr[1], "tmp1")
    space.get_point_manager().add_point(tmpPoint)
    print(tmpPoint.nom + ": (" + str(tmpPoint.x) + ", " + str(tmpPoint.y) + ")")

def add_shape(space: Space):
    tmpStr = str(input("Shape name : "))
    polygon = Polygon(tmpStr)
    nb_of_points = int(input("Number of points : "))
    for i in range(nb_of_points):
        point_input = str(input(f"Point tmp{i+1} format : x.0;y.0")).split(";")
        tmpPoint = Point(point_input[0], point_input[1], f"tmp{i+1}")
        space.get_point_manager().add_point(tmpPoint)
        polygon.add_point(tmpPoint)
    space.get_shape_manager().add_shape(polygon)
    print(f"Shape {tmpStr} created with {nb_of_points} points.")
    for i in range(nb_of_points):
        print(f"Point tmp{i+1}: (" + str(space.get_point_manager().get_points()[-(nb_of_points-i)].x) + ", " + str(space.get_point_manager().get_points()[-(nb_of_points-i)].y) + ")")