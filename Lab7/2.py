def main() :
    c = input().strip()
    s = input().strip()
    pos = s.rfind(c)
    if pos == -1 :
        print("Not Found")
    else :
        print("index =", pos)
    

if __name__ == '__main__' :
    main()