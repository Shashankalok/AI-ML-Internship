#  Amazon Product Review Sentiment Analysis (NLP Project)

## Project Overview

This project focuses on building a **Sentiment Analysis Model** using **Natural Language Processing (NLP)** techniques to classify Amazon product reviews as **Positive** or **Negative**.

---

##  Problem Statement

Understanding customer feedback is crucial for businesses.
This project analyzes review text and predicts whether the sentiment is positive or negative.

---

## Project Workflow

```
Raw Text → Cleaning → Tokenization → Feature Engineering → Model → Prediction
```

---

## Dataset

* Amazon Fine Food Reviews Dataset
* Contains:

  * Review Text
  * Score (1–5)

---

##  Exploratory Data Analysis

### Score Distribution

* Most reviews are **4 and 5 stars**
* Indicates **positive bias in data**

### Sentiment Distribution

* More **positive reviews than negative**
* Dataset is **imbalanced**

---

## Text Preprocessing (NLP)

The following NLP steps were applied:

* 🔤 **Tokenization** → Splitting text into words
* 🚫 **Stopword Removal** → Removing common words (e.g., "the", "is")
* 🔄 **Lemmatization** → Converting words to base form
* 🧼 **Text Cleaning** → Removing punctuation and lowercasing

Example:

```
Original: "This product is AMAZING!!!"
Cleaned: "product amazing"
```

---

## Feature Engineering

### Bag of Words (BoW)

* Converts text into word frequency vectors
* Simple baseline approach

### TF-IDF (Term Frequency - Inverse Document Frequency)

* Assigns importance to meaningful words
* Reduces impact of common words

Example:

* "good" → lower importance
* "excellent" → higher importance

---

## Model Building

### Models Used:

1. **Naive Bayes (BoW)**
2. **Logistic Regression (TF-IDF)**
3. **Naive Bayes (TF-IDF)**

---

## Model Evaluation

Evaluation metrics used:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## Confusion Matrix Explanation

```
                Predicted
              Neg    Pos
Actual  Neg   TN     FP
        Pos   FN     TP
```

* **TP** → Correct positive predictions
* **TN** → Correct negative predictions
* **FP** → Wrongly predicted positive
* **FN** → Wrongly predicted negative

---

## Model Comparison

| Model                        | Description        |
| ---------------------------- | ------------------ |
| BoW + Naive Bayes            | Baseline model     |
| TF-IDF + Logistic Regression | Strong performance |
| TF-IDF + Naive Bayes         | Best for text      |

---

## Prediction System

The model can predict sentiment for new input text:

```
Input: "This product is amazing!"
Output: Positive
```

---

## Final Conclusion

* TF-IDF performs better than Bag of Words
* NLP preprocessing significantly improves accuracy
* Naive Bayes works well for text classification
* Logistic Regression provides strong results

---

## Key Learnings

* Importance of **text preprocessing**
* Role of **feature engineering in NLP**
* Comparison of **different ML models**
* Building an **end-to-end NLP pipeline**

---

## Tech Stack

* Python
* Pandas
* NumPy
* NLTK
* Scikit-learn
* Matplotlib

---

## Future Improvements

* Use Deep Learning (LSTM, BERT)
* Handle class imbalance
* Deploy using Streamlit

---

## Author

Shashank Alok
