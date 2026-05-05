import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("train.csv")

# Select important columns
data = data[["Survived", "Pclass", "Sex", "Age", "Fare"]]

# Handle missing values
data["Age"].fillna(data["Age"].mean(), inplace=True)

# Convert categorical to numeric
data["Sex"] = data["Sex"].map({"male": 0, "female": 1})

# Split features and target
X = data[["Pclass", "Sex", "Age", "Fare"]]
y = data["Survived"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", accuracy)

# Test sample
sample = [[3, 0, 22, 7.25]]  # Example passenger
result = model.predict(sample)

print("Survival Prediction (0=No, 1=Yes):", result[0])