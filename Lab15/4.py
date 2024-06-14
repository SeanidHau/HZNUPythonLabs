def read_and_xor(filename, positions) :
    with open(filename, "rb") as file :
        byte_values = []
        for pos in positions :
            file.seek(pos - 1)
            byte = file.read(1)
            if byte :
                byte_values.append(byte[0])
                
        result = byte_values[0]
        for value in byte_values[1:] :
            result ^= value
            
        return result
    
    
def main() :
    filename = "image.jpg"
    positions = [13, 49, 80]
    result = read_and_xor(filename, positions)
    print(f"{result:02x}")
    
    
if __name__ == "__main__" :
    main()