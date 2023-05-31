''' This Python program that will allow the user to access to different finantial calculators: 
an investment calculator and a home loan repayment calculator'''
import math

# displaying choices for user
print("investment - to calculate the amount of interest you'll earn on your investment") 
print("bond       - to calculate the amount you'll have to pay on a home loan")
menu = input("Enter either 'investment' or 'bond' from the menu above to proceed: ") # ask user choose between investment and bond

option_1 = "investment"
option_2 = "bond"


if menu == option_1: # user choose investments 
    deposit = int(input("Please enter a deposit : ")) 
    the_interest = int(input("Please enter an interest rate : ")) 
    year = int(input("Please enter the number of the year you plan on investing : "))

    intrest_in_per = the_interest/100 # interest rate divided by 100%, if 8% is entered than r is 0.08%

    simp_intrest = deposit*(1+intrest_in_per*year) # calculation of simple interest
    comp_intrest = deposit* math.pow((1+intrest_in_per),year) # calculation of compound interest 
    
    interest = input("Do you want 'simple' or 'compound' interest ? ") # asks user to choose between simple or compound interest
    
    if interest == "simple":
        print(simp_intrest) # prints out the result of calculation (simple investment)
    elif interest == "compound":
        print(comp_intrest) # prints out the result of calculation (compound investment)
    else:
        print ("Enter your choice")
elif menu == option_2: # user choose bond
    value = int(input("Enter value of the house : ")) 
    intrest_rate = int(input("Enter interest rate : ")) 
    months = int(input("Enter number of months you plan to repay the bond : "))
    
    i = (intrest_rate / 100) / 12 # interest rate divided by 100, if 8% is entered than it is 0.08% and anual interest rate divided by 12
    
    repayment = (i * value)/(1 - (1 +i)**(-months)) # calculation of repayment
    print(repayment) # prints out the amound of repayment

else:
   print("Please enter one of the options below") # if user didn't enter the words "investment" or "bond" 