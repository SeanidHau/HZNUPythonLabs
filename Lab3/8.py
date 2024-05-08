def main() :
    x, op, y = input().split()
    x = int(x)
    y = int(y)
    
    if op == "+" :
        print(x + y)
    elif op == "-" :
        print(x - y)
    elif op == "*" :
        print(x * y)
    elif op == "/" :
        print(x // y)
    elif op == "%" :
        print(x % y) 
    else :
        print("Error")
        

if __name__ == "__main__" :
    main()