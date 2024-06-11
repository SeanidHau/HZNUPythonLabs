from math import sqrt

def get_area(a, b, c) :
    if a + b > c and a + c > b and b + c > a :
        if a == b or a == c or b == c :
            p = (a + b + c) / 2
            area = sqrt(p * (p - a) * (p - b) * (p - c))
            return area
        else :
            raise ValueError("The input is illegal")
    else :
        raise ValueError("The input is illegal")


def main() :
    try :
        a, b, c = map(eval, input().split())
        print(f"{get_area(a, b, c):.2f}")
    except ValueError as ex :
        print(ex)


if __name__ == "__main__" :
    main()
