# Python List

# A list is a compound data type that lets you group values together.
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]

type(fam)

a = "is"
b = "nice"
my_list = ["my", "list", a, b]

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)

# A list can contain any Python type.
# A list can contain a mix of Python types including strings, floats, booleans.

# hose information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

print(house)
print(type(house))

# List slicing - [inclusive:exclusive]

x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result

# The areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area
eat_sleep_area = areas[3] + areas[7]

print(eat_sleep_area)

# Use slicing to create downstairs
downstairs = areas[:6]

# Use slicing to create upstairs
upstairs = areas[-4:]

print(downstairs)
print(upstairs)
