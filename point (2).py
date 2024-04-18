import random
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        """
        This will return a string value used in printing the point
        :return:
        """
        return f"({self.x}, {self.y})"
    def __repr__(self):
        """
        this is when the point is in a list or ather container
        :return:
        """
        return self.__str__()

    def distance_origin(self):
        """

        :return:
        """
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, other):
        """
        define how a point is greater than another
        :param other: the other point to compare the other
        :return:
        """
        return self.distance_origin() > other.distance_origin()

    def __eq__(self, other):
        """
        define when 2 points are equal
        :param other:
        :return:
        """
        return self.distance_origin() == other.distance_origin()

if __name__ == "__main__":
    a = Point(2, 3)
    b = Point(7, 9)

    print(f"a=({a.x}, {a.y})")
    print(f"b=({b.x}, {b.y})")


    points = []
    for _ in range(5):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        random_point = Point(x, y)
        points.append(random_point)

    for point in points:
        print(f"p({point.x}, {point.y})")

    print("Printing point value:", points[0])
    print(points)
    a = Point(3,4)
    print(f"distance to origin: a = {a.distance_origin()}")