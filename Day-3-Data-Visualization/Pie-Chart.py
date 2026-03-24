import matplotlib.pyplot as plt

labels = ["A","B","C"]
sizes = [30,40,30]

plt.pie(sizes, labels=labels)
plt.title("Pie Chart")
plt.show()

#Pie-Chart-With-Percentage
import matplotlib.pyplot as plt

sizes = [40, 30, 20, 10]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Basic Pie Chart")

plt.show()

#3rd pie Chart
import matplotlib.pyplot as plt

types = ['Payment', 'Transfer', 'Cash-Out', 'Debit']
values = [50, 20, 20, 10]

plt.pie(values, labels=types, autopct='%1.1f%%')
plt.title("Transaction Distribution")

plt.show()


##Pie Chart 
import matplotlib.pyplot as plt


labels = ['Payment', 'Transfer', 'Cash-Out', 'Debit']
sizes = [50, 20, 20, 10]

# Styling
colors = ['gold', 'lightblue', 'lightgreen', 'pink']
explode = [0, 0.2, 0, 0]  # highlight "Transfer"

plt.figure(figsize=(6,6))

plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',   # percentage
    colors=colors,
    explode=explode,
    startangle=90,
    shadow=True
)

plt.title("Transaction Distribution Analysis", fontsize=14)

plt.axis('equal')  # makes it circular
plt.show()