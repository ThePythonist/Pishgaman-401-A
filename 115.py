class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        # print("Area :", self.length * self.width)
        return self.length * self.width

    def perimeter(self):
        # print("Perimeter :", (self.length + self.width) * 2)
        return (self.length + self.width) * 2


l = int(input("Enter length : "))
w = int(input("Enter width : "))

shape = Rectangle(l, w)
print(shape.area())
print(shape.perimeter())

# class Rectangle:
#     def __init__(self, l, w):
#         self.length = l
#         self.width = w
#         self.area = 0
#         self.perimeter = 0
#
#     def Area(self):
#         # print("Area :", self.length * self.width)
#         # return self.length * self.width
#         self.area = self.length * self.width
#
#     def Perimeter(self):
#         # print("Perimeter :", (self.length + self.width) * 2)
#         # return (self.length + self.width) * 2
#         self.perimeter = (self.length + self.width) * 2
