def encrypt() :
    with open("plaintext.txt", "r") as file :
        plaintext = file.read()

    ciphertext = ''.join(chr(ord(char) + 2) for char in plaintext)
    with open("ciphertext.txt", "w") as file :
        file.write(ciphertext)


def main() :
    encrypt()


if __name__ == "__main__" :
    main()