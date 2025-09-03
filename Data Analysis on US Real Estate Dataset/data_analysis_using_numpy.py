import numpy as np

# Load datasets
ids, price, zip_code, house_size = np.genfromtxt(
    'DataSets\RealEstate-USA.csv',
    delimiter=',',
    usecols=(0,2,9,10),
    unpack=True,
    dtype=float,
    skip_header=1
)

# Basic statistics
print("USA Real Estate Price mean:", np.mean(price))
print("USA Real Estate Price average:", np.average(price))
print("USA Real Estate Price std:", np.std(price))
print("USA Real Estate Price median:", np.median(price))
print("USA Real Estate Price percentile - 25:", np.percentile(price, 25))
print("USA Real Estate Price percentile - 75:", np.percentile(price, 75))
print("USA Real Estate Price percentile - 3:", np.percentile(price, 3))
print("USA Real Estate Price min:", np.min(price))
print("USA Real Estate Price max:", np.max(price))

# Mathematical operations
print("USA Real Estate Price square:", np.square(price))
print("USA Real Estate Price sqrt:", np.sqrt(price))
print("USA Real Estate Price pow:", np.power(price, 2)) 
print("USA Real Estate Price abs:", np.abs(price))

# Arithmetic operations between zip_code and house_size
addition = zip_code + house_size
subtraction = zip_code - house_size
multiplication = zip_code * house_size
division = np.divide(zip_code, house_size)

print("Zip + Size Addition:", addition)
print("Zip - Size Subtraction:", subtraction)
print("Zip * Size Multiplication:", multiplication)
print("Zip / Size Division:", division)

# Trigonometric operations
pricePie = (price / np.pi) + 1
print("Sine values:", np.sin(pricePie))
print("Cosine values:", np.cos(pricePie))
print("Tangent values:", np.tan(pricePie))
print("Exponential values:", np.exp(pricePie))

# Logarithmic operations
log_array = np.log(pricePie)
log10_array = np.log10(pricePie)
print("Natural log:", log_array)
print("Base-10 log:", log10_array)

# Hyperbolic functions
print("Hyperbolic Sine:", np.sinh(pricePie))
print("Hyperbolic Cosine:", np.cosh(pricePie))
print("Hyperbolic Tangent:", np.tanh(pricePie))
print("Inverse Hyperbolic Sine:", np.arcsinh(pricePie))
print("Inverse Hyperbolic Cosine:", np.arccosh(pricePie))

# 2D array of zip_code and house_size
D2ZipSize = np.array([zip_code, house_size])
print("2D Array:", D2ZipSize)
print("Dimensions:", D2ZipSize.ndim)
print("Total Elements:", D2ZipSize.size)
print("Shape:", D2ZipSize.shape)
print("Data Type:", D2ZipSize.dtype)

# Slicing and indexing
slice1 = D2ZipSize[:1, :5]
slice2 = D2ZipSize[:1, 4:15:4]
print("Slice1:", slice1)
print("Slice2:", slice2)
print("Indexed Item from Slice1:", slice1[0, 1])
print("Indexed Item from Slice2:", slice2[0, 2])

# Iteration
for elem in np.nditer(D2ZipSize):
    print(elem)

for index, elem in np.ndenumerate(D2ZipSize):
    print(index, elem)

# Reshape
reshaped = np.reshape(D2ZipSize, (1, D2ZipSize.size))
print("Reshaped Array:", reshaped)
print("Reshaped Size:", reshaped.size)
print("Reshaped Dimensions:", reshaped.ndim)
print("Reshaped Shape:", reshaped.shape)
