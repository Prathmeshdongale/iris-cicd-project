from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the built-in Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train the model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model accuracy: {accuracy:.2%}")

# Save the trained model and class names
joblib.dump(
    {
        "model": model,
        "target_names": iris.target_names.tolist()
    },
    "iris_model.pkl"
)

print("Model saved as iris_model.pkl")