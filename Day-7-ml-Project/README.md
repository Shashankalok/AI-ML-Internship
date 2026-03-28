# 🏠 House Price Prediction using Machine Learning

## 📌 Project Overview

This project focuses on building a machine learning model to predict house prices based on various features such as area, number of bedrooms, bathrooms, and amenities.

The goal is to help:

* Real estate businesses
* Buyers and sellers
* Investors

make informed decisions based on data-driven insights.

---

## 📊 Dataset Information

* Total Rows: 545
* Total Columns: 13 (before encoding)
* Features include:

  * Numerical: area, bedrooms, bathrooms, stories, parking
  * Categorical: mainroad, guestroom, basement, airconditioning, furnishingstatus, etc.

---

## 🧹 Data Preprocessing

Steps performed:

* Converted binary categorical variables (yes/no → 1/0)
* Applied one-hot encoding on furnishingstatus
* Converted all features to numeric format
* Checked for missing values (none found)

---

## 📈 Exploratory Data Analysis

* Correlation heatmap used to identify relationships
* Strong predictors:

  * Area
  * Bathrooms
  * Air conditioning

---

## ⚙️ Model Building

### Models Used:

* Linear Regression
* Ridge Regression
* Lasso Regression

### Data Split:

* Training: 80%
* Testing: 20%

### Feature Scaling:

* StandardScaler applied

---

## 📊 Model Performance

| Metric   | Value     |
| -------- | --------- |
| MAE      | 970,043   |
| RMSE     | 1,324,506 |
| R² Score | 0.65      |

---

## 🔍 Key Insights

* Area and bathrooms are the most important features
* Amenities like AC and parking increase price
* Unfurnished houses reduce price

---

## 📉 Model Evaluation

* Scatter plot: shows good alignment with actual values
* Residual plot: no major pattern → good model fit
* Residual distribution: approximately normal

---

## 💾 Model Deployment

Model saved using:

```python
joblib.dump(model, "house_price_model.pkl")
```

---

## 🎯 Interview Questions & Answers

### 1. What is Linear Regression?

Linear Regression is a supervised learning algorithm used to predict continuous values by modeling the relationship between independent and dependent variables.

### 2. Why did you use StandardScaler?

To normalize features so that all variables contribute equally to the model.

### 3. What is R² Score?

It measures how much variance in the target variable is explained by the model.

### 4. Difference between Ridge and Lasso?

* Ridge: L2 regularization, reduces coefficients
* Lasso: L1 regularization, can make coefficients zero (feature selection)

### 5. Why check residuals?

To validate model assumptions and detect patterns or bias.

### 6. What is overfitting?

When a model performs well on training data but poorly on unseen data.

### 7. Why Linear Regression performed best?

Because data was clean and had a mostly linear relationship.

### 8. What are limitations of your model?

* Moderate accuracy (R² = 0.65)
* Errors in extreme values

### 9. How can you improve this model?

* Use Random Forest
* Use XGBoost
* Hyperparameter tuning

### 10. What are business insights?

* Larger houses cost more
* Amenities increase value
* Furnishing impacts price perception

---

## 🚀 Future Improvements

* Use advanced ML models
* Deploy using Streamlit or Flask
* Add more features (location, age of house)

---

## 💼 Resume Points

* Built a machine learning model to predict house prices
* Achieved R² score of 0.65
* Performed EDA, feature engineering, and model evaluation

---

## ⭐ Final Conclusion

This project demonstrates end-to-end machine learning workflow including data preprocessing, modeling, evaluation, and insights generation. The model performs reasonably well and provides valuable insights for real estate decision-making.
