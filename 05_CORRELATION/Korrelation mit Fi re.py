import pandas as pd

# CSV-Datei einlesen
file_path = '/Users/moritz/PycharmProjects/pythonProject1/korrelation /Datensammlungen/Z13 Datensammlung.csv'
encoding = 'latin-1'  # oder das richtige Zeichencodierungsformat angeben
data = pd.read_csv(file_path, encoding=encoding)

# Spalte mit verschiedenen Korrelationsmethoden korrelieren
fixed_column = 'Fi re'  # Spaltennamen anpassen
correlated_columns = ['Mean', 'Outer Edge Length', 'Surface', 'Variance']  # Spaltennamen anpassen

correlation_methods = ['pearson', 'spearman', 'kendall']  # Liste der gewünschten Korrelationsmethoden

correlation_results = {}
for column in correlated_columns:
    corr_values = []
    for method in correlation_methods:
        corr_value = data[fixed_column].corr(data[column], method=method)
        corr_values.append(corr_value)
    correlation_results[column] = corr_values

# Ausgabedatei erstellen
output_data = pd.DataFrame(correlation_results, index=correlation_methods)
output_path = 'Z13 Korrelationswerte Fi re.csv'
output_data.to_csv(output_path)

print(output_data)
