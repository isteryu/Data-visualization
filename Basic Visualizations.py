# Install libraries (if needed)
# !pip install matplotlib seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample data
x = np.array([2, 4, 6, 8, 9, 12, 13, 15, 18, 20])
y = np.array([10, 15, 7, 12, 20, 8, 2, 16, 25, 5])

# Bar Chart
plt.figure()
plt.bar(x, y)
plt.title('Bar Chart Example')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.show()

# Line Graph
plt.figure()
plt.plot(x, y, marker='o')
plt.title('Line Graph Example')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.show()

# Scatter Plot
plt.figure()
sns.scatterplot(x=x, y=y)