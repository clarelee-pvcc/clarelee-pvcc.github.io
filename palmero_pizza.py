# Name: Clare Lee
# Prog Purpose: This program finds the cost of a meal at Palermo Pizza

import datetime

######### define global variables ###########
#STUDENTS: CLARE LEE

PRICE_SMALL = 9.99 
PRICE_MED = 12.99
PRICE_LARGE = 17.99
PRICE_EXTRA_LARGE = 21.99
DRINKS = 3.99
BREADSTICKS = 6.99
SALES_TAX_RATE = .055

 # define global variables
num_pizzas = 0
num_drinks = 0 
num_breadsticks = 0
cost_pizzas=0 
cost_drinks = 0
cost_breadsticks = 0 
subtotal = 0
sales_tax = 0
total = 0

##################define program functions ##################
def main():
        
        more = True
        
        while more:
                get_user_data()
                perform_calculations()
                display_results()

        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno.upper() == "N":
                more = False
                print("Thank you for your order. Enjoy your pizza!")
             
def get_user_data():
        global pizza_size, num_pizzas, num_drinks, num_breadsticks

        print('******* Palermo Pizza *******')
        print('s Small Pizza          $  9.99')
        print('M Medium Pizza         $ 12.99')
        print('L Large Pizza          $ 17.99')
        print('X Extra Large Pizza    $ 21.99')
    
          
        pizza_size = input("\nwhat size pizza would you like to order? (S, M, L, XL): ")
        pizza_size = pizza_size.upper()
          
        num_pizzas = int(input("Number of pizzas: "))
        num_drinks = int(input("Number of drinks: "))
        num_breadsticks = int(input("Number of breadstick orders: "))
                         
def perform_calculations():
        global cost_pizzas, cost_drinks, cost_breadsticks, subtotal, sales_tax, total
        if pizza_size == "S":
                cost_pizzas = num_pizzas * PRICE_SMALL
        elif pizza_size == "S":
                cost_pizzas = num_pizzas * PRICE_SMALL
        if pizza_size == "M":
                cost_pizzas = num_pizzas * PRICE_MED
        elif pizza_size == "M":
                cost_pizzas = num_pizzas * PRICE_MED
        if pizza_size == "L":
                cost_pizzas = num_pizzas * PRICE_LARGE
        elif pizza_size == "L":
                cost_pizzas = num_pizzas * PRICE_LARGE
        if pizza_size == "X":
                cost_pizzas = num_pizzas * PRICE_EXTRA_LARGE
        elif pizza_size == "X":
                cost_pizzas = num_pizzas * PRICE_EXTRA_LARGE
              
        cost_drinks = num_drinks * DRINKS
        cost_breadsticks = num_breadsticks * BREADSTICKS
        subtotal= cost_pizzas + cost_drinks + cost_breadsticks
        sales_tax = subtotal * SALES_TAX_RATE
        total = subtotal + SALES_TAX_RATE
             
def display_results():
        currency = "8,.2f"
        line = '-----------------------------'
        full_date = str(datetime.datetime.now())
        short_date= full_date [0:16]
        
        print(line)
        print('******* Palermo Pizza ******')
        print(short_date)
        print(line)
        print('Number of pizzas ordered: '+ str(num_pizzas))
              
        print(line)
        print('Pizzas        $ ' + format(cost_pizzas,currency))
        print('DRINKS        $ ' + format(cost_drinks,currency))
        print('BREADSTICKS   $ ' + format(cost_breadsticks,currency))
        print('Subtotal      $ ' + format(subtotal,currency))
        print('Sales Tax     $ ' + format(sales_tax,currency))
        print('Total         $ ' + format(total,currency))
        print('----Enjoy!-------')
        print(str(datetime.datetime.now()))

########### call on main program to execute ##########
main()
