def main():
    #Accepts input for variable assignment
    payrate = int(input("What is the payrate? "))
    hours = int(input("How many hours were worked? "))
    taxRate = int(input("What is the tax rate?")
    #Performs calculations and assigns them to different variables
    grossPay = payrate * hours
    taxesPaid = grossPay * taxRate
    netPay = grossPay - taxesPaid
    #Returns the result of calculations
    print("The grossPay is ", grossPay)
    print("The taxes paid is", taxesPaid)
    print("The net pay is", netPay)

    
main()

"""
Author: Nick Zwan
01/22/19
"""

    
