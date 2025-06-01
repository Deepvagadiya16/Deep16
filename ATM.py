print("\n\n----------------Hello Welcome to our ATM----------------\n\n")

print("\n\n----------------ATM MENU----------------\n\n")
print("1. Balance Enquiry")
print("2. Cash Withdrawal")
print("3. Cash Deposit")
print("4. Change Password")
print("5. Exit")

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, welcome to our ATM. Please follow the instructions on the screen.")
engine.runAndWait()

# Initial password
password = "1234"
# User input for password
Password = input("Enter your password: ")

if Password ==  password:
    while True :
            
            choice = int(input("Enter your choice:"))
            # Balance enquiry.
            
            if choice == 1:
                balance = 10000  # Example balance
                print(f"Your account balance is: {balance} INR")  # Example balance
                print("Thank you for using our ATM.")
                engine.say(f"Your account balance is: {balance} INR")
                engine.runAndWait()
            #Case withdrawal.
            elif choice == 2:
                amount = int(input("Enter the amount to withdraw:"))
                print(f"You have withdrawn {amount} INR")
                print("Please collect your cash.")  
                balance = balance - amount # final belance 
                print(f"Your balance is now:{balance} INR")
                engine.say(f"You have withdrawn {amount} INR. Your balance is now {balance} INR.\nPlease collect your cash.")
                engine.runAndWait()
            #Case deposit.
            elif choice == 3:
                amount = int(input("Enter the amount to deposit:"))
                print(f"You have deposited {amount} INR")
                print("Your deposit is successful!")
                balance = balance + amount  # final balance
                print(f"Your balance is now: {balance} INR")
                engine.say(f"You have deposited {amount} INR. Your balance is now {balance} INR.")
                engine.runAndWait()
            #Chenge password    
            elif choice == 4:
                new_password = input("Enter your new password: ")
                confirm_password = input("Confirm your new password: ")
                if new_password != confirm_password:
                    engine.say("Passwords do not match. Password not changed.")
                    engine.runAndWait()
                    print("Passwords do not match. Password not changed.")
                elif new_password.strip() == "":
                    engine.say("Password cannot be empty.")
                    engine.runAndWait()
                    print("Password cannot be empty.")
                else:
                    password = new_password
                    engine.say("Password changed successfully!")
                    engine.runAndWait()
                    print("Password changed successfully!")

                # Ask user to re-enter password
                entered_password = input("Re-enter your new password to confirm login: ")
                if entered_password == password:
                    engine.say("Password confirmed. You are logged in.")
                    engine.runAndWait()
                    print("Password confirmed. You are logged in.")
                    continue  # back to main menu
                else:
                    engine.say("Incorrect password. Access denied.")
                    engine.runAndWait()
                    print("Incorrect password. Access denied.")

                    break 
            elif choice == 5:
                print("Thank you for using our ATM. Goodbye!")
                engine.say("Thank you for using our ATM. Goodbye! ")
                engine.runAndWait()
                break
            else:
                print("Invalid choice, please try again.")