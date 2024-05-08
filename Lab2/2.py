rank = {"A": 1, "B": 2, "C": 3, "D": 4}


def main():
    ranks = input().split()
    print(rank[ranks[0]] + rank[ranks[1]] + rank[ranks[2]] + rank[ranks[3]] + rank[ranks[4]])


if __name__ == "__main__":
    main()