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