class Circle:
    def __init__(self,r):
        self.radius = r

    def area(self):
        print((self.radius**2)*3.14)

    def perimeter(self):
        print((self.radius * 2) * 3.14)


r = int(input("Enter radius : "))
dayere = Circle(r)
dayere.area()
dayere.perimeter()
