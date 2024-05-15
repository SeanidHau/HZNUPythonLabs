def main() :
    words = input().replace(",", " ").replace(".", " ").split()
    length_count = {}
    total = 0
    for word in words :
        length = len(word)
        total += length
        if length in length_count :
            length_count[length] += 1
        else :
            length_count[length] = 1
    for length in sorted(length_count.keys()) :
        print(f"({length},{length_count[length]})")
    print(f"{total}/{len(words)}")    
    
if __name__ == "__main__" :
    main()