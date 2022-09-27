import math


def hexagon(side):
    return 6 * areaTriangle(side)


def areaTriangle(side):
    return (math.sqrt(3) / 4) * math.pow(5, 2)


n = float(input("enter the side: "))

print("%.2f" % hexagon(n))
