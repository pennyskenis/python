import sys

#welcomes the user to henderson pizza palace
#asks the user if they would like to begin the order
#if 0 is pressed, > the program exits
#if 1 is pressed > the program begins and moves onto the next prompt
while True:
    start = int(input("Welcome to Henderson Pizza Palace!\n * press 1 to begin your order\n * press 0 to cancel your order\n"))

    if start == 0:
        print("Haere rā - Please come again soon!")
        sys.exit()
        
    if start == 1:

#name of the user is asked
#.title() makes the first letter capitlised
#.strip() removes any trailing blank characters

#if user input is blank > loop continues > user feedback is given
#if user inputs a name > loop breaks
     while True:
         user_name = input("Kia Ora! What is your name?\n").title().strip()
         if user_name:
             break
         else:
                print("Sorry but I don't understand.")
