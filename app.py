from pathlib import Path

from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

MODEL_PATH = Path(__file__).with_name("iris_model.pkl")


def load_model():
    # Train the model automatically if it does not exist
    if not MODEL_PATH.exists():
        from train_model import main
        main()

    saved_data = joblib.load(MODEL_PATH)
    return saved_data["model"], saved_data["target_names"]


model, target_names = load_model()


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None
    values = ["", "", "", ""]

    if request.method == "POST":
        try:
            fields = [
                "sepal_length",
                "sepal_width",
                "petal_length",
                "petal_width"
            ]

            values = [request.form.get(field, "") for field in fields]

            measurements = [float(value) for value in values]

            if not all(0 < value <= 10 for value in measurements):
                raise ValueError(
                    "Enter measurements greater than 0 and at most 10 cm."
                )

            result = model.predict([measurements])[0]
            prediction = target_names[result].replace("_", " ").title()

        except (ValueError, TypeError):
            error = (
                "Please enter four valid numeric measurements "
                "greater than 0 and at most 10 cm."
            )

    return render_template(
        "index.html",
        prediction=prediction,
        error=error,
        values=values
    )


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)