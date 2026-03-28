Titanic Dataset Analysis
Project Overview

This project performs Exploratory Data Analysis (EDA) on the Titanic dataset to understand the key factors that influenced passenger survival.

The analysis focuses on identifying patterns based on:

Gender
Passenger class
Age
Fare
Embarkation port
Family size

The goal is to extract meaningful insights from the data and understand which factors had the strongest impact on survival.

Project Objectives
To analyze survival distribution among passengers
To identify whether gender influenced survival
To study the relationship between passenger class and survival
To examine how embarkation port affected survival rates
To understand the impact of age and fare on survival
To create new features (like family size) for deeper insights
To visualize patterns and relationships in the dataset

Dataset Summary
Total Passengers: 891
Total Features: 12
Target Variable: Survived (0 = No, 1 = Yes)
Missing Data:
Age → Missing values present
Cabin → Large number of missing values (dropped)
Embarked → Few missing values (handled)

Data Cleaning & Preprocessing
Missing values in Age were filled using the median
Cabin column was removed due to excessive missing data
Missing values in Embarked were filled using the mode
Data consistency was verified after cleaning

Key Analysis Questions & Results
1. Who survived more: Men or Women?
Females had a significantly higher survival rate compared to males
A large proportion of male passengers did not survive 
Gender was one of the strongest factors influencing survival

Conclusion:
Women were given priority during evacuation, leading to higher survival rates.

2. What is the average age by passenger class?
First-class passengers had the highest average age
Second-class passengers had moderate average age
Third-class passengers were generally younger

Conclusion:
Higher-class passengers tended to be older and possibly more affluent.

3. How did embarkation port affect survival?
Passengers from Cherbourg (C) had the highest survival rate
Passengers from Queenstown (Q) had moderate survival
Passengers from Southampton (S) had the lowest survival

Conclusion:
Ports with more first-class passengers had higher survival rates.

4. What is the overall survival rate?
Approximately 38% of passengers survived
Around 62% did not survive

Conclusion:
The dataset is imbalanced, with a majority of passengers not surviving.

5. How did passenger class affect survival?
First-class passengers had the highest survival rate
Second-class passengers had moderate survival
Third-class passengers had the lowest survival

Conclusion:
Socio-economic status (represented by class) strongly influenced survival.

6. What is the relationship between fare and survival?
Passengers who paid higher fares had a higher chance of survival
Lower fare passengers had lower survival rates

Conclusion:
Fare is positively associated with survival, indicating wealth advantage.

7. Did age affect survival?
Age showed very weak relationship with survival
Both younger and older passengers had similar survival chances

Conclusion:
Age alone was not a strong predictor of survival.

8. How did family size impact survival?
Passengers traveling alone had lower survival rates
Small to medium families had higher survival rates
Large families had very low survival rates

Conclusion:
Moderate family size increased chances of survival, while very large families struggled.

9. Combined Effect of Gender and Class
Females in first class had the highest survival rate
Males in third class had the lowest survival rate

Conclusion:
Both gender and class together had a strong combined effect on survival.

Key Insights
Gender was the most important factor in survival
Passenger class strongly influenced survival probability
Higher fare increased chances of survival
Embarkation port indirectly affected survival
Age had minimal impact
Family size played a significant role
 Conclusion
This analysis shows that survival on the Titanic was not random but influenced by multiple socio-economic and demographic factors.

The most important factors were:

Gender
Passenger class
Fare

The findings highlight how privilege and priority played a crucial role during the disaster.

Future Scope
Apply machine learning models to predict survival
Perform feature encoding for categorical variables
Evaluate model accuracy and performance
Build a predictive system for survival classification