class LinearEquation :
    def __init__(self, a, b, c, d, e, f) :
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def is_solvable(self) :
        if (self.__a * self.__d - self.__b * self.__c) != 0 :
            return True
        else : return False

    def get_x(self) :
        return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)

    def get_y(self) :
        return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)