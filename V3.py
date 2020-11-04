#needed for sys.exit()
import sys

#needed definitions and values
delivery_charge = 0
method = 0

#needed definitions and values
delivery_address = []

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

#asks for the method of the order
#if 1 is pressed > order is delivery > goes to address input prompts > user feedback is given
#if 2 is pressed > order is pickup > skips the address input prompts
#if 3 is pressed > order is cancelled and program exits > user feedback is given
    method = int(input("Hello {}. Is this order a delivery or pickup? \n * press 1 for delivery \n * press 2 for pickup \n * or press 3 to cancel the order \n".format(user_name)))
    if method == 3:
        print("Haere rā - Please come again soon!")
        sys.exit()
         
    if method == 1:
        print("You have chosen delivery. A $3 surchage has been added to your total bill\n")
#adds $3 to delivery charge > used later on in the order to calculate total price
        delivery_charge=delivery_charge+3
        
#asks the user for the delivery address - asks for house number and road name

#asks user for house number        
#while loops make it so the user must give a valid input
#blank input is deemed invalid
        print("For the delivery address we use this following format: \n* House Number, Road,\n")

        while True:
            house_number = input("What is the house number?\n")
            if house_number:
                break
            else:
                print("Sorry but I don't understand.")

#asks user for road name       
#.title() makes the first letter capitlised
#.strip() removes any trailing blank characters
#str is used because we will be combining the house no. and road name into a single address
#while loops make it so the user must give a valid input
#blank input is deemed invalid > user feedback
        while True:
            road_name = str(input("What is the road name?\n")).title().strip()
            if road_name:
                break
            else:
                print("Sorry but I don't understand.")
            
#formats the collected delivery information into a single address - which is then displayed back to the user
        delivery_address = (house_number) + ' ' + (road_name)
        print("You have chosen to deliver to {} \n".format(delivery_address))
