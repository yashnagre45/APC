import math

def distance(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return math.sqrt(x * x + y * y)


def farthest_point(points):
    farthest = points[0]

    for point in points:
        if distance(point, (0, 0)) > distance(farthest, (0, 0)):
            farthest = point

    return farthest


points = [(2, 3), (4, 5), (-6, 2), (1, -7)]

print("Points:", points)

p1 = points[0]
p2 = points[1]

print("Distance between", p1, "and", p2, ":", distance(p1, p2))
print("Point farthest from origin:", farthest_point(points))