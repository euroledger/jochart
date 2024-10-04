import math

import numpy as np
import matplotlib.pyplot as plt

# Define the equation y = mx + b (e.g., y = 2x + 1)
def line_eq(x):
    return 2 * x + 1


y2_values=[0,6,12,19,27,36,45,55,65,74,82,89,95,100]

# example
# num_data_points = 14
# parameter = 0.5
# max_value = 100


def generate_data_points(parameter, num_data_points, max_value):

    dp_array = []
    L = max_value
    p = parameter

    for x in range(0, num_data_points):
        dp_array.append(L / (1+ math.exp(-p * (x - num_data_points / 2))))
        print(x, ":", dp_array[x])

    return dp_array

def plot(x_values, y_values, label):
    # Generate x values
    # x_values = np.linspace(-1, 1, 400)  # 400 points from -10 to 10
    # y_values = line_eq(x_values)  # Calculate y values based on the function

    # Plotting the line
    plt.plot(x_values, y_values, label=label)

    # Customizing the plot
    plt.title('Python Line Graph from Sigmoid Equation and other stuff')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

def plot2():
    # Generate x values
    x_values = np.linspace(-1, 1, 400)  # 400 points from -10 to 10
    y_values = line_eq(x_values)  # Calculate y values based on the function

    # Plotting the line
    plt.plot(x_values, y_values, label='y = 2x + 1')

    # Customizing the plot
    plt.title('Python Line Graph from Sigmoid Equation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

    # Show the plot
    plt.show()

# num_data_points = 14
# parameter = 0.5
# max_value = 100
x_values = range(14)
print(x_values)
y_values = generate_data_points(0.8, 14, 100)


plot(x_values,y_values, 'Sigmoid')
plot(x_values, y2_values,'Original')

# plot(x_values, y2_values, 'Original Estimate')
mng= plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show()