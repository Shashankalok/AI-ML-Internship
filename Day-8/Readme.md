# 🚢 Titanic Survival Prediction using Machine Learning

## 📌 Project Overview

This project aims to predict whether a passenger survived the Titanic disaster using various machine learning classification algorithms. The workflow includes data preprocessing, feature engineering, model building, and evaluation using multiple metrics.

---

## 🎯 Objective

To build a classification model that predicts passenger survival and compare multiple models to identify the best-performing one.

---

## 📂 Dataset Description

The dataset contains passenger details such as:

* PassengerId
* Survived (Target Variable)
* Pclass
* Name
* Sex
* Age
* SibSp (Siblings/Spouses)
* Parch (Parents/Children)
* Ticket
* Fare
* Cabin
* Embarked

---

## 🧹 Data Preprocessing

### ✔ Handling Missing Values

* Missing values in `Embarked` were filled using the mode (most frequent value).

### ✔ Feature Engineering

* **FamilySize** = SibSp + Parch + 1
* **IsAlone** = 1 if passenger is alone, else 0

### ✔ Encoding Categorical Variables

* Sex → male = 0, female = 1
* Embarked → S = 0, C = 1, Q = 2

### ✔ Dropping Irrelevant Features

Removed:

* Name
* Ticket
* PassengerId

---

## 🔀 Train-Test Split

* 80% training data
* 20% testing data
* Ensures model evaluation on unseen data

---

## 🤖 Models Used

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. K-Nearest Neighbors (KNN)

---

## ⚙️ Pipeline

* StandardScaler applied for Logistic Regression and KNN
* Tree-based models used without scaling

---

## 📊 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* ROC Curve & AUC
* Confusion Matrix

---

## 📈 Model Performance Summary

| Model               | Accuracy | Precision | Recall | F1 Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Random Forest       | ~0.83    | High      | High   | Best     |
| KNN                 | ~0.81    | High      | Medium | Good     |
| Logistic Regression | ~0.79    | Medium    | Medium | Stable   |
| Decision Tree       | ~0.78    | Medium    | Medium | Lowest   |

---

## 📉 ROC Curve Analysis

* Random Forest achieved the highest AUC (~0.90)
* Indicates best ability to distinguish between classes

---

## 📊 Confusion Matrix Insights

* Random Forest had the best balance of predictions
* Lower false negatives compared to other models
* KNN showed higher false negatives (missed survivors)

---

## 🏆 Final Model Selection

**Random Forest** was selected as the best model because:

* Highest accuracy
* Best AUC score
* Balanced precision and recall
* Fewer classification errors

---

## 📌 Conclusion

This project demonstrates how machine learning can be applied to predict survival outcomes. Feature engineering and proper model evaluation significantly improved performance. Random Forest proved to be the most reliable model for this dataset.

---

## 🚀 Future Improvements

* Hyperparameter tuning
* Feature selection techniques
* Use of advanced models (XGBoost, LightGBM)
* Deployment using Streamlit or Flask

---

## 🧠 Key Learnings

* Importance of data preprocessing
* Feature engineering impact
* Model comparison techniques
* Evaluation beyond accuracy

---

## 📬 Author

Shashank Alok

---

## ⭐ If you like this project

Give it a star on GitHub and share it on LinkedIn!
