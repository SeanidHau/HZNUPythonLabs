def is_anagram(s1, s2) :
    sorted_s1 = sorted(s1.strip())
    sorted_s2 = sorted(s2.strip())
    return sorted_s1 == sorted_s2