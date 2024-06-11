def quotient(numerator, denominator) :
    if denominator == 0 :
        raise ZeroDivisionError("Zero is an invalid denominator.Please try again.")
    return numerator // denominator


def main() :
    while True :
        try :
            num1, num2 = map(int, input().split())
            print(quotient(num1, num2))
            break
        except (TypeError, NameError, ValueError) :
            print("You must enter intergers.Please try again.")
        except ZeroDivisionError as ex :
            print(ex)


if __name__ == "__main__" :
    main()