import math

import numpy as np
import matplotlib.pyplot as plt

# Define the equation y = mx + b (e.g., y = 2x + 1)
def line_eq(x):
    return 2 * x + 1


  # function generateDataPoints(p) {
  #   let dpArray = Array(numDataPoints);
  #
  #   for (let x = 0; x < numDataPoints; x++) {
  #     dpArray[x] = L / (1 + Math.exp(-p * (x - numDataPoints / 2)));
  #     // dpArray[x] = L / (1 + Math.exp(-p * (x)));
  #   }
  #
  #   return dpArray;
  # }

# example
# num_data_points = 14
# parameter = 0.5
# max_value = 100

# 0:2.931223075135632
# 1:4.742587317756678
# 2:7.5858180021243555
# 3:11.920292202211755
# 4:18.242552380635637
# 5:26.894142136999513
# 6:37.754066879814545
# 7:50
# 8:62.245933120185455
# 9:73.10585786300048
# 10:81.75744761936436
# 11:88.07970779778823
# 12:92.41418199787564
# 13:95.25741268224333

def generate_data_points(parameter, num_data_points, max_value):

    dp_array = []
    L = max_value
    p = parameter

    for x in range(0, num_data_points):
        dp_array.append(L / (1+ math.exp(-p * (x - num_data_points / 2))))
        print(x, ":", dp_array[x])

    return dp_array

def plot(x_values, y_values):
    # Generate x values
    # x_values = np.linspace(-1, 1, 400)  # 400 points from -10 to 10
    # y_values = line_eq(x_values)  # Calculate y values based on the function

    # Plotting the line
    plt.plot(x_values, y_values, label='Sigmoid')

    # Customizing the plot
    plt.title('Python Line Graph from Sigmoid Equation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

    # Show the plot
    plt.show()

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
y_values = generate_data_points(0.5, 14, 100)


plot(x_values,y_values)