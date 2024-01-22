import matplotlib.pyplot as plt
import numpy as np

# Define sequences
n_values_1 = np.arange(0, 33, 1)
n_values_2 = np.arange(21)

# Define sequences x_1(n) and x_2(n)
x_1_values = 10 - 3 * n_values_1
x_2_values = -3 + 2.5 * n_values_2

# Highlight points
highlight_n_1 = 29
highlight_value_1 = 10 - 3 * highlight_n_1

highlight_n_2 = 10
highlight_value_2 = -3 + 2.5 * highlight_n_2

# Create the first stem plot for x_1(n)
plt.subplot(2, 1, 1)
plt.stem(n_values_1, x_1_values, linefmt='b-', markerfmt='bo', basefmt='r-')

if highlight_value_1 != 0:
    plt.stem(highlight_n_1, highlight_value_1, linefmt='r-', markerfmt='ro', basefmt=' ')

# Add labels and title for the first plot
plt.xlabel('$n$')
plt.ylabel('$x_1(n)$')
plt.grid(True)

# Create the second stem plot for x_2(n)
plt.subplot(2, 1, 2)
plt.stem(n_values_2, x_2_values, linefmt='b-', markerfmt='bo', basefmt=' ')

plt.stem(highlight_n_2, highlight_value_2, linefmt='r-', markerfmt='ro', basefmt=' ')

# Add labels and title for the second plot
plt.xlabel('$n$')
plt.ylabel('$x_2(n)$')
plt.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Save the combined plot as "combined_plot.png"
plt.savefig('combined_plot.png')

# Show the combined plot (optional)
plt.show(block=True)

