import numpy as np

investment, growth_rate, startup_age = np.genfromtxt(
    'G:\FULLSTACK-AI-BOOTCAMP-B2-MonTOFri-7TO9-PM-Explorer\DataSetForPractice\startup_growth_investment_data.csv',
    delimiter=',',
    usecols=(1, 2, 3),
    unpack=True,
    dtype=float,
    skip_header=1
)

print("Investment Mean:", np.mean(investment))
print("Investment Std Dev:", np.std(investment))
print("Investment Median:", np.median(investment))
print("Investment 25th Percentile:", np.percentile(investment, 25))
print("Investment 75th Percentile:", np.percentile(investment, 75))
print("Investment Min:", np.min(investment))
print("Investment Max:", np.max(investment))

print("Growth Rate Squared:", np.square(growth_rate))
print("Growth Rate Square Root:", np.sqrt(growth_rate))
print("Growth Rate Power 3:", np.power(growth_rate, 3))
print("Growth Rate Absolute:", np.abs(growth_rate))

print("Investment + Growth Rate:", investment + growth_rate)
print("Investment - Growth Rate:", investment - growth_rate)
print("Investment * Growth Rate:", investment * growth_rate)
print("Investment / Growth Rate:", np.divide(investment, growth_rate))

age_scaled = (startup_age / np.pi) + 1
print("Sine of Age:", np.sin(age_scaled))
print("Cosine of Age:", np.cos(age_scaled))
print("Tangent of Age:", np.tan(age_scaled))
print("Exponential of Age:", np.exp(age_scaled))

print("Natural Log of Age:", np.log(age_scaled))
print("Base-10 Log of Age:", np.log10(age_scaled))

print("Hyperbolic Sine of Age:", np.sinh(age_scaled))
print("Hyperbolic Cosine of Age:", np.cosh(age_scaled))
print("Hyperbolic Tangent of Age:", np.tanh(age_scaled))
print("Inverse Hyperbolic Sine of Age:", np.arcsinh(age_scaled))
print("Inverse Hyperbolic Cosine of Age:", np.arccosh(age_scaled))

D2_Array = np.array([investment, growth_rate])
print("2D Array:", D2_Array)
print("Dimensions:", D2_Array.ndim)
print("Total Elements:", D2_Array.size)
print("Shape:", D2_Array.shape)
print("Data Type:", D2_Array.dtype)

slice1 = D2_Array[:1, :5]
slice2 = D2_Array[:1, 4:15:4]
print("Slice1:", slice1)
print("Slice2:", slice2)
print("Indexed Item from Slice1:", slice1[0, 1])
print("Indexed Item from Slice2:", slice2[0, 2])

for elem in np.nditer(D2_Array):
    print(elem)

for index, elem in np.ndenumerate(D2_Array):
    print(index, elem)

reshaped = np.reshape(D2_Array, (1, D2_Array.size))
print("Reshaped Array:", reshaped)
print("Reshaped Size:", reshaped.size)
print("Reshaped Dimensions:", reshaped.ndim)
print("Reshaped Shape:", reshaped.shape)
