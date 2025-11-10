from scripts.Point import Point
from scripts.Space import Space

def add_point(space: Space):
    tmpStr = str(input("Points format : x.0;y.0")).split(";")
    tmpPoint = Point(tmpStr[0], tmpStr[1], "tmp1")
    space.get_point_manager().add_point(tmpPoint)
    print(tmpPoint)