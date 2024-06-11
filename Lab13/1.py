from collections import deque

def is_balanced(s: str) -> bool :
    stack = deque()

    for char in s :
        if char == '(' :
            stack.append(char)
        elif char == ')' :
            if not stack or stack.pop() != '(' :
                return False
    return not stack


def main() :
    str = input()
    print(is_balanced(str))


if __name__ == "__main__" :
    main()