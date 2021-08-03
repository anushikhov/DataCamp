savings = 100
growth_multiplier = 1.1
desc = "compound interest"
result = 100 * 1.10 ** 7

# Assign product of growth_multiplier and savings to year1
year1 = growth_multiplier * savings

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)
