from sklearn.ensemble import IsolationForest
from config import Config


def run_anomaly_detection(df):
    features = df.drop(columns=["class", "time"], errors="ignore")

    model = IsolationForest(
        contamination=Config.CONTAMINATION,
        random_state=Config.RANDOM_STATE
    )

    df["anomaly_score"] = model.fit_predict(features)

    df["anomaly_flag"] = df["anomaly_score"].apply(
        lambda x: 1 if x == -1 else 0
    )

    return df