import math

def main() :
    o, h, l ,c = map(float, input().split())
    eps = 1e-6
    if c < o:
        print("BW-Solid", end = '')
    elif c > o:
        print("R-Hollow", end = '')
    elif math.fabs(c - o) <= eps:
        print("R-Cross", end = '')
    if (l < o and l < c) and (h > o and h > c):
        print(" with Lower Shadow and Upper Shadow")
    elif (l < o and l < c):
        print(" with Lower Shadow")
    elif (h > o and h > c):
        print(" with Upper Shadow")


if __name__ == "__main__" :
    main()