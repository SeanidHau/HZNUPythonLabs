class Power :

    def __init__(self, n) :
        self.n = n
        self.count = 0

    def __iter__(self) :
        return self

    def __next__(self) :
        if self.count > self.n :
            raise StopIteration
        result = 3 ** self.count
        self.count += 1
        return result