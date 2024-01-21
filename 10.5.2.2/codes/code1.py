import matplotlib.pyplot as plt
import numpy as np

# Define the function x_1(n)
def x_1(n):
    return 10 - 3 * n

# Generate natural numbers for n
n_values = np.arange(0, 33, 1)  # Considering n as natural numbers up to 32

# Generate corresponding y values for x_1(n)
y_values = x_1(n_values)

# Create a stem plot for x_1(n)
plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo', basefmt='r-')

# Highlight the stem at n = 29 in red
highlight_n = 29
highlight_index = np.where(n_values == highlight_n)[0][0]
if x_1(highlight_n) != 0:
    plt.stem(highlight_n, x_1(highlight_n), linefmt='r-', markerfmt='ro', basefmt='r-')

# Add labels and title
plt.xlabel('$n$')
plt.ylabel('$x_1(n)$')

# Add legend
plt.legend()

# Save the plot as "plot1.png"
plt.grid(True)
plt.savefig('plot1.png')

# Show the plot (optional)
plt.show()
