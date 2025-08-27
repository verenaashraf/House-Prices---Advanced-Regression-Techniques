from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        
        features = [
            float(request.form['OverallQual']),
            float(request.form['GrLivArea']),
            float(request.form['GarageCars']),
            float(request.form['TotalBsmtSF'])
        ]

        final_features = np.array([features])
        prediction = model.predict(final_features)

        return render_template("index.html", prediction_text=f"Predicted Price: ${prediction[0]:,.2f}")

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
