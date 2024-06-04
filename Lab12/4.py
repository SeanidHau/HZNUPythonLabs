class Power:
    
    def __init__(self, n) :
        self.n = n

    def power(self) :
        lst = []
        for i in range(self.n + 1) :
            lst.append(3 ** i)

        return lst