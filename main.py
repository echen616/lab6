condition = True

def main():
    while condition == True:
        print("Menu")
        print("----------")
        print("1. Encode\n2. Decode\n3. Quit\n")
        option = str(input("Please enter an option: "))
        if option == "1":
            code = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
        elif option == "3":
            exit()

if __name__ == "__main__":
    main()