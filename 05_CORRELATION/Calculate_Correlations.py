import os

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def calculate_correlations(file_path, var1, var2):
    # Load data from excel
    df = pd.read_excel(file_path)

    # Calculate correlation matrix
    corr_matrix = df.corr()

    # Print correlation matrix
    print('Correlation Matrix: ')
    print(corr_matrix)

    corr_matrix.to_csv('correlation_matrix.csv', index=True)
    print("Correlation matrix saved to correlation_matrix.csv")
    # find maximum correlation
    max_corr = corr_matrix.max().max()
    # Find columns with maximum correlation
    max_corr_cols = corr_matrix.unstack().sort_values(ascending=False).drop_duplicates().head(2).index.tolist()

    # Print results
    print("\nMaximum Correlation:")
    print("Correlation value: ", max_corr)
    print("Columns: ", max_corr_cols)

    # Generate scatter plot for the selected variables
    plt.scatter(df[var1], df[var2])
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.title("Scatter Plot")
    plt.show()




dir_in = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(dir_in, '../01_DATA/Z19/Test File/Z19 Datensammlung.xlsx')
calculate_correlations(folder_path, 'Max_Deviation', "fi' li")


