class OutOfRange(Exception) :
    def __init__(self, message) :
        super().__init__()
        self.message = message

    def __str__(self) :
        return self.message


class IntRange :
    def __init__(self, lower, upper, value = 0) :
        self.lower = lower
        self.upper = upper
        self.value = value

    def getValue(self) :
        self.value = int(input())
        if self.value < self.lower or self.value > self.upper :
            raise OutOfRange("overflow")
        return self.value