from collections import Counter

def count_vowels(s: str) -> Counter :
    vowels = 'aeiou'
    vowel_counts = Counter(char for char in s if char in vowels)
    sorted_vowels = sorted(vowel_counts.items())
    result = '\n'.join(f"{char}:{counter}" for char, counter in sorted_vowels)
    return result


def main() :
    str = input().lower()
    vowel_count = count_vowels(str)
    print(vowel_count)


if __name__ == "__main__" :
    main()