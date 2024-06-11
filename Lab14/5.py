from math import sqrt

class NegativeNumberException(Exception) :
    def __init__(self, message) :
        super().__init__()
        self.message = message

    def __str__(self) :
        return self.message


def square_root(x) :
    if x < 0 :
        raise NegativeNumberException("Invalid")
    return sqrt(x)


def main() :
    try :
        num = eval(input())
        print(f"{square_root(num):.2f}")
    except NegativeNumberException as ex :
        print(ex)


if __name__ == "__main__" :
    main()