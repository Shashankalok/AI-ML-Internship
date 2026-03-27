# 📩 SMS Spam Detection – Text Cleaning, Feature Engineering & Visualization

---

## 📌 Project Overview

This project focuses on cleaning messy SMS text data using **Regular Expressions (Regex)** and analyzing how cleaning affects the data using **visualization techniques**.

The dataset contains spam and ham messages with noise such as:

* URLs
* Phone numbers
* Special characters
* Extra spaces
* Repeated characters
* Inconsistent casing

---

## 🎯 Objectives

* Clean raw SMS text using Regex (step-by-step)
* Perform feature engineering on both raw and cleaned data
* Compare **Before vs After Cleaning**
* Visualize distributions and patterns
* Extract meaningful insights

---

## 🛠️ Libraries Used

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
```

* **pandas** → data manipulation
* **seaborn / matplotlib** → visualization
* **re (regex)** → text cleaning

---

## 📂 Dataset Information

* Total rows: **5572**
* Columns:

  * `v1` → label (spam/ham)
  * `v2` → message

---

## 🔧 Data Preprocessing

### 🔹 Selecting Required Columns

```python
data = data[['v1', 'v2']]
data.columns = ['label', 'message']
```

✔ Removed unnecessary columns
✔ Renamed for clarity

---

### 🔹 Checking Data

```python
data.info()
data.shape
```

✔ No missing values in main columns
✔ Dataset shape: (5572, 2)

---

## 📊 Class Distribution

```python
data['label'].value_counts()
sns.countplot(x='label', data=data)
```

### 📌 Insight:

* Ham messages are significantly higher than spam
* Dataset is **imbalanced**

---

## ⚙️ Feature Engineering (Before Cleaning)

```python
data['message_length'] = data['message'].apply(len)
data['word_count'] = data['message'].apply(lambda x: len(x.split()))
```

✔ `message_length` → number of characters
✔ `word_count` → number of words

---

## 📊 Visualization (Before Cleaning)

### 🔹 Histogram (Message Length)

```python
sns.histplot(data['message_length'], bins=50)
```

✔ Right-skewed distribution
✔ Some very long messages (outliers)

---

### 🔹 Boxplot

```python
sns.boxplot(x='label', y='message_length', data=data)
```

✔ Spam messages are longer
✔ Ham messages have more variability

---

## 🧹 Text Cleaning Using Regex

---

### 🔹 Step 1: Convert to Lowercase

```python
data['cleaned_message'] = data['message'].str.lower()
```

✔ Standardizes text

---

### 🔹 Step 2: Remove URLs

```python
re.sub(r'http\S+|www\S+', '', x)
```

✔ Removes links

---

### 🔹 Step 3: Remove Numbers

```python
re.sub(r'\d+', '', x)
```

✔ Removes digits

---

### 🔹 Step 4: Remove Special Characters

```python
re.sub(r'[^\w\s]', '', x)
```

✔ Keeps only letters and spaces

---

### 🔹 Step 5: Remove Extra Spaces

```python
re.sub(r'\s+', ' ', x).strip()
```

✔ Normalizes spacing

---

### 🔹 Step 6: Remove Single Characters

```python
re.sub(r'\b[a-zA-Z]\b', '', x)
```

✔ Removes meaningless words like "a", "u", "r"

---

### 🔹 Step 7: Normalize Repeated Characters

```python
re.sub(r'(.)\1+', r'\1\1', x)
```

✔ Example:

* "heyyyy" → "heyy"
* "nooooo" → "noo"

---

## ⚙️ Feature Engineering (After Cleaning)

```python
data['cleaned_length'] = data['cleaned_message'].apply(len)
data['cleaned_word_count'] = data['cleaned_message'].apply(lambda x: len(x.split()))
```

✔ Measures cleaned text size
✔ Helps comparison

---

## 📊 Visualization (After Cleaning)

---

### 🔹 Message Length Comparison

```python
sns.histplot(data['message_length'], bins=50, label='Before', kde=True)
sns.histplot(data['cleaned_length'], bins=50, label='After', kde=True)
```

### 📌 Insight:

* Cleaned messages are shorter
* Outliers reduced

---

### 🔹 Word Count Comparison

✔ Word count slightly reduced
✔ More meaningful words retained

---

### 🔹 Boxplot (Cleaned Data)

✔ Spam messages remain longer
✔ Distribution becomes tighter

---

### 🔹 Violin Plot

✔ Shows density of message length
✔ Spam is more consistent
✔ Ham is more spread

---

## 📈 Final Insights

* Spam messages are generally longer than ham messages
* Cleaning reduces noise and improves data quality
* Feature engineering enhances analysis
* Distributions become more stable after cleaning
* Cleaned data is better suited for ML models

---

## 🚀 Why This Project is Important

✔ Demonstrates real-world NLP preprocessing
✔ Strong understanding of Regex
✔ Combines statistics + visualization
✔ Shows end-to-end data analysis workflow

---

## 🔮 Future Scope

* Stopwords removal
* TF-IDF / Vectorization
* Machine Learning models
* Model evaluation (Accuracy, Precision, Recall)
* Deployment

---

## 🧠 Key Learning

* Regex is powerful for text cleaning
* Data cleaning directly impacts model performance
* Visualization helps understand data deeply

---

## 👨‍💻 Author

**Shashank Alok**
M.Sc. Statistics | Data Analyst | ML Enthusiast

---
