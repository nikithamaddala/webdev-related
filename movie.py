import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("movies.csv")

# Convert Genre to numbers
data["Genre"] = data["Genre"].map({
    "Action": 0,
    "Comedy": 1,
    "Drama": 2
})

# Features & Target
X = data[["Genre", "Duration", "Votes"]]
y = data["Rating"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
sample = [[0, 130, 55000]]  # Action movie
prediction = model.predict(sample)

print("Predicted Rating:", prediction[0])