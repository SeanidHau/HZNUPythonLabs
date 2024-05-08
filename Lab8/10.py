def list_to_tuples(two_dimensional_list):
    return tuple(tuple(sub_list[::-1]) for sub_list in two_dimensional_list)

def main():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    two_dimensional_list = [line.split() for line in input_lines if line.strip()]
    result = list_to_tuples(two_dimensional_list)
    print(result)

if __name__ == "__main__":
    main()