# Name: Clare Lee
# Prog Purpose: This program finds PVCC college tuition & fees based on number of credits
# PVCC Fee Rates are from # https://www.pvcc.edu/tuition-and-fees
#   The output is sent to an .html file

import datetime

##############  define global variables ############
# define tax rate and prices
RATE_TUITION_IN = 146.26
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.5
RATE_INSTITUTION_FEE= 1.75
RATE_ACTIVITY_FEE = 2.9

# define global variables
inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarship_amt = 0

tuition_amt = 0
inst_fee = 0
cap_fee = 0
act_fee = 0
total = 0
balance = 0

# create output file
outfile = 'tuition-webpage.html'


##############  define program functions ################
def main():
    
    open_outfile()
    more = True
    
    while more:
        get_user_data()
        perform_calculations()
        create_output_file()
        
        askAgain = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if askAgain.upper() == 'N':
            more_tickets = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> PIEDMONT VIRGINIA COMMUNITY COLLEGE Tuition & Fees </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #B3B3F1; background-image: url(wp-tuition.png); color: #B15E6C;">\n')
    
def get_user_data():
    global inout, numcredits, scholarshipamt
    inpout = int(input("Enter a 1 for IN-STATE ; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered  for: "))
    scholarship_amt =  int(input("Scholarship amount received: "))    

def perform_calculations():
    global tuition, inst_fee, cap_fee, act_fee, total, balance
    if inout == 1:
            tuition = numcredits * RATE_TUITION_IN
            cap_fee = numcredits * RATE_CAPITAL_FEE
            act_fee = numcredits * RATE_ACTIVITY_FEE
            inst_fee = numcredits * RATE_INSTITUTION_FEE
            total = tuition + cap_fee + act_fee + inst_fee
            balance = total - scholarship_amt

    else:
            tuition = numcredits * RATE_TUITION_OUT
            cap_fee = numcredits * RATE_CAPITAL_FEE
            act_fee = numcredits * RATE_ACTIVITY_FEE
            inst_fee = numcredits * RATE_INSTITUTION_FEE
            inst_fee = RATE_INSTITUTION_FEE * numcredits
            total = tuition + cap_fee + act_fee + inst_fee
            balance = total - scholarship_amt

        
def create_output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "3">'
    sp = " "

    f.write('\n<table border="3"   style ="background-color: #CEC2FF;  font-family: arial; margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2>******PIEDMONT VIRGINIA COMMUNITY COLLEGE*****</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('******* Tuition & Fees ********\n')
    
    f.write(tr + 'tuition' + endtd + str(numcredits) + endtd + format(tuition_amt,currency) + endtr)
    f.write(tr + 'scholarship_amt' + endtd + str(numcredits) + endtd + format(scholarship_amt,currency) + endtr)
    f.write(tr + 'activity fee ' + endtd + str(numcredits) + endtd +  format(act_fee,currency)  + endtr)

    f.write(tr + 'cap fee' +  endtd + sp + endtd + format(cap_fee,currency)  + endtr)     
    f.write(tr + 'institutional fee' + endtd + sp + endtd + format(inst_fee,currency) + endtr)
    f.write(tr + 'TOTAL' +     endtd + sp + endtd + format(total,currency) + endtr)
    
    f.write(colsp + 'Date/Time: '+ day_time + endtr)
    f.write('</table><br />')


##########  call on main program to execute ############
main()              

