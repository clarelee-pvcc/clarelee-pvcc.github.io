# Name: Clare Lee
# Prog Purpose: This program calculate personal property tax for vehicles in
# Charlottesville VA. It displays a tax bill for the amount owed,
# given the information below. The program should loop.

import datetime

#define rates
TAX_RATE = .042
TAX_RELIEF = .33

#define global variables
vehicle_value = 0
eligible_tax_relief = ""
assessed_value = 0
relief_amount = 0
annual_tax = 0
six_month_tax = 0


#############define program functions ########
def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()

def get_user_data():
    global vehicle_value,  relief_yesno

    print('Personal property tax rate     4.2% per year')
    print('Tax relief for qualified vehicles        33%')

    vehicle_value= int(input("Assessed value of the vehicle? "))
    relief_yesno= input("\nEligible for tax relief (Y or N)? ")
    relief_yesno = relief_yesno.upper()

def perform_calculations():
    global annual_tax, vehicle_value, six_month_tax, eligible_tax_relief, total_due
    annual_tax = vehicle_value * TAX_RATE
    six_month_tax = annual_tax / 2
   
    if relief_yesno == "Y":
        eligible_tax_relief = six_month_tax * TAX_RELIEF
    else:
        eligible_tax_relief = 0

    total_due = six_month_tax - eligible_tax_relief

def display_results():
    
    print('----------------------------------')
    print('******** City of Charlottesville, Virginia ********')
    print('-------------Personal Property Tax----')
    print('----------------1st Half 2024----')
    print('Assessed Value of the vehicle          $ ' + format(vehicle_value,"8,.2f"))
    print('Full annual amount owed                $ ' + format(annual_tax,"8,.2f"))
    print('Relief amount                          $ ' + format(eligible_tax_relief,"8,.2f"))
    print('Total due                              $ ' + format(total_due,"8,.2f"))
    print('----------------------------------')
    print(str(datetime.datetime.now()))

########### call on main program to execute ##########
main()
    
