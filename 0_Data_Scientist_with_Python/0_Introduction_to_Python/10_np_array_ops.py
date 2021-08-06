# height_in and weight_lb are available as regular lists
height_in = [74, 72, 75, 75, 69, 82, 89, 65]
weight_lb = [185, 175, 200, 211, 204, 180, 199, 103]

# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2

# Print out bmi
print(bmi)

# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 5
print(np_weight_lb[5])

# Print out sub-array of np_height_in: index 1 up to and including index 5
print(np_height_in[1:6])
