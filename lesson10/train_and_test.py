import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load the hand_data.csv dataset
hand_data = pd.read_csv('data/hand_data.csv')

# Separate the features and labels
X = hand_data.iloc[:, 1:]
y = hand_data.iloc[:, 0]

# Preprocess the data by subtracting the mean of x, y, and z coordinates
for i in range(0, 63, 21):
    X_array = X.iloc[:, i:i+21].to_numpy()
    X_mean = X_array.mean(axis=1, keepdims=True)
    X_array -= X_mean
    X.iloc[:, i:i+21] = pd.DataFrame(X_array, index=X.index)

# Initialize and train the Random Forest classifier
clf = RandomForestClassifier()
clf.fit(X, y)

# Create a directory to store the trained model
model_dir = 'lesson10/'
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

# Define the path for the model
model_path = os.path.join(model_dir, 'random_forest_classifier.pkl')

# Save the trained model to the defined path
joblib.dump(clf, model_path)

# Load the model back into the 'model' variable
model = joblib.load(model_path)

# Define the classify_hand function
def classify_hand(coordinates, model):
    # Ensure the coordinates are in the correct shape (1, 63)
    coordinates = np.array(coordinates).reshape(1, -1)
    # Predict the class using the loaded model
    prediction = model.predict(coordinates)
    return prediction[0]

# Load the hand_data_test.csv dataset
hand_data_test = pd.read_csv('data/hand_data_test.csv')

# Separate the features and labels
X_test = hand_data_test.iloc[:, 1:]
y_test = hand_data_test.iloc[:, 0]

# Preprocess the test data by subtracting the mean of x, y, and z coordinates
for i in range(0, 63, 21):
    X_test_array = X_test.iloc[:, i:i+21].to_numpy()
    X_test_mean = X_test_array.mean(axis=1, keepdims=True)
    X_test_array -= X_test_mean
    X_test.iloc[:, i:i+21] = pd.DataFrame(X_test_array, index=X_test.index)

# Test the classify_hand function and calculate the accuracy
correct_predictions = 0
for index, row in X_test.iterrows():
    prediction = classify_hand(row.tolist(), model)
    if prediction == y_test.iloc[index]:
        correct_predictions += 1

test_accuracy = correct_predictions / len(y_test)
print(f"Test accuracy: {test_accuracy}")
