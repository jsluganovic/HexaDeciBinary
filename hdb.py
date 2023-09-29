"""
HexaDeciBinary 
"""

def hexadezimal_in_dezimal(hexadezimal):
    """
    Convert a hexadecimal number to a decimal number.

    :param hexadezimal: The hexadecimal number to convert.
    :return: The decimal number.
    """
    # Convert the hexadecimal number to uppercase to avoid problems with lowercase letters
    hexadezimal = hexadezimal.upper()
    # Initial value for the decimal number
    dezimal = 0
    # Go through each digit of the hexadecimal number
    for i in range(len(hexadezimal)):
        # Convert the digit to a decimal number and add it to the result
        try:
            dezimal += int(hexadezimal[i], 16) * 16 ** (len(hexadezimal) - i - 1)
            """
            Step by step explanation:
            1. the variable [dezimal] is assigned to the value [0]
            2. the loop [runs for] as many times as the [length of the string] hexadezimal
            3. the variable [dezimal] is assigned to the value of the [variable dezimal] PLUS the [value of the string]
               hexadezimal at the position i, converted to an integer times 16 to the power of the length of the string 
               hexadezimal minus i minus 1, cause index starts at 0
            """
        except ValueError:
            raise ValueError("Invalid hexadecimal number")
    return dezimal

def dezimal_in_hexadezimal(dezimal):
    """
    Convert a decimal number to a hexadecimal number.

    :param dezimal: The decimal number to convert.
    :return: The hexadecimal number.
    """
    # Initial value for the hexadecimal number
    hexadezimal = ""
    # Go through each digit of the decimal number
    while dezimal > 0:
        # Convert the digit to a hexadecimal number and add it to the result
        try:
            hexadezimal = str(hex(dezimal % 16)[2:].upper()) + hexadezimal
            """
            Step by step explanation:
            1. hex(dezimal % 16) returns the hexadezimal representation of the last digit of dezimal
            2. [2:] cuts off the first two characters of the string returned by hex(dezimal % 16) because 
               they are not part of the hexadezimal number (0x)
            3. upper() converts the string returned by hex(dezimal % 16)[2:] to uppercase
            4. str(hex(dezimal % 16)[2:].upper()) converts the result of the last three steps to a string
            5. hexadezimal = str(hex(dezimal % 16)[2:].upper()) + hexadezimal adds the string from step 4 
               to the end of the hexadezimal number 
            """
        except ValueError:
            raise ValueError("Invalid decimal number")
        dezimal //= 16 # performs floor division, meaning that the result is rounded down to the next integer
    return hexadezimal

def dual_in_hexadezimal(dual):
    """
    Convert a binary number to a hexadecimal number.

    :param dual: The binary number to convert.
    :return: The hexadecimal number.
    """
    # Initial value for the hexadecimal number
    hexadezimal = ""
    # Go through each digit of the binary number
    while dual != "":
        # Convert the digit to a hexadecimal number and add it to the result
        try:
            hexadezimal = str(hex(int(dual[-4:], 2))[2:].upper()) + hexadezimal
            """
            Step by step explanation:
            1. dual[-4:] returns the last four digits of the binary number
            2. int(dual[-4:], 2) converts the last four digits of the binary number to a decimal number
            3. hex(int(dual[-4:], 2)) converts the decimal number from step 2 to a hexadecimal number
            4. [2:] cuts off the first two characters of the string returned by hex(int(dual[-4:], 2)) because
                they are not part of the hexadezimal number (0x)
            5. upper() converts the string returned by hex(int(dual[-4:], 2))[2:] to uppercase
            6. str(hex(int(dual[-4:], 2))[2:].upper()) converts the result of the last three steps to a string
            7. hexadezimal = str(hex(int(dual[-4:], 2))[2:].upper()) + hexadezimal adds the string from step 6
                to the end of the hexadezimal number
            """

        except ValueError:
            raise ValueError("Invalid binary number")
        dual = dual[:-4] # shifts the processing window four bits to the right for the next iteration of the loop
    return hexadezimal

def hexadezimal_in_dual(hexadezimal):
    """
    Convert a hexadecimal number to a binary number.

    :param hexadezimal: The hexadecimal number to convert.
    :return: The binary number.
    """
    # Convert the hexadecimal number to uppercase to avoid problems with lowercase letters
    hexadezimal = hexadezimal.upper()
    # Initial value for the binary number
    dual = ""
    # Go through each digit of the hexadecimal number
    for i in range(len(hexadezimal)):
        # Convert the digit to a binary number and add it to the result
        try:
            dual += str(bin(int(hexadezimal[i], 16))[2:]).zfill(4)
            """
            Step by step explanation:
            1. hexadezimal[i] returns the digit at position i of the hexadecimal number
            2. int(hexadezimal[i], 16) converts the digit from step 1 to a decimal number
            3. bin(int(hexadezimal[i], 16)) converts the decimal number from step 2 to a binary number
            4. [2:] cuts off the first two characters of the string returned by bin(int(hexadezimal[i], 16)) because
                they are not part of the binary number (0b)
            5. str(bin(int(hexadezimal[i], 16))[2:]) converts the result of the last three steps to a string
            6. str(bin(int(hexadezimal[i], 16))[2:]).zfill(4) adds zeros to the beginning of the string from step 5
                until the string has a length of 4
            7. dual = str(bin(int(hexadezimal[i], 16))[2:]).zfill(4) + dual adds the string from step 6 to the
                beginning of the binary number
            """
        except ValueError:
            raise ValueError("Invalid hexadecimal number")
    return dual


def run():
    # ask what kind of conversion the user wants to do
    print("What kind of conversion do you want to do?")
    print("1: Hexadecimal to decimal")
    print("2: Decimal to hexadecimal")
    print("3: Binary to hexadecimal")
    print("4: Hexadecimal to binary")
    print("5: Exit")
    # get the user's choice
    choice = input("Your choice: ")
    # check the user's choice
    if choice == "1":
        # ask for the hexadecimal number
        hexadezimal = input("Hexadecimal number: ")
        # convert the hexadecimal number to a decimal number
        dezimal = hexadezimal_in_dezimal(hexadezimal)
        # print the result
        print(hexadezimal + " = " + str(dezimal))
    elif choice == "2":
        # ask for the decimal number
        dezimal = int(input("Decimal number: "))
        # convert the decimal number to a hexadecimal number
        hexadezimal = dezimal_in_hexadezimal(dezimal)
        # print the result
        print(str(dezimal) + " = " + hexadezimal)
    elif choice == "3":
        # ask for the binary number
        dual = input("Binary number: ")
        # convert the binary number to a hexadecimal number
        hexadezimal = dual_in_hexadezimal(dual)
        # print the result
        print(dual + " = " + hexadezimal)
    elif choice == "4":
        # ask for the hexadecimal number
        hexadezimal = input("Hexadecimal number: ")
        # convert the hexadecimal number to a binary number
        dual = hexadezimal_in_dual(hexadezimal)
        # print the result
        print(hexadezimal + " = " + dual)
    elif choice == "5":
        # exit the program
        exit()
    else:
        # the user entered an invalid choice
        print("Invalid choice")

run()