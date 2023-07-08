import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Load data from CSV
in_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(in_dir, '../../01_DATA/Z13/Z13_Datensammlung_Processed.csv')
data = pd.read_csv(folder_path)
X = data[['Mean', 'Outer Edge Length', 'Surface', 'Variance', 'Max_Deviation', 'Min_Deviation']]
Y = data[["F'i re", "fl' re", "fk' re", "fi' re", "F'i li", "fl' li", "fk' li", "fi' li"]]

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
Y_scaled = scaler.fit_transform(Y)


# Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y_scaled, test_size=0.2, random_state=42)
nan_indices = np.isnan(Y_train)
nan_values = Y_train[nan_indices]
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