import matplotlib.pyplot as plt
import numpy as np

# Function to calculate x_1(n)
def x_1(n):
    return 10 - 3 * n

# Function to calculate x_2(n)
def x_2(n):
    return -3 + 2.5 * n

def generate_y_values(func, n_values):
    return func(n_values)

def highlight_point(x, y, label, color='r'):
    plt.stem(x, y, linefmt=f'{color}-', markerfmt=f'{color}o', basefmt=' ')
    plt.text(x, y, label, verticalalignment='bottom', horizontalalignment='right', color=color)

def main():
    # Generate natural numbers for n
    n_values_1 = np.arange(0, 33, 1)  # Considering n as natural numbers up to 32
    n_values_2 = np.arange(21)

    # Generate corresponding y values for x_1(n) and x_2(n)
    y_values_1 = generate_y_values(x_1, n_values_1)
    x_2_values = generate_y_values(x_2, n_values_2)

    # Create a stem plot for x_1(n)
    plt.subplot(2, 1, 1)
    plt.stem(n_values_1, y_values_1, linefmt='b-', markerfmt='bo', basefmt='r-')
    highlight_n_1 = 29
    if x_1(highlight_n_1) != 0:
        highlight_point(highlight_n_1, x_1(highlight_n_1), '', color='r')

    # Add labels and title for the first plot
    plt.xlabel('$n$')
    plt.ylabel('$x_1(n)$')
    plt.grid(True)

    # Create a stem plot for x_2(n)
    plt.subplot(2, 1, 2)
    plt.stem(n_values_2, x_2_values, linefmt='b-', markerfmt='bo', basefmt=' ')
    highlight_n_2 = 10
    highlight_value_2 = x_2(highlight_n_2)
    highlight_point(highlight_n_2, highlight_value_2, '', color='r')

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

if __name__ == "__main__":
    main()

