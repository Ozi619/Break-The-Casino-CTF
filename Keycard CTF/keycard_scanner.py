print("Offline Member Card Scanner")
print("-----------------------")
print()
print("no card reader attached")
print()
print("Please load a card by entering the file name")
print("Example KC_239_Ricky.nic")

file_name = input("Enter the file name:")
try:
    with open(file_name, 'r') as keycard:
        content = keycard.read()
        print("\nKey Card loaded successfully")
        attempts = 3
        while attempts > 0:
            passcode = input("Please enter your pass-code: ")
            if passcode == "76544567":
                print("Card and Pass accepted")
                print("----------------------")
                print("Welcome Bruce.B")
                    
                while True:
                    print("")
                    print("Please select from the following options")
                    option = input("[1] Check details, [2] Check balance, [3] Exit: ")
                        
                    if option == "1":
                        print("Bruce Buggins")
                        print("Gold Square Rank")
                        print("------------------------")
                        print("Member since: 12/Aug/1955")
                        print("Expiry:       12/Feb/2008")
                        print("------------------------")
                        print("DoB:        29/Jan/1935")
                        print("Occupation: Cricketer - Machine Operator")
                        print("Home Town:  Perth")
                    elif option == "2":
                        print("Balance[$700023.23]")
                    elif option == "3":
                        print("Exited")
                        break
                    else:
                        print("Invalid option. Please try again.")
                break
            else:
                attempts -= 1
                print(f"Incorrect passcode. {attempts} attempts remaining.")
            
            if attempts == 0:
                print("Access denied. Too many failed attempts.")
            break
        
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An file internal error occurred: {e}")




print()
file_name = input("Press Enter to close the program")
