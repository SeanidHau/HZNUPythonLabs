def formatted_print(dictionary) :
    sorted_dictionary = sorted(dictionary.items(), key = lambda item: item[1], reverse = True)
    for name, score in sorted_dictionary :
        print(f"{name:<10}{score:6.2f}")
    

def main() :
    dict = {}
    user_input = input()
    while(user_input != "") :
        name, score = user_input.split(",")
        score = float(score)
        dict[name] = score
        user_input = input()
    formatted_print(dict)
    
            

if __name__ == "__main__" :
    main()