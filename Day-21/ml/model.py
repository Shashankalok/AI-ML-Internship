import numpy as np
from sklearn.linear_model import LogisticRegression

model = None

def generate_data(n=200):
    np.random.seed(42)

    heart_rate = np.random.randint(50, 150, n)
    oxygen = np.random.randint(85, 100, n)

    X = np.column_stack((heart_rate, oxygen))

    y = []

    for hr, o2 in X:
        if hr > 130 or hr < 45 or o2 < 88:
            y.append(2)  # critical
        elif hr > 100 or o2 < 94:
            y.append(1)  # warning
        else:
            y.append(0)  # stable

    return X, np.array(y)


def get_model():
    global model

    if model is None:
        X, y = generate_data(300)

        model = LogisticRegression(max_iter=300)
        model.fit(X, y)

    return model


def predict_risk(heart_rate, oxygen_level):
    model = get_model()

    pred = model.predict([[heart_rate, oxygen_level]])[0]
    prob = model.predict_proba([[heart_rate, oxygen_level]])[0]

    labels = ["LOW", "MEDIUM", "HIGH"]

    return {
        "prediction": labels[pred],
        "confidence": round(max(prob) * 100, 2)
    }