from flask import Flask, render_template, request
from model import predict_crop

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    N = float(request.form['N'])
    P = float(request.form['P'])
    K = float(request.form['K'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])

    values = [N, P, K, temperature, humidity, ph, rainfall]

    result = predict_crop(values)

    return f"Recommended Crop: {result}"

if __name__ == "__main__":
    app.run(debug=True)