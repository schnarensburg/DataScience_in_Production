import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

'''
Building a LinearRegression Model to predict linear connections
'''

# Load data from CSV
in_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(in_dir, '../../07_RESULTS/linear_correlation_matrix.csv')
data = pd.read_csv(folder_path)
X = data[['Mean', 'Variance', 'Max_Deviation', 'Min_Deviation']]
Y = data[["fk' re", "fi' re", "fk' li", "fi' li"]]

# Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, Y_train)
predictions = model.predict(X_test)

mae = mean_absolute_error(Y_test, predictions)
mse = mean_squared_error(Y_test, predictions)
r2 = r2_score(Y_test, predictions)
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("R^2 Score:", r2)


plt.scatter(Y_test, predictions)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Linear Regression: Actual vs. Predicted Values")
plt.show()