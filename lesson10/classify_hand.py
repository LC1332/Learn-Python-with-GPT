
import numpy as np
import pandas as pd
import joblib

default_model_path = "lesson10/random_forest_classifier.pkl"
__model = None

def classify_hand(coordinates, model = None):
    if model is None:
        global __model
        if __model is None: 
            __model = joblib.load(default_model_path)
        model = __model
        
    coordinates = np.array(coordinates).reshape(1, -1)
    prediction = model.predict(coordinates)
    return prediction[0]


if __name__ == '__main__':
    # Define the path for the model
    # model_path = '/mnt/data/lesson10/random_forest_classifier.pkl'
    
    # Load the model back into the 'model' variable
    # model = joblib.load(model_path)

    model = None
    
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
