def distance(x1, y1, x2, y2) :
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class Circle2D :
    def __init__(self, x = 0, y = 0, radius = 0) :
        self.__x = x
        self.__y = y
        self.__radius = radius

    def get_x(self) :
        return self.__x

    def set_x(self, x) :
        self.__x = x
    
    def get_y(self) :
        return self.__y

    def set_y(self, y) :
        self.__y = y
        
    def get_radius(self) :
        return self.__radius
    
    def set_radius(self, radius) :
        self.__radius = radius

    def get_area(self) :
        return math.pi * (self.__radius ** 2)

    def get_perimeter(self) :
        return math.pi * self.__radius * 2
    
    def contains_point(self, x, y) :
        return distance(x, y, self.__x, self.__y) <= self.__radius
    
    def contains(self, Circle2D) :
        dist = distance(self.__x, self.__y, Circle2D.__x, Circle2D.__y)
        return Circle2D.__radius + dist < self.__radius
    
    def overlaps(self, Circle2D) :
        dist = distance(self.__x, self.__y, Circle2D.__x, Circle2D.__y)
        return dist > abs(self.__radius - Circle2D.__radius) and dist < self.__radius + Circle2D.__radius
    
    def __lt__(self, Circle2D) :
        return self.__radius < Circle2D.__radius