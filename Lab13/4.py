class Screen :

    def __init__(self, width  =640, height = 480):
        self.width = width
        self.height = height
        if self.width > 1000 or self.height > 1000 or self.width <= 0 or self.height <= 0 :
            print("invalid screen size\n")
            sys.exit()
        else:
            print("screen\n")


class Rectangle(Screen):

    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0, screen = None):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.screen = screen
        print("rectangle")

    def set_coordinations(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0) :
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def set_screen(self, s) :
        self.screen=s
    
    def draw(self) :
        self.width = self.x2 - self.x1
        self.height = self.y2 - self.y1
        if (self.screen.height <= self.height or self.screen.width <= self.width or self.x1 <= 0 or self.x1 >= 1000 or self.x2 <= 0 or self.x2 >= 1000 or self.y1 <= 0 or self.y1 >= 1000 or self.y2 <= 0 or self.y2 >= 1000 or self.width >= 1000 or self.height >= 1000 or self.width <= 0 or self.height <= 0):
            print('invalid rectangle')
        else:
            print(self.x1, end=' ')
            print(self.y1, end=' ')
            print(self.width, end=' ')
            print(self.height)