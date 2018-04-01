# Prompt the user for hours and rate per hour to compute gross pay
hours = input("Enter work Hours: ")
rate = input("Enter work Rate/hour: ")
# convert both values to float to account for decimals
pay = float(hours) * float(rate)
# this function will round and print the result
round(pay,2)