import numpy as np

lat, long, pcode = np.genfromtxt(
    'DataSets\FastFoodRestaurants.csv',
    delimiter = ',',
    usecols = (4,5,7),
    unpack = True,
    dtype = float,
    skip_header=1
)

#Basic Statistics
print("FastFood Restaurants Postal Code mean:", np.mean(pcode))
print("FastFood Restaurants Postal Code average:", np.average(pcode))
print("FastFood Restaurants Postal Code std:", np.std(pcode))
print("FastFood Restaurants Postal Code median:", np.median(pcode))
print("FastFood Restaurants Postal Code percentile - 25:", np.percentile(pcode, 25))
print("FastFood Restaurants Postal Code percentile - 75:", np.percentile(pcode, 75))
print("FastFood Restaurants Postal Code percentile - 3:", np.percentile(pcode, 3))
print("FastFood Restaurants Postal Code min:", np.min(pcode))
print("FastFood Restaurants Postal Code max:", np.max(pcode))

# Mathematical Operations
print("FastFood Restaurants Latitude square:", np.square(lat))
print("FastFood Restaurants Latitude sqrt:", np.sqrt(lat))
print("FastFood Restaurants Latitude pow:", np.power(lat, 2)) 
print("FastFood Restaurants Latitude abs:", np.abs(lat))

# Arithmetic operations between latitude and longitude
addition = lat + long
subtraction = lat - long
multiplication = lat * long
division = np.divide(lat, long)

print("Latitude + Longitude Addition:", addition)
print("Latitude - Longitude Subtraction:", subtraction)
print("Latitude * Longitude Multiplication:", multiplication)
print("Latitude / Longitude Division:", division)

# Trigonometric operations
LongPie = (long / np.pi) + 1
print("Sine values:", np.sin(LongPie))
print("Cosine values:", np.cos(LongPie))
print("Tangent values:", np.tan(LongPie))
print("Exponential values:", np.exp(LongPie))

# Logarithmic operations
log_array = np.log(LongPie)
log10_array = np.log10(LongPie)
print("Natural log:", log_array)
print("Base-10 log:", log10_array)

# Hyperbolic functions
print("Hyperbolic Sine:", np.sinh(LongPie))
print("Hyperbolic Cosine:", np.cosh(LongPie))
print("Hyperbolic Tangent:", np.tanh(LongPie))
print("Inverse Hyperbolic Sine:", np.arcsinh(LongPie))
print("Inverse Hyperbolic Cosine:", np.arccosh(LongPie))

# 2D array of lat and long
D2_Array = np.array([lat, long])
print("2D Array:", D2_Array)
print("Dimensions:", D2_Array.ndim)
print("Total Elements:", D2_Array.size)
print("Shape:", D2_Array.shape)
print("Data Type:", D2_Array.dtype)

# Slicing and indexing
slice1 = D2_Array[:1, :5]
slice2 = D2_Array[:1, 4:15:4]
print("Slice1:", slice1)
print("Slice2:", slice2)
print("Indexed Item from Slice1:", slice1[0, 1])
print("Indexed Item from Slice2:", slice2[0, 2])

# Iteration
for elem in np.nditer(D2_Array):
    print(elem)

for index, elem in np.ndenumerate(D2_Array):
    print(index, elem)

# Reshape
reshaped = np.reshape(D2_Array, (1, D2_Array.size))
print("Reshaped Array:", reshaped)
print("Reshaped Size:", reshaped.size)
print("Reshaped Dimensions:", reshaped.ndim)
print("Reshaped Shape:", reshaped.shape)
