import matplotlib.pyplot as plt
import numpy as np  # Added NumPy import

# Function to calculate x_2(n)
def x_2(n):
    return -3 + 2.5 * n

# Generate data points for n from 0 to 20
n_values = np.arange(21)
x_2_values = x_2(n_values)

# Create a stem plot
plt.stem(n_values, x_2_values, linefmt='b-', markerfmt='bo', basefmt=' ')

# Highlight the stem at n = 10 in red
plt.stem(10, x_2(10), linefmt='r-', markerfmt='ro', basefmt=' ')

# Add labels and title
plt.xlabel('n')
plt.ylabel('x_2(n)')
plt.title('Stem Plot of x_2(n)')

# Save the plot as plot2.png
plt.savefig('plot2.png')

# Show the plot (optional)
plt.show()

