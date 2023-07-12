import os
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import cross_val_score, KFold
from sklearn.preprocessing import StandardScaler
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.metrics import r2_score
from keras.utils import plot_model

'''
Build a Neural Network for the reany output values, forecasting performance of the gear data based on geometric data
'''

# Load data from CSV
in_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(in_dir, '../../07_RESULTS/Z19_Data_Processed.csv')
data = pd.read_csv(folder_path)
X = data[['Mean', ' Outer Edge Length', ' Surface', 'Variance', 'Max_Deviation', 'Min_Deviation']].values
Y = data[["F'i re", "fl' re",  "fk' re", "fi' re", "F'i li", "fl' li", "fk' li", "fi' li"]].values


# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
Y_scaled = scaler.fit_transform(Y)

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

def r2_metric(Y_train, Y_predict):
    r2 = r2_score(Y_train, Y_predict)
    return r2

# Define architecture of Keras model
def create_model():
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(32, activation='softmax', input_shape=(6,)))
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(1))  # Output layer with 1 unit for the current output value
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

# Create function to build KerasRegressor model
def build_model():
    model = KerasRegressor(build_fn=create_model, epochs=100, batch_size=64, verbose=1)
    return model

# Create separate models for each output value
models = []
for i in range(Y_scaled.shape[1]):
    model = build_model()
    models.append(model)

# Define cross-validation
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Perform cross-validation for each model
metrics = []
for i, model in enumerate(models):
    cv_results = cross_val_score(model, X_scaled, Y_scaled[:, i], cv=kfold, scoring='neg_mean_squared_error')
    loss = -cv_results.mean()
    model.fit(X_scaled, Y_scaled)
    Y_scaled_pred = model.predict(X_scaled)
    r2 = r2_score(Y_scaled[:, i], Y_scaled_pred)
    metrics.append([loss, r2])

print("Overall Mean Squared Error:", np.mean([sub_array[0] for sub_array in metrics]))
print("Overall Mean R2 score: ", np.mean([sub_array[1] for sub_array in metrics]))
print(metrics)

def prediction_trial(models, index, pointcloud):
    model = models[index]

    data = pd.read_csv(pointcloud)
    X = data[['Mean', ' Outer Edge Length', ' Surface', 'Variance', 'Max_Deviation', 'Min_Deviation']].values
    Y = data[["F'i re", "fl' re", "fk' re", "fi' re", "F'i li", "fl' li", "fk' li", "fi' li"]].values

    # Scale data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    Y_scaled = scaler.fit_transform(Y)

    prediction_scaled = model.predict(X_scaled)
    prediction = scaler.inverse_transform(Y_scaled)

    formatted_pred = ["Wälzfehler rechts: ", prediction[0][0], "Wälzfehler links: ", prediction[0][4]]

    print(f"Beispielvorhersage durch Neural Network:\n "
          f"{formatted_pred[0]} {formatted_pred[1]} \n "
          f"{formatted_pred[2]} {formatted_pred[3]}")

pointcloud_geometric_data = '../../07_RESULTS/example_data.csv'
prediction_trial(models, 6, pointcloud_geometric_data)

