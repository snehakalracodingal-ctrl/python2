class area:
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width
o1 = area(12, 10)
o2 = area(5, 6)
print("Dimension of Rectangle - Length : %d Width : %d" % (o1.length, o1.width))
print("Area of Rectangle :", o1.rectangle_area())
print("Dimension of Rectangle - Length : %d Width : %d" % (o2.length, o2.width))
print("Area of Rectangle :", o2.rectangle_area())