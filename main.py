"""
Lab 6
Authors: Kyle Scarmack and Pair Programmer: Ben Gold
Class: COP3502C
Section: 12309
Description: A simplified password encoder/decoder program
"""


def menu():
    # print menu options
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()


def encode(password):
    encoded_password = ""
    for num in password:
        # shift each digit up by 3 numbers
        encoded_num = str(int(num) + 3)
        # if the encoded number is 10 or more, the encoded number should only display the 2nd digit, such as 10 being 0
        if int(encoded_num) > 9:
            encoded_num = str(int(encoded_num) - 10)
        # add encoded number to encoded password
        encoded_password += encoded_num
    return encoded_password


def decode(password):
    decoded_pass = ""
    for num in password:
        decoded_num = str(int(num) - 3)
        if int(decoded_num) < 0:
            decoded_num = str(int(decoded_num) + 10)
        decoded_pass += decoded_num
    return decoded_pass



def main():
    encoded_password = None
    decoded_password = None
    user_selection = True
    while user_selection:
        menu()
        # prompt user for menu option
        option = int(input("Please enter an option: "))
        if option == 1:
            # prompt user to enter password
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            # display encoded password and decoded password
            # decoded_password = decode(encoded_password)
            decoded_pass = decode(encoded_password)
            print(f"The encoded password is {encoded_password} and the original password is {decoded_pass}.\n")
        elif option == 3:
            quit()


if __name__ == "__main__":
    main()
