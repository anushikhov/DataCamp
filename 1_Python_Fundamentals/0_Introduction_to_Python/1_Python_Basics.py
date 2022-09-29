# Print the sum of 7 and 10
print(7 + 10)

# Exponentiation
# Raises the number to its left to the power of the number to its right
print(4 ** 2)

# Modulo
# Returns the remainder of the division of the number to the left by the number on its right
print(18 % 7)

# Suppose you have $100, which you can invest with a 10% return each year.
# After one year, it's 100 x 1.1 = 110 dollars,
# and after two years it's 100 x 1.1 x 1.1 = 121.
# Add code to calculate how much money you end up with after 7 years,
# and print the result.  
print(100 * 1.1 ** 7)

# How the code behaves depends on the types you're working with.

# Create a variable
savings = 100

# Print out savings
print(savings)

growth_multiplier = 1.1

result = savings * growth_multiplier ** 7

print(result)

desc = "compound interest"

profitable = True

print(type(desc))

# To find out the type of a value or a variable that refers to that value:  
type(desc)

year1 = savings * growth_multiplier

print(type(year1))

doubledesc = desc + desc

print(doubledesc)

print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# You need to explicitly convert the types of your variables. 

pi_string = "3.1415926"
pi_float = float(pi_string)

