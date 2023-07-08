import os.path
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score, KFold
from sklearn.preprocessing import StandardScaler
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.metrics import r2_score


in_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(in_dir, '../../08_Korrelation/newfile.csv')

data = pd.read_csv((folder_path))
X = data[['Mean', 'Variance', 'Max_Deviation', 'Min_Deviation']].values
Y = data[["fl' re", "fk' re", "fi' re", "fl' li", "fk' li", "fi' li"]].values

# Split data into training and testing sets
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(f"Maximum X_scaled: {max(max(row) for row in X_scaled)} and Minimum X_scaled: {min(min(row) for row in X_scaled)}")
Y_scaled = scaler.fit_transform(Y)
print(f"Maximum Y_scaled: {max(max(row) for row in Y_scaled)} and Minimum Y_scaled: {min(min(row) for row in Y_scaled)}")

# Calculate mean and standard deviation of the scaled data
mean = np.mean(X_scaled, axis=0)
std = np.std(X_scaled, axis=0)
'''
# Plot histogram or density plot for each feature
for i in range(X_scaled.shape[1]):
    plt.figure()
    plt.hist(X_scaled[:, i], bins=50)  # Or use plt.plot with 'kde' for density plot
    plt.xlabel('Feature')
    plt.ylabel('Frequency')
    plt.title(f'Distribution of Feature {i+1} (mean={mean[i]:.2f}, std={std[i]:.2f})')
    plt.show()
'''

# Define the architecture of the Keras model
def create_model():
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(32, activation='softmax', input_shape=(4,)))
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(1))  # Output layer with 1 unit for the current output value
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

# Create a function to build the KerasRegressor model
def build_model():
    model = KerasRegressor(build_fn=create_model, epochs=100, batch_size=64, verbose=1)
    return model

# Create separate models for each output value using the KerasRegressor wrapper
models = []
for i in range(Y_scaled.shape[1]):
    model = build_model()
    models.append(model)

# Define the cross-validation strategy
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Perform cross-validation for each model
metrics = []
for i, model in enumerate(models):
    print(f"Training and Evaluating Model {i+1}")

    # measure MSE with cross validation for the scaled input data
    cv_results = cross_val_score(model, X_scaled, Y_scaled[:, i], cv=kfold, scoring='neg_mean_squared_error')
    loss = -cv_results.mean()
    model.fit(X_scaled, Y_scaled)
    Y_scaled_pred = model.predict(X_scaled)
    r2 = r2_score(Y_scaled[:, i], Y_scaled_pred)
    metrics.append([loss, r2])
    print(f"Cross-Validation Results for Model {i+1}:")
    print(cv_results)
    print(f"Mean Squared Error for Model {i+1}: {loss}")

print("Overall Mean Squared Error:", np.mean([sub_array[0] for sub_array in metrics]))
print("Overall Mean R2 score: ", np.mean([sub_array[1] for sub_array in metrics]))
print(metrics)

