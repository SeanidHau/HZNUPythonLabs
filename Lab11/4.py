class Fraction :
    def __init__(self, a, b) :
        if b < 0 :
            a = -a
            b = -b

        self.__a = a
        self.__b = b
        self.reduce()

    def to_float(self) :
        return self.__a / self.__b

    def plus(self, r) :
        s = self.__a * r.__b + r.__a * self.__b
        m = self.__b * r.__b
        f = Fraction(s, m)
        f.reduce()
        return f

    def multiply(self, r) :
        s = self.__a * r.__a
        m = self.__b * r.__b
        f = Fraction(s, m)
        f.reduce()
        return f

    def reduce(self) :
        for i in range (2, self.__a + 1) :
            while(self.__a % i == 0 and self.__b % i == 0) :
                self.__a = self.__a // i
                self.__b = self.__b // i

    def print_fraction(self) :
        self.reduce()
        if self.__a == 0:
            print(0)
        elif self.__a == self.__b:
            print(1)
        elif self.__b == 1:
            print(self.__a)
        else:
            print(self.__a, '/', self.__b, sep='')