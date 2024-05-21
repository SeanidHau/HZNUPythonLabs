class Point :
    def __init__(self, x = 0, y = 0) :
        self.__x = x
        self.__y = y
    
    def get_x(self) :
        return self.__x

    def get_y(self) :
        return self.__y

    def distance(self, p) :
        return ((p.__x - self.__x) ** 2 + (p.__y - self.__y) ** 2) ** 0.5