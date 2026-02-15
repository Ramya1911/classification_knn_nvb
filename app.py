from flask import Flask, render_template, request
import pickle
import json
import os

app = Flask(__name__)

# Ensure folders exist (important for Render)
os.makedirs("models", exist_ok=True)
os.makedirs("metrics", exist_ok=True)

# -------------------------------
# Load Models
# -------------------------------
nvb_model = pickle.load(open("models/Iris_classification_nvb.pkl", "rb"))
knn_model = pickle.load(open("models/Iris_classification_knn.pkl", "rb"))

# -------------------------------
# Label Mapping
# -------------------------------
label_map = {
    1: "Iris-setosa",
    2: "Iris-versicolor",
    3: "Iris-virginica"
}

# -------------------------------
# Load Metrics Function
# -------------------------------
def load_metrics(algo_name):
    """
    algo_name -> 'nvb' or 'knn'
    """

    train_path = f"metrics/train_metrics_{algo_name}.json"
    test_path = f"metrics/test_metrics_{algo_name}.json"

    with open(train_path, "r") as f:
        train_metrics = json.load(f)

    with open(test_path, "r") as f:
        test_metrics = json.load(f)

    return train_metrics, test_metrics


# -------------------------------
# Main Route
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    train_metrics = None
    test_metrics = None
    selected_algo = None

    if request.method == "POST":

        # Get Inputs from Form
        try:
            sepal_length = float(request.form["SepalLengthCm"])
            sepal_width = float(request.form["SepalWidthCm"])
            petal_length = float(request.form["PetalLengthCm"])
            petal_width = float(request.form["PetalWidthCm"])
        except:
            return render_template("index.html",
                                   prediction="Invalid Input",
                                   train_metrics=None,
                                   test_metrics=None,
                                   selected_algo=None)

        input_data = [[sepal_length,
                       sepal_width,
                       petal_length,
                       petal_width]]

        # Determine which algorithm button was clicked
        if "nvb" in request.form:
            selected_algo = "nvb"
            model = nvb_model

        elif "knn" in request.form:
            selected_algo = "knn"
            model = knn_model

        # Make Prediction
        result = model.predict(input_data)[0]

        # Convert numeric to species name
        prediction = label_map.get(result, "Unknown")

        # Load JSON Metrics for selected algorithm
        train_metrics, test_metrics = load_metrics(selected_algo)

    return render_template(
        "index.html",
        prediction=prediction,
        train_metrics=train_metrics,
        test_metrics=test_metrics,
        selected_algo=selected_algo
    )


# -------------------------------
# Run App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
