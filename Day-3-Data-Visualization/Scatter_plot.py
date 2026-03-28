#Basic-Scatter-PLot
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,15,25,30]

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

#2nd -Scatter-plot
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()

##Scatter plot with different sizes
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,15,20,25]
sizes = [50,100,200,300]

plt.scatter(x, y, s=sizes)
plt.title("Scatter Plot with Sizes")
plt.show()

##Scatter Plot with colour mapping

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,15,20,25]
colors = [1,2,3,4]

plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()
plt.title("Color Mapped Scatter Plot")
plt.show()

##Scatter plot with Multiple groups

import matplotlib.pyplot as plt

x1 = [1,2,3]
y1 = [10,20,30]

x2 = [1,2,3]
y2 = [5,15,25]

plt.scatter(x1, y1, label="Group 1")
plt.scatter(x2, y2, label="Group 2")

plt.legend()
plt.title("Multiple Scatter Plot")
plt.show()