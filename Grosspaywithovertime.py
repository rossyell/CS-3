# Prompt the user for hours and rate per hour to compute gross pay
work_hours = 40.00
loading = 1.5
# Capture, convert to float and determine if numbers.
hours = input("Enter work Hours: ")
try:
    worked_hours = float(hours)
except:
    print("Please only enter numbers")
#
rate = input("Enter basic Rate/hour: ")
try:
    basic_rate = float(rate)
except:
    print("Please only enter numbers")
# Determine if working greater than 40 hours, determine amount over and pay
if worked_hours > work_hours:
    overtime = worked_hours - work_hours
    overtime_pay = overtime * basic_rate * loading
    standard_pay = work_hours * basic_rate
    tot_pay = overtime_pay + standard_pay
else:
    tot_pay = worked_hours * basic_rate
# this function will round and print the result
print("Total pay is ", tot_pay)
#round(tot_pay,2)