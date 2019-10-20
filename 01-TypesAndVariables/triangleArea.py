# heron formula to calculate area of triangle
import math


def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Pole trójkąta wynosi {area}")


triangle_area(int(input("a: ")), int(input("b: ")), int(input("c: ")))
