class Rectangle :
    def __init__(self, w = 1, h = 2) :
        self.__w = w
        self.__h = h

    @property
    def width(self) :
        return self.__w
    
    @width.setter
    def width(self, w) :
        self.__w = w

    @property
    def height(self) :
        return self.__h
    
    @height.setter
    def height(self, h) :
        self.__h = h

    def get_area(self) :
        return self.__w * self.__h

    def get_perimeter(self) :
        return 2 * (self.__w + self.__h)