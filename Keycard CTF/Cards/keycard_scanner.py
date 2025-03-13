print("Offline Member Card Scanner")
print("-----------------------")
print()
print("no card reader attached")
print()
print("Please load a card by entering the file name")
print("Example: KC_239_Ricky.nfc")


user_password = None

bruce_password = "76544567"
bruce_balance = "Balance[$700023.23]"
bruce_name = "Bruce .B"
bruce_personal = "Bruce Buggins \nGold Square Rank \n---------------------- \nMember since: 12/Aug/1955 \nExpiry:       12/Feb/2008 \n---------------------- \nDoB:        29/Jan/1935 \nOccupation: Cricketer - Machine Operator \nHome Town:  Perth"

pete_password = "44693522"
pete_balance = "Balance[$23821.76]"
pete_name = "Pete .D"
pete_personal = "Pete Dale \nGreen Triangle Rank \n---------------------- \nMember since: 2/Jan/1999 \nExpiry:       5/Oct/2027 \n---------------------- \nDoB:        5/Jan/1982 \nOccupation: Unemployed \nHome Town:  Sydney"




file_name = input("Enter the file name:")
try:
    with open(file_name, 'r') as keycard:
        content = keycard.read()
        print("\nKey Card loaded successfully")
        
        uid_found = None
        for line in content.splitlines():
            if line.startswith("UID:"):
                uid_found = line.split("UID:")[1].strip()
                break
        
        bruce_uid = "04 4E 6F AD A2 76 4C"
        pete_uid = "04 3D 38 89 C2 FE 4A"
        
        if uid_found is None:
            print("Error: Not a vaild .nfc file")
            sys.exit(1)
                  
        elif bruce_uid == uid_found:
            user_password = bruce_password
            user_balance = bruce_balance
            user_name = bruce_name
            user_personal = bruce_personal
        elif pete_uid == uid_found:
            user_password = pete_password
            user_balance = pete_balance
            user_name = pete_name
            user_personal = pete_personal
                    
        print("")
        
        attempts = 3
        while attempts > 0:
            passcode = input("Please enter your pass-code: ")
            if passcode == user_password and user_password != None:
                print("Card and Pass accepted")
                print("----------------------")
                print("Welcome " + user_name)
                    
                while True:
                    print("")
                    print("Please select from the following options")
                    option = input("[1] Check details, [2] Check balance, [3] Exit: ")
                    print("--------------------------------------------")
                    print("")
                        
                    if option == "1":
                        print(user_personal)
                    elif option == "2":
                        print(user_balance)
                    elif option == "3":
                        print("Exited")
                        break
                    else:
                        print("Invalid option. Please try again.")
                break 
            else:
                attempts -= 1
                print(f"Error: Keycard and pass-code do not match. {attempts} attempts remaining.")
                if attempts == 0:
                    print("Access denied. Too many failed attempts.")
                    sys.exit(1)
        
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An internal file error occurred: {e}")

print()
input("Press Enter to close the program")
