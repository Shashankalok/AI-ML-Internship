##Histogram

import matplotlib.pyplot as plt

data = [10, 20, 20, 30, 30, 30, 40]

plt.hist(data)
plt.title("Basic Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()

##Histogram with Bins

import matplotlib.pyplot as plt

data = [10, 20, 20, 30, 30, 30, 40]

plt.hist(data, bins=4)
plt.title("Histogram with Bins")

plt.show()

##Styled Histogram

import matplotlib.pyplot as plt

data1 = [10,20,30,40,50]
data2 = [15,25,35,45,55]

plt.hist(data1, bins=5, alpha=0.5, label='Group A')
plt.hist(data2, bins=5, alpha=0.5, label='Group B')

plt.legend()
plt.title("Comparison Histogram")

plt.show()

##Seaborn Histogram

import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = [10, 20, 20, 30, 30, 30, 40]

# Create histogram with KDE
sns.histplot(data, bins=5, kde=True)

# Labels and title
plt.title("Histogram with KDE")
plt.xlabel("Values")
plt.ylabel("Frequency")

# Show plot
plt.show()


## Histogram(Transaction Amount)
import matplotlib.pyplot as plt
import seaborn as sns

data1 = [100, 200, 150, 300, 250, 400, 500, 600, 700]
data2 = [120, 220, 180, 320, 270, 420, 520, 620, 720]

# Create figure
plt.figure(figsize=(8,6))

# Histogram 1
plt.hist(data1, bins=5, color='skyblue', edgecolor='black', alpha=0.6, label='Transactions A')

# Histogram 2 (Comparison)
plt.hist(data2, bins=5, color='orange', edgecolor='black', alpha=0.6, label='Transactions B')

# Seaborn KDE (Advanced)
sns.kdeplot(data1, color='blue', linewidth=2)
sns.kdeplot(data2, color='red', linewidth=2)

# Labels & Title
plt.title("Transaction Amount Distribution Analysis", fontsize=14)
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.legend()

plt.show()