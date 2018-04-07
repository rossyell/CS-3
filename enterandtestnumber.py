# A program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message otherwise 
number = input("Please enter a number between 0.0 and 1.0: ")
try:
    clean_number = float(number)
except:
    print("Bad Score - Please only enter numbers")
# To check if out of range
if clean_number > 1.0 and clean_number < 0.0:
    print("Bad score - number is out of range")
elif clean_number >= 0.9:
    print("A")
elif clean_number >= 0.8:
    print("B")
elif clean_number >= 0.7:
    print("C")
elif clean_number >= 0.6:
    print("D")
else:
    print("F")
print("end of grading")