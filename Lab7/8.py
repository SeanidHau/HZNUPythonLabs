def is_acronym(s) :
    words = s.strip().split()
    acronym = ''
    for word in words :
        acronym += word[0].upper()
    return acronym