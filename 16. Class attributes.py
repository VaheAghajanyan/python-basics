class Circle:
    PI = 3.14

    def __init__(self, radius):
       self.radius = radius

    def get_perimeter(self):
        return self.radius * 2 * Circle.PI

    def get_area(self):
        return Circle.PI * self.radius ** 2