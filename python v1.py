total_price = 0
delivery_charge = 0
method = 0
index = 0
pizza_ordered = [] 

#pizza menu
menu=[("1. Simple Cheese",8.50),("2. Pepperoni",8.50),("3. Cheesy Garlic",8.50),("4. Hawaiian",8.50),("5. Vege Trio",8.50),("6. Ham & Cheese",8.50),("7. Beef & Onion",8.50),("8. BBQ Pork & Onion",8.50),("9. Chicken, Bacon & Aioli",13.50),("10. Chicken, Bacon & Avocado",13.50),("11. Mega Meatlovers",13.50),("12. Peri-Peri Chicken",13.50),("13. Garlic Prawn",13.50)]
#pizzas ordered
pizza_ordered=[]

#ask the user if they would like to begin the pizza order process
start = int(input("Welcome to Henderson Pizza Palace!\n * press 1 to begin your order\n * press 0 to cancel your order\n"))

#exits the process if the user presses 0
if start == 0:
    print("Please come again soon!")
    exit
#start the process if the user presses 1
if start == 1:
#ask for the user name and stores it for later use
 user_name = input("Greetings! What is your name?\n").title()
 #ask user for their order method type eg. delivery or pickup
 method = int(input("Hello {}. Is this order a delivery or pickup? \n * press 1 for delivery \n * press 2 for pickup \n * press 3 to cancel the order\n".format(user_name)))

#display the order type message & informs the user of the added surcharge of delivery orders
if method == 1:
    print("You have chosen delivery. A $3 surchage has been added to your total bill\n")
    #adds $3 dollars to the delivery charge
    delivery_charge=delivery_charge+3
    
#ask for the delivery address
#gathers the delivery address information. house no. road name, suburb name, city name
    print("For the delivery address we use this following format: \n House no. Road, Suburb, City, \n")
    house_number = str(input("What is the house number?\n"))
    road_name = str(input("What is the road name?\n")).title()
    suburb_name = str(input("What is the name of the suburb?\n")).title()
    city_name = str(input("What is the name of the city?\n")).title()

#print the users chosen delivery address
#condenses the users delivery address information into a single variable
    delivery_address = (house_number) + ' ' + (road_name) + ' ' + (suburb_name) + ' ' + (city_name)
    print("You have chosen to deliver to {} \n".format(delivery_address))

#asks for the users phone number
    phone_number = input("What is your phone number? Please use the format 0X XXX XXXX\n")
    print("The phone number you chosen to use for your order is {}".format(phone_number))

#display the order type message : pickup
if method == 2:
    print("You have chosen pickup.")

#ask the user how many value pizzas they would like to order
    print("\nnote that we have 2 ranges of pizzas: the value pizza range and the gourmet pizza range. Also the maximum pizzas for an order is 5 - This includes both value and gourmet range of pizzas.\n")
    value_pizza_amount = int(input("How many value range pizzas would you like to order? \n *there is a max limit of 5 total pizzas: \n"))

#checks if the amount of pizzas wanted by the user is valid
    if value_pizza_amount >= 1 or value_pizza_amount <= 5:
     print("you have chosen to order {} value pizza(s)\n".format(value_pizza_amount))
     
#any value equal or lesser than 0 is invalid
#any value equal or greater than 6 is invalid
    elif value_pizza_amount <= 0 or value_pizza_amount >= 6 :
     print("Sorry but you must input a valid number of  pizzas")

#ask the user how many gourmet pizzas they would like to order
     if value_pizza_amount >= 1 or value_pizza_amount <= 5:
         gourmet_pizza_amount = int(input("How many gourmet range pizzas would you like to order? \n"))
    
#calculates the total number of pizzas that the user wants
#if the total pizza amount is equal or greater than 6 than the user must input a correct number of pizzas
    total_pizza_amount = gourmet_pizza_amount + value_pizza_amount
    if total_pizza_amount >= 6:
              print("Sorry but you must input a valid number of  pizzas. 5 is the maximum amount of pizzas for one order.")
    if gourmet_pizza_amount >= 1:
        print("you have chosen to order {} gourmet pizza(s)\n".format(gourmet_pizza_amount))


        pizza_ordered = []
#displays pizza menu in a descending line, starting from [1] and ending at [13]
    while index <len(menu):
        print(menu[index])
        index=index+1
#ask user the value pizza that they would like to order
    for n in range(value_pizza_amount):
        value_pizza_number = int(input("\n*note that you are now ordering a value pizza. Press the associated number to select the value pizza you would like to order:\n"))
        pizza_ordered.append(value_pizza_number) # add input to the list

#ask the user if they would like to add extra toppings to the chosen pizza
        value_extra = int(input("\n Would you like to add extra toppings to your pizza? \n * press (1) to add extra toppings\n * press (2) to NOT add extra toppings\n"))
        if value_extra == 1:

#ask user the gourmet pizza that they would like to order
            for n in range(gourmet_pizza_amount):
                gourmet_pizza_number = int(input("\n*note that you are now ordering a gourmet pizza. Press the associated number to select the gourmet pizza you would like to order:\n"))
        pizza_ordered.append(gourmet_pizza_number) # add input to the list

#ask the user if they would like to add extra toppings to the chosen pizza
        gourmet_extra = int(input("\n Would you like to add extra toppings to your pizza?\n * press (1) to add extra toppings\n * press (2) to NOT add extra toppings\n"))
        if gourmet_extra == 1:
            print("You have chosen to add extra toppings to this pizza")
            total_price + 0.5
            

            print("You have chosen to order pizza(s) {} \n".format(pizza_ordered))
        
    value_pizza_cost = value_pizza_amount * 8.50
    gourmet_pizza_cost = gourmet_pizza_amount * 13.50

    total_price = value_pizza_cost + gourmet_pizza_cost + delivery_charge
    print("\nYour order comes out to a total of ${} ".format(total_price))
