class Car:
    def __init__(self, m, c, y, p):
        print("Hello from init")
        self.model = m
        self.color = c
        self.year = y
        self.power = p

    def Break(self):
        print("Break!")

    def Tell_Info(self):
        print(self.model)
        print(self.color)


persia = Car("TU5", "Black", "1401", "1600")
pride = Car("141", "White", "1398", "600")

persia.Break()
persia.Tell_Info()
