# Eddy Chen


condition = True
password = ""
def main():
    while condition == True:
        print("Menu")
        print("----------")
        print("1. Encode\n2. Decode\n3. Quit\n")
        option = str(input("Please enter an option: "))
        if option == "1":
            global password
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
        elif option == "2":
            decode()

        elif option == "3":
            exit()
def encode(password):
    newpass = ""
    for element in password:
        if element == "0":
            newpass += "3"
        elif element == "1":
            newpass += "4"
        elif element == "2":
            newpass += "5"
        elif element == "3":
            newpass += "6"
        elif element == "4":
            newpass += "7"
        elif element == "5":
            newpass += "8"
        elif element == "6":
            newpass += "9"
        elif element == "7":
            newpass += "0"
        elif element == "8":
            newpass += "1"
        elif element == "9":
            newpass += "2"
    return newpass
def decode():
    print(f"The encoded password is {encode(password)}, and the original password is {password}.")
if __name__ == "__main__":
    main()

