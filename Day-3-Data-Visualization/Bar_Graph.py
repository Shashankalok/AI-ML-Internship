import matplotlib.pyplot as plt
categories = ['A', 'B', 'C']
values = [5, 7, 3]

plt.bar(categories, values)
plt.title("Bar Chart")
plt.show()

##Group Bar Chart
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)

y1 = [10, 20, 15]
y2 = [12, 18, 10]

plt.bar(x - 0.2, y1, width=0.4)
plt.bar(x + 0.2, y2, width=0.4)

plt.xticks(x, ["A", "B", "C"])
plt.title("Grouped Bar Chart")
plt.show()

##Stacked Bar Chart
import matplotlib.pyplot as plt

x = ["A", "B", "C"]
y1 = [10, 20, 15]
y2 = [5, 10, 5]

plt.bar(x, y1)
plt.bar(x, y2, bottom=y1)

plt.title("Stacked Bar Chart")
plt.show()

##Horizontal Bar Chart
import matplotlib.pyplot as plt

categories = ["A", "B", "C"]
values = [10, 20, 15]

plt.barh(categories, values)
plt.title("Horizontal Bar Chart")
plt.show()