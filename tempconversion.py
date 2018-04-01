# Prompt the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature
celsius = input("Enter the temperature in Deg. Celsius: ")
# use formula f = c x 9/5 + 32 - change order in function for clarity
fahrenheit = (9 * float(celsius) / 5) + 32
# round to two decimal places and print
print(round(fahrenheit,2))