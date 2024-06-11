from math import sqrt

def square_root(x) :
    if x < 0 :
        raise ArithmeticError("Invalid")
    return sqrt(x)


def main() :
    num = eval(input())
    try :
        print(f"{square_root(num):.2f}")
    except ArithmeticError as ex :
        print(ex)


if __name__ == "__main__" :
    main()