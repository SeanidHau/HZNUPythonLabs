class Triangle(Shape) :

    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0) :
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self) :
        p = 1 / 2 * (self.side1 + self.side2 + self.side3)
        s = (p * (p - self.side1) * (p - self.side2) * (p - self.side3)) ** 0.5
        return s
    
    def get_perimeter(self) :
        return self.side1 + self.side2 + self.side3
    
    def __str__(self) :
        return super().__str__() + '\n' + "side1 = " + str(self.side1) + " side2 = " + str(self.side2) + " side3 = " + str(self.side3)