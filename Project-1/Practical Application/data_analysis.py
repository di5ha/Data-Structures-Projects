import numpy as np

# Generate random data for demonstration
data = np.random.randint(1, 100, size=100)

# Calculating mean and standard deviation using arrays
mean_value = np.mean(data)
std_deviation = np.std(data)

print("Data:", data)
print("Mean:", mean_value)
print("Standard Deviation:", std_deviation)