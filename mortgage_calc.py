# -*- coding: utf-8 -*-
"""
Created on Sun May 23 16:02:02 2021

@author: echua
"""
# Import packages
import pandas as pd
import matplotlib.pyplot as plt

# This is a mortgage loan calculator

loan_amount = float(input('Please input loan amount ($): '))
loan_year = float(input('Please input loan period (years): '))
loan_month = int(loan_year * 12)
interest_year = float(input('Please input annual interest rate (%): '))
interest_month = interest_year / 100 / 12

# Formula to calculate monthly repayment
month_payment = loan_amount * ((interest_month * (1 + interest_month) ** loan_month) / (((1 + interest_month) ** loan_month) -1))
month_payment = round(month_payment,2)

print('')
print('Your monthly payment is $' + str(month_payment))

# Plot
month = []
remaining_amount = []
for i in range(1,loan_month+1):
    interest = loan_amount * interest_month
    loan_amount = loan_amount - (month_payment - interest)
    month.append(i)
    remaining_amount.append(loan_amount)

plt.plot(month, remaining_amount,'ro')
plt.xlabel('Month')
plt.ylabel('Remaining Amount ($)')
plt.show()