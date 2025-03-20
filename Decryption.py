#!/bin/bash
def display_details():
    print()
    print("***Welcome***")
    print()
    print("Hopefully you were able to find the encryted string")
    print("Did you though the location would be in plain text???") 
    print("Unfortunately we don't store anything in plain text :)")
    print("This program will help you to find the Location!")
    print()
    print("Goodluck!")
    print()
    

display_details()


# Displaying menu to the screen using function
def get_menu_choice():
    print("*** Menu ***")
    print()
    print("1. Encrypt string")
    print("2. Decrypt string")
    print("3. Brute force decryption")
    print("4. Quit")
    print()

get_menu_choice()

# Asking user what he/she wants to do
choice = int(input("What would you like to do [1,2,3,4]? "))
print()



# creating valid choices
valid_choices  = [1,2,3,4]

# If user choose invalid choice 
while choice not in valid_choices:
    print("Invalid choice, please enter either 1, 2, 3 or 4.")
    print()
    choice = int(input("What would you like to do [1,2,3,4]? "))
    print()


# When user enter valid choice 
while choice in valid_choices:

# Using if statements to convert valid choice in to particular program

    if choice == 1:
        # Asking user to enter string to enscrypt and offset value
        string_to_encrypt = input("Please enter string to encrypt: ")
        offset_value = int(input("Please enter offset value (1 to 94): "))

        # Using while loop to make sure user enter valid offset value
        while offset_value < 1 or offset_value > 94:
            offset_value = int(input("Please enter offset value (1 to 94): "))


        # Creating empty string which will help in loop
        encrypted_string = ''
        print()
        # Use loop to iterate over string
        for ch in string_to_encrypt:

            # Using ord() and chr() functions to enscrypt the string 
            if ord(ch) + offset_value > 126:
                encrypted_string += chr(ord(ch) + offset_value - 95)
            else:
                encrypted_string += chr(ord(ch) + offset_value)

        # Printing encrypted string
        print("Encrypted string:")
        print(encrypted_string)
        print()

        # Displaying choice and asking user if they want to use that program again
        get_menu_choice()
        choice = int(input("What would you like to do [1,2,3,4]? "))
        print()
    elif choice == 2:
        # Asking user to enter enscrypt string and offset value
        encrypted_string = input("Please enter string to Decrypt: ")
        offset_value = int(input("Please enter offset value (1 to 94): "))

        # Using while loop to make sure user enter valid offset value
        while offset_value < 1 or offset_value > 94:
            offset_value = int(input("Please enter offset value (1 to 94): "))

        # Creating empty string which will help in loop
        decrypted_string = ''

        # Use loop to iterate over string
        for ch in encrypted_string:
            # Using ord() and chr() functions to decrypt the string
            if ord(ch) - offset_value < 32:
                decrypted_string += chr(ord(ch) - offset_value + 95)
            else:
                decrypted_string += chr(ord(ch) - offset_value)
        print()
        # Printing decrypted string
        print("decrypted_string")
        print(decrypted_string)
        print()

        # Displaying menu and asking user if they want to use that program again
        get_menu_choice()
        choice = int(input("What would you like to do [1,2,3,4]? "))
        print()


    elif choice == 3:
        # Asking user to enter enscrypt
        encrypted_string = input("Please enter string to decrypt: ")
        print()
        print("Brute Force is disabled for this challenge! If you have python skills write it yourself and make your life easy")
        print()
         
        # Asking user if he/she wants to use the program again
        get_menu_choice()
        choice = int(input("What would you like to do [1,2,3,4]? "))

    elif choice == 4:
        print()
        print("Goodbye")
        choice=0



        
