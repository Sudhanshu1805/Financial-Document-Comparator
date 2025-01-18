# --- anomaly.py ---
# Detect anomalies in text documents
from sklearn.ensemble import IsolationForest
import numpy as np

def detect_anomalies(data):
    """Uses Isolation Forest to detect anomalies in the given data."""
    model = IsolationForest(contamination=0.1, random_state=42)
    reshaped_data = np.array(data).reshape(-1, 1)
    predictions = model.fit_predict(reshaped_data)
    return predictions
