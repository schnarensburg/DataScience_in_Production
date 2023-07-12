import pandas as pd
import csv

#Einlesen der Excel Dateien und löschen von leeren Zellen
df1_input = '../../07_RESULTS/Frenco/Datenauswertung-Frenco.csv'
df1 = pd.read_csv(df1_input)
df1 = df1.dropna()

# df2_input = 'C:/Users/siewe/TeamprojektDataScience/Daten/Input/Z13-Datensammlung.csv'
df2_input = '../../07_RESULTS/Frenco/Z13-Datensammlung.csv'
df2 = pd.read_csv(df2_input)
df2 = df2.dropna()

# df3_input = 'C:/Users/siewe/TeamprojektDataScience/Daten/Input/Z19-Datensammlung.csv'
df3_input = '../../07_RESULTS/Frenco/Z19-Datensammlung.csv'
df3 = pd.read_csv(df3_input)
df3 = df3.dropna()

#Auswahl der Zellenwerte die in der Frenco Datenauswertung erfasst worden sind
merged_df1 = pd.merge(df1, df2, how='inner', on='Z13')
merged_df2 = pd.merge(df1, df3, how='inner', on='Z19')

#Speicherung der jeweiligen Parameter in Variablen aus Z13 Datensammlung
Fi_li1 = merged_df1['Fi li'].tolist()
Fi_re1 = merged_df1['Fi re'].tolist()
fl_li1 = merged_df1['fl li'].tolist()
fl_re1 = merged_df1['fl re'].tolist()
fk_li1 = merged_df1['fk li'].tolist()
fk_re1 = merged_df1['fk re'].tolist()
fi_li1 = merged_df1['fi li'].tolist()
fi_re1 = merged_df1['fi re'].tolist()

#Speicherung der jeweiligen Parameter in Variablen aus Z19 Datensammlung
Fi_li2 = merged_df2['Fi li'].tolist()
Fi_re2 = merged_df2['Fi re'].tolist()
fl_li2 = merged_df2['fl li'].tolist()
fl_re2 = merged_df2['fl re'].tolist()
fk_li2 = merged_df2['fk li'].tolist()
fk_re2 = merged_df2['fk re'].tolist()
fi_li2 = merged_df2['fi li'].tolist()
fi_re2 = merged_df2['fi re'].tolist()

#Speicherung der jeweiligen Parameter in Variablen aus Z13 Datensammlung
Mean1 = merged_df1['Mean'].tolist()

#Speicherung der jeweiligen Parameter in Variablen aus Z19 Datensammlung
Mean2 = merged_df2['Mean'].tolist()

#Speicherung der jeweiligen Parameter in Variablen aus Z13 Datensammlung
OuterEdgeLength1 = merged_df1['Outer Edge Length'].tolist()

#Speicherung der jeweiligen Parameter in Variablen aus Z19 Datensammlung
OuterEdgeLength2 = merged_df2['Outer Edge Length'].tolist()

#Speicherung der jeweiligen Parameter in Variablen aus Z13 Datensammlung
Surface1 = merged_df1['Surface'].tolist()

#Speicherung der jeweiligen Parameter in Variablen aus Z19 Datensammlung
Surface2 = merged_df2['Surface'].tolist()

#Speicherung der jeweiligen Parameter in Variablen aus Z13 Datensammlung
Variance1 = merged_df1['Variance'].tolist()

#Speicherung der jeweiligen Parameter in Variablen aus Z19 Datensammlung
Variance2 = merged_df2['Variance'].tolist()

#Speicherung der jeweiligen Parameter in Variablen aus Z13 Datensammlung
Max_Deviation1 = merged_df1['Max_Deviation'].tolist()

#Speicherung der jeweiligen Parameter in Variablen aus Z19 Datensammlung
Max_Deviation2 = merged_df2['Max_Deviation'].tolist()

#Speicherung der jeweiligen Parameter in Variablen aus Z13 Datensammlung
Min_Deviation1 = merged_df1['Min_Deviation'].tolist()

#Speicherung der jeweiligen Parameter in Variablen aus Z19 Datensammlung
Min_Deviation2 = merged_df2['Min_Deviation'].tolist()

#Speicherung der jeweiligen Parameter in Variablen aus Z13 Datensammlung
Span_Deviation1 = merged_df1['Span_Deviation'].tolist()

#Speicherung der jeweiligen Parameter in Variablen aus Z19 Datensammlung
Span_Deviation2 = merged_df2['Span_Deviation'].tolist()

# Funktion zum Schreiben der ersten Zeile mit den Namen der Parameter
def write_header(csv_writer):
    header = ['Z13', 'Z19', 'MeanZ13', 'MeanZ19', 'OuterEdgeLengthZ13', 'OuterEdgeLengthZ19', 'SurfaceZ13', 'SurfaceZ19' , 'VarianceZ13', 'VarianceZ19', 'Max_DeviationZ13', 'Max_DeviationZ19', 'Min_DeviationZ13', 'Min_DeviationZ19', 'Span_DeviationZ13', 'Span_DeviationZ19', 'Fi_liZ13', 'Fi_liZ19', 'Fi_reZ13', 'Fi_reZ19', 'fl_liZ13', 'fl_liZ19', 'fl_reZ13', 'fl_reZ19', 'fk_liZ13', 'fk_liZ19', 'fk_reZ13', 'fk_reZ19', 'fi_liZ13', 'fi_liZ19', 'fi_reZ13', 'fi_reZ19','Wälzfehler VW', 'Wälzfehler RW', 'Wälzsprung VW', 'Wälzsprung RW']

    csv_writer.writerow(header)

# Öffne die CSV-Datei im Schreibmodus
with open('../../07_RESULTS/Frenco/output_frencomatching.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    write_header(writer)

    # Schreibe die Array-Daten spaltenweise in die CSV-Datei
    for row in zip(df1['Z13'], df1['Z19'], Mean1, Mean2, OuterEdgeLength1, OuterEdgeLength2, Surface1, Surface2, Variance1, Variance2, Max_Deviation1, Max_Deviation2, Min_Deviation1, Min_Deviation2, Span_Deviation1, Span_Deviation2, Fi_li1, Fi_li2, Fi_re1, Fi_re2, fl_li1, fl_li2, fl_re1, fl_re2, fk_li1, fk_li2, fk_re1, fk_re2, fi_li1, fi_li2, fi_re1, fi_re2, df1["Wälzfehler VW"], df1["Wälzfehler RW"], df1["Wälzsprung VW"], df1["Wälzsprung RW"]):
        writer.writerow(row)
