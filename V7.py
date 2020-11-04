#needed for sys.exit()
import sys

#needed definitions and values
total_price = 0
delivery_charge = 0
method = 0

#needed definitions and values
value_pizza_ordered = []
value_ordered_menu = []
gourmet_pizza_ordered = []
gourmet_ordered_menu = []
delivery_address = []

#value menu with prices ($8.50)
#gourmet menu with prices ($13.50)
#full menu with prices
value_menu=[("Simple Cheese",8.50),("Pepperoni",8.50),("Cheesy Garlic",8.50),("Hawaiian",8.50),("Vege Trio",8.50),("Ham & Cheese",8.50),("Beef & Onion",8.50),("BBQ Pork & Onion",8.50)]
gourmet_menu=[("Chicken, Bacon & Aioli",13.50),("Chicken, Bacon & Avocado",13.50),("Mega Meatlovers",13.50),("Peri-Peri Chicken",13.50),("Garlic Prawn",13.50)]
full_menu=[("Simple Cheese",8.50),("Pepperoni",8.50),("Cheesy Garlic",8.50),("Hawaiian",8.50),("Vege Trio",8.50),("Ham & Cheese",8.50),("Beef & Onion",8.50),("BBQ Pork & Onion",8.50),("Chicken, Bacon & Aioli",13.50),("Chicken, Bacon & Avocado",13.50),("Mega Meatlovers",13.50),("Peri-Peri Chicken",13.50),("Garlic Prawn",13.50)]


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

#while loops make it so the user must give a valid input
#blank input is deemed invalid > user feedback
#input with a length of more than 9 is deemed invalid > user feedback
#input with a length of less than 9 is deemed invalid > user feedback
#if input is valid > program prints number back to user (user feedback)
        while True:
            phone_number = input("What is your phone number? Please use the format 0XXXXXXXX (maximum of 9 characters)\n")
            if len(phone_number) > 9:
                print("Sorry but the number you have entered is greater than 9 characters, Try again please")
            elif len(phone_number) < 9:
                print("Sorry but the number you have entered is less than 9 characters, Try again please")
            else:
                print("Great!, The phone number you chosen to use for your order is {}\n".format(phone_number))
                break
            
#if method = 2 (pickup) > skips to phone number prompts
#while loops make it so the user must give a valid input
#blank input is deemed invalid > user feedback
#input with a length of more than 9 is deemed invalid > user feedback
#input with a length of less than 9 is deemed invalid > user feedback
#if input is valid > program prints number back to user (user feedback)        
    if method == 2:
        while True:
            phone_number = input("What is your phone number? Please use the format 0XXXXXXXX\n")
            if len(phone_number) > 9:
                print("Sorry but the number you have entered is greater than 9 characters, Try again please")
            elif len(phone_number) < 9:
                print("Sorry but the number you have entered is less than 9 characters, Try again please")
            else:
                print("Great!, The phone number you chosen to use for your order is {}\n".format(phone_number))
                break

#tells the user that there are 2 pizza ranges - value range and the gourmet range
#program also tells user that there is a maximum of 5 pizzas allowed for an order
        print("note that we have 2 ranges of pizzas:\n * the value pizza range \n * the gourmet pizza range.\n The maximum amount of pizzas for an order is 5\n")

#asks the user how many value pizzas they would like to order
#while loops make it so the user must give a valid input
#blank input is deemed invalid > user feedback
#input must be a value between 1 and 5 > if not = invalid > user feedback
#if value is not an integer > it is deemed invalid > loop does not break > user feedback
    while True:
        try:
            value_pizza_amount = int(input("How many value range pizzas would you like to order? \n *there is a max limit of 5 total pizzas: \n"))
            assert 0 <= value_pizza_amount <= 5
            print("you have chosen to order {} value pizza(s)\n".format(value_pizza_amount))
        except ValueError:
            print("Sorry but I don't understand.")
        except AssertionError:
            print("Sorry but I don't understand.")
        else:
            break

#number of value pizzas must be between 1 and 4 > otherwise invalid and the user is unable to order a gourmet pizza        
#asks the user how many gourmet pizzas they would like to order
#while loops make it so the user must give a valid input
#blank input is deemed invalid > user feedback
#calculations are done to calculate if their are more than 5 pizzas being ordered
        #if 5 or more total pizzas > deemed invalid > user feedback
        #if 4 or less total pizzas > valid > user feedback
    if 0 <= value_pizza_amount <= 4:
        while True:
            gourmet_pizza_amount = int(input("How many gourmet range pizzas would you like to order? \n"))
            total_pizza_amount = gourmet_pizza_amount + value_pizza_amount
            if total_pizza_amount > 5:
                print("Sorry but you must input a valid number of  pizzas. 5 is the maximum amount of pizzas for one order.")
            elif gourmet_pizza_amount >= 0:
                print("you have chosen to order {} gourmet pizza(s)\n".format(gourmet_pizza_amount))
                break

#value menu is displayed to the user
#the user is able to pick the desired amount of value pizzas from the list by using their associated numbers
#chosen value pizzas is then added to a list
#chosen value pizza(s) is displayed back to the user
#if chosen pizza amount is 1 or greater than user is able to pick from the menu
#if chosen pizza amount is 0 than the user is not able to pick from the menu and is skipped

    if value_pizza_amount >= 1:
        def display(value_menu):
            counter = 0
            for value_pizza_number in value_menu:
                counter += 1
                value_pizza_ordered.append(value_pizza_number)
                print("%s. %s" % (counter, value_pizza_number))
            return value_pizza_ordered

        def get_list(value_pizza_ordered):
            print("\nPress the associated number with the *value* pizza you wish to order:")
            for n in range(value_pizza_amount):
                choose = input()
                choice = int(choose)-1
                print("You have chosen to order a: ")
                print(value_pizza_ordered[choice])
                print("")
                
                value_ordered_menu.append(value_pizza_ordered[choice])

        value_pizza_ordered = display(value_menu)
        get_list(value_pizza_ordered)

#gourmet menu is displayed to the user
#the user is able to pick the desired amount of gourmet pizzas from the list by using their associated numbers
#chosen gourmet pizzas is then added to a list
#chosen gourmet pizza(s) is displayed back to the user
#if chosen pizza amount is 1 or greater than user is able to pick from the menu
#if chosen pizza amount is 0 than the user is not able to pick from the menu and is skipped

    if gourmet_pizza_amount >= 1:
        def display(gourmet_menu):
            counter = 0
            for gourmet_pizza_number in gourmet_menu:
                counter += 1
                gourmet_pizza_ordered.append(gourmet_pizza_number)
                print("%s. %s" % (counter, gourmet_pizza_number))
            return gourmet_pizza_ordered

        def get_list(gourmet_pizza_ordered):
            print("\nPress the associated number with the *gourmet* pizza you wish to order:")
            for n in range(gourmet_pizza_amount):
                choose = input()
                choice = int(choose)-1
                print("You have chosen to order a: ")
                print(gourmet_pizza_ordered[choice])
                print("")
                
                gourmet_ordered_menu.append(gourmet_pizza_ordered[choice])

        gourmet_pizza_ordered = display(gourmet_menu)
        get_list(gourmet_pizza_ordered)

#pizza amounts are multiplied by their prices
#pizzas are then added and stored
#total price of the order is displayed back to the user

    value_pizza_cost = value_pizza_amount * 8.50
    gourmet_pizza_cost = gourmet_pizza_amount * 13.50
    total_price = value_pizza_cost + gourmet_pizza_cost + delivery_charge
