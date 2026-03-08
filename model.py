import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("dataset/Crop_recommendation.csv")

# Features
X = data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]

# Target
y = data['label']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Prediction function
def predict_crop(values):
    prediction = model.predict([values])
    return prediction[0]