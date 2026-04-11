from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import subprocess
import json
import logging
import pandas as pd   #  NEW (important)

app = Flask(__name__)

# ================= LOGGING SETUP =================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Load model and preprocessors
model = joblib.load('house_price_model.joblib')
scaler = joblib.load('scaler.joblib')
label_encoders = joblib.load('label_encoders.joblib')


# ================= HOME =================
@app.route('/')
def home():
    return render_template('index.html')


# ================= PREDICT =================
@app.route('/predict', methods=['POST'])
def predict():
    try:
        logging.info("Prediction request received")

        data = request.get_json()

        # Extract features
        features = {
            'area': float(data['area']),
            'bedrooms': int(data['bedrooms']),
            'bathrooms': int(data['bathrooms']),
            'stories': int(data['stories']),
            'mainroad': data['mainroad'],
            'guestroom': data['guestroom'],
            'basement': data['basement'],
            'hotwaterheating': data['hotwaterheating'],
            'airconditioning': data['airconditioning'],
            'parking': int(data['parking']),
            'prefarea': data['prefarea'],
            'furnishingstatus': data['furnishingstatus']
        }

        # Encode categorical variables
        for col in ['mainroad', 'guestroom', 'basement', 'hotwaterheating',
                    'airconditioning', 'prefarea', 'furnishingstatus']:
            features[col] = label_encoders[col].transform([features[col]])[0]

        #  FIX: Use DataFrame instead of numpy array
        feature_df = pd.DataFrame([features])

        # Scale
        scaled_features = scaler.transform(feature_df)

        # Predict
        prediction = model.predict(scaled_features)[0]

        logging.info(f"Prediction result: {prediction}")

        return jsonify({
            "status": "success",
            "predicted_price": float(prediction)
        })

    except Exception as e:
        logging.error(f"Prediction error: {str(e)}")

        return jsonify({
            "status": "error",
            "error": str(e)
        }), 400


# ================= TRAIN =================
@app.route('/train', methods=['POST'])
def train():
    try:
        logging.info("Model training started")

        result = subprocess.run(
            ['python', 'train_model.py'],
            capture_output=True,
            text=True
        )

        logging.info("Model retrained successfully")

        return jsonify({
            "status": "success",
            "message": "Model retrained successfully",
            "output": result.stdout
        })

    except Exception as e:
        logging.error(f"Training error: {str(e)}")

        return jsonify({
            "status": "error",
            "message": str(e)
        })


# ================= MODEL INFO =================
@app.route('/model-info', methods=['GET'])
def model_info():
    try:
        logging.info("Model info requested")

        with open('model_info.json', 'r') as f:
            info = json.load(f)

        return jsonify({
            "status": "success",
            "model_info": info
        })

    except Exception as e:
        logging.error(f"Model info error: {str(e)}")

        return jsonify({
            "status": "error",
            "message": str(e)
        })


# ================= RUN =================
if __name__ == '__main__':
    app.run(debug=True)