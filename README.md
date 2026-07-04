# 🌱 Crop Recommendation System

A simple **Machine Learning + Flask web application** that recommends the best crop to grow based on soil nutrients and environmental conditions.

The system takes the following inputs:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH value
- Rainfall

Using these inputs, the model predicts the **most suitable crop** using a **Random Forest Classifier**.

---

# 📂 Project Structure

```
crop-recommendation-system
│
├── dataset
│   └── Crop_recommendation.csv
│
├── templates
│   └── index.html
│
├── app.py
├── model.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Requirements

Make sure the following are installed on your system:

- Python 3.8 or higher
- pip (Python package manager)
- Git

---

# 🚀 Installation and Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/crop-recommendation-system.git
```

### 2️⃣ Navigate to the Project Folder

```
cd crop-recommendation-system
```

### 3️⃣ Create a Virtual Environment

```
python -m venv venv
```

### 4️⃣ Activate the Virtual Environment

**Windows**

```
venv\Scripts\activate
```

**Mac / Linux**

```
source venv/bin/activate
```

---

### 5️⃣ Install Required Libraries

```
pip install -r requirements.txt
```

This will install:

- Flask
- Pandas
- NumPy
- Scikit-learn

---

# ▶️ Running the Application

Start the Flask server using:

```
python app.py
```

You will see output similar to:

```
Running on http://127.0.0.1:5000/
```

---

# 🌐 Open in Browser

Open your browser and go to:

```
http://127.0.0.1:5000/
```

Enter the soil and environmental parameters to get the **recommended crop**.

---

# 🧠 Machine Learning Model

The project uses:

- **RandomForestClassifier** from Scikit-learn
- Dataset containing soil nutrients and crop labels
- Trained during runtime inside `model.py`

---

# 📊 Input Parameters

| Parameter   | Description                |
| ----------- | -------------------------- |
| N           | Nitrogen content in soil   |
| P           | Phosphorus content in soil |
| K           | Potassium content in soil  |
| temperature | Temperature in °C          |
| humidity    | Humidity percentage        |
| ph          | Soil pH value              |
| rainfall    | Rainfall in mm             |

---

# 📌 Notes

- The **`venv`** folder is not included in the repository.
- Install dependencies using `requirements.txt`.
- The dataset must be inside the **dataset folder**.

---

# 👩‍💻 Author

Deepika N P
B.Tech Information Technology Student
VSB Engineering College, India

---

# 📜 License

This project is open-source and available for educational purposes.
