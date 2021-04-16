"""
    File: Assignment 4.1. py
    Author: Aritzi Piedras-Silva
    Date: 09/20/2019
    course: DSC 510 - Introduction to programing
    Desc: This program will calculate the installation price for fiber optic cable
    Usage: This program will welcome the user followed by asking for the name of business
    as well as the length in square feet needed for fiber optic cable
    Default rate is $0.80
    > 100 feet : $0.87
    < 100 feet and >=250 feet : $0.80
    <=250 feet and > 500 feet: $0.70
    >500 feet : $0.50
    This program will also introduce the concept of functions

"""
# Display Welcome Message
print('Welcome To My Program!!!')

#new function with parameters
def total_cost(feet, price):
    feet = int(feet)
    if feet <= 100:
        price = price
    elif feet > 500:
        feet = price * 0.50
    elif feet > 250:
        feet = price * 0.70
    elif feet > 100:
        feet = price * 0.80
    print('\n', '--------------------FINAL RECEIPT--------------------\n',
          'Total in length to be installed:    ', feet, 'ft \n',
          'Total Cost: $',price,'\n'
          '\n', '--------------------FINAL RECEIPT--------------------\n')



# Company Name will be prompted
company = input('Please Enter Your Company Name:')

# This will pull the total of feet and the cost per feet
try:
    #this will ask how many feet will be need in the company
    total_feet = input('How many Feet Do You Want Installed In' + company + ':')
    total_price = int(total_feet) * 0.87
    total_cost(total_feet,total_price)
    # this will correct and re-ask any type of mistake by the user
except:
    print('Invalid! please enter a number')
    total_feet = input('How many Feet Do You Want Installed In' + company + ':')
    total_price = int(total_feet) * 0.87
    total_cost(total_feet,total_price)


