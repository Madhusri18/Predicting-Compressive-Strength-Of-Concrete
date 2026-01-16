from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load trained model
with open("cement.pkl", "rb") as f:
    model = pickle.load(f)

# Load feature names
with open("feature_names.pkl", "rb") as f:
    FEATURE_NAMES = [col.strip() for col in pickle.load(f)]


# Home page
@app.route("/")
def home():
    return render_template("prj.html")

# Prediction input page
@app.route("/Prediction")
def prediction():
    return render_template("prj2.html")

# Handle prediction
@app.route("/predict", methods=["POST"])
@app.route("/predict", methods=["POST"])
def predict():
    try:
        cement = float(request.form["cement"])
        blast_furnace_slag = float(request.form["blast_furnace_slag"])
        fly_ash = float(request.form["fly_ash"])
        water = float(request.form["water"])
        superplasticizer = float(request.form["superplasticizer"])
        coarse_aggregate = float(request.form["coarse_aggregate"])
        fine_aggregate = float(request.form["fine_aggregate"])
        age = float(request.form["age"])

        x = pd.DataFrame([[
            cement,
            blast_furnace_slag,
            fly_ash,
            water,
            superplasticizer,
            coarse_aggregate,
            fine_aggregate,
            age
        ]], columns=FEATURE_NAMES)

        result = model.predict(x)[0]

        return render_template(
    "prj3.html",
    prediction_value=result
)



    except Exception as e:
        return render_template(
            "prj3.html",
            prediction_text=f"Error: {str(e)}"
        )

if __name__ == "__main__":
    app.run(debug=True)
