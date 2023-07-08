import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def gradientBoostingRegressor(Y_data):

    # Load data from CSV
    in_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(in_dir, '../01_DATA/Z13/Z13_Datensammlung_Processed.csv')
    data = pd.read_csv(folder_path)
    X = data[['Mean', 'Outer Edge Length', 'Surface', 'Variance', 'Max_Deviation', 'Min_Deviation']].values
    Y = data[Y_data].values

    # Split data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Create Gradient Boosting Regression Model
    model = GradientBoostingRegressor()

    # Fit model with training data
    model.fit(X_train, Y_train)

    # Predict testing data
    predictions = model.predict(X_test)

    # Calculate MSE
    mse = mean_squared_error(Y_test, predictions)
    print("Mean Squared Error: ", mse)

    if Y_data == "fi' li":
        plt.scatter(Y_test, predictions)
        plt.xlabel("Actual Values")
        plt.ylabel("Predicted Values")
        plt.title("Gradient Boosting Regression: Actual vs Predicted Values")
        plt.show()

Y = ["F'i re", "fl' re", "fk' re", "fi' re", "F'i li", "fl' li", "fk' li", "fi' li"]
for element in Y:
    print(element)
    gradientBoostingRegressor(element)