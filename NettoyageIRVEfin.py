#Mike Huttenschmitt
#IRVE fin a quelques defauts ;; à la fin de chaque ligne et ligne vide : resolution en dessous.
import csv
input_path="./DonnéesVéhiculesElectriques/IRVE-fin.csv"
output_path="./FichierNettoyéEntier.csv"

with open(input_path, newline='',encoding='utf-8') as in_file:
    with open(output_path, 'w', newline='',encoding='utf-8') as out_file:
        writer = csv.writer(out_file)
        rowNumber=0
        for row in csv.reader(in_file):
            if rowNumber==0:
                # disjonction car l'entête est stocké dans une liste enfaite il suffit de faire row[0][:-2]
                row2=row[0][:-2]
                #on met la première ligne dans tous les outputs
                writer.writerow([row2])
            elif row:
            #en ayant passé ce test on sait que la ligne n'est pas vide alors on enlève les deux derniers caractères
                writer.writerow([row[0][:-2]])
            rowNumber+=1
                
            
        


    