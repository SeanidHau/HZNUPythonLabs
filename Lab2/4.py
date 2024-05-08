def main():
    s = int(input())
    ans = s // 100 + s // 10 % 10 * 10 + s % 10 * 100
    print(ans) 


if __name__ == "__main__":
    main()