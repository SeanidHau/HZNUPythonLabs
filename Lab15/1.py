def write_to_file(user_input) :
    nums = list(map(int, user_input.split()))
    with open("example.txt", "w") as file :
        for i in range(0, len(nums), 5) :
            line = ' '.join(map(str, nums[i: i  + 5]))
            file.write(line + "\n")
            

def main() :
    user_input = input()
    write_to_file(user_input)
    

if __name__ == "__main__" :
    main()