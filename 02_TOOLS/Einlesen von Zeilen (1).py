import os
import pandas as pd

# Pfad zum Ordner mit den CSV-Dateien angeben
folder_path = '/Users/moritz/PycharmProjects/pythonProject1/Reany Daten/Reany Daten Z13'

# Liste zur Speicherung der Daten und Dateinamen erstellen
daten = []
dateinamen = []

# Alle Dateien im Ordner durchgehen
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        # Pfad zur aktuellen CSV-Datei erstellen
        file_path = os.path.join(folder_path, filename)

        # CSV-Datei in ein DataFrame laden und Trennzeichen angeben
        dataframe = pd.read_csv(file_path, encoding='latin-1')

        # Annahmen zum Spaltennamen und Zeilenbereich treffen
        spaltenname = dataframe.columns[0]  # Name der Spalte, die den Wert enthält
        zeilenbereich = range(31, 35)  # Zeilenbereich für Auswertung

        # Werte auslesen und zur Liste der Daten hinzufügen
        werte = []
        for row_index in zeilenbereich:
            zeile = dataframe.iloc[row_index]  # Ausgewählte Zeile
            wert = zeile[spaltenname]  # Wert in der Spalte
            zahlenwert = float(wert.split(';')[1])  # Zahlenwert befindet sich an zweiter Stelle
            werte.append(zahlenwert)

        daten.append(werte)
        dateinamen.append(filename)

# Erstellen eines DataFrames aus den Daten und Dateinamen
dataframe = pd.DataFrame(daten, columns=[f"Zeile {i + 1}" for i in zeilenbereich])
dataframe.insert(0, "Dateiname", dateinamen)

# Speichern des DataFrames in einer CSV-Datei
output_file = 'ergebnis.csv'
dataframe.to_csv(output_file, index=False)

print(f"Die Ergebnisse wurden in der Datei '{output_file}' gespeichert.")



