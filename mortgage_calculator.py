# Filename : mortgage_calculator.py

# Calculate the monthly payments of a fixed term mortgage over given Nth terms
# at a given interest rate. Also figure out how long it will take the user
# to pay back the loan. For added complexity, add an option for users to
# select the compounding interval (Monthly, Weekly, Daily, Continually).

import math

def calc_mortgage(principal, interest, years):
    '''
    given mortgage loan principal, interest(%) and years to pay
    calculate and return monthly payment Amount
    '''
    # monthly rate from annual percentage rate
    interest_rate = interest/(100 * 12)
    # total number of payments
    payment_num = years * 12
    # calculate monthly payment
    payment = principal * (interest_rate/(1-math.pow(1+interest_rate), (-payment_num)))
    return payment

# mortgage loan principal
principal = 100000
# percent annual interest
interest = 7.5
# years to pay off mortgage
years = 30
# calculate monthly payment Amount
monthly_payment = calc_mortgage(principal, interest, years)
# calculate total amount paid
total_amount = monthly_payment * years * 12

# show result ...
# {:,} uses the comma as a thousands separator
sf = '''
for a {} year mortgage loan of ${:,}
at an annual interest rate of {:.2f}%
you pay ${:.2f} monthly'''
print(sf.format(years, principal, interest, monthly_payment))
print('_'*40)
print("Total amount paid will be ${:,.2f}".format(total_amount))

''' result...
For a 30 Year mortgage loan of $100,100000at an annual interest rate of 7.50%
you pay $699.21 monthly
Total amount paid will be $251,717.22
'''
