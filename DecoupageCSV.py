#Mike Huttenschmitt
#Script de decoupage de fichier csv en n parties, n au choix.
#IRVE fin a quelques defauts ;; à la fin de chaque ligne et ligne vide : resolution en dessous.
import csv
input_path="./DonnéesVéhiculesElectriques/IRVE-fin.csv"
output_path="./FichierNettoyé"

# d'abord on compte le nombre de lignes
with open(input_path, newline='',encoding='utf-8') as in_file:
    rowTot = sum(1 for row in in_file)
    print(rowTot)
#On recommence
with open(input_path, newline='',encoding='utf-8') as in_file:
    # on va couper le fichier en n parties.
    #on cherche les endroits ou le changement de fichier va se faire
    n=6
    out=[output_path+str(k)+".csv"for k in range(n)]
    first_cut=rowTot//n
    cuts=[(k+1)*first_cut for k in range(n-1)]
    
    rowNumber=0
    # on ne peux pas ouvrir toutes les fichiers en écriture en dehors de la boucle
    # donc on le fais dedans et on utilise un boolen pour savoir quand
    changeOfWritingFile=False
    currentFile=0 #on commence par écrire dans le fichier 0
    #on parcours ligne par ligne :
    for row in csv.reader(in_file):
        if rowNumber==0:
            # disjonction de cas car on a besoin de l'en-tête pour chaque sous-fichier
            rowHead=[row[0][:-2]] #ligne a commenter si decoupage uniquement
            #rowHead=row utilise cette ligne si il faut seulement découper le fichier sans nettoyage
            out_file = open(out[currentFile], 'w', newline='',encoding='utf-8')
            print("opening"+str(out[currentFile]))
            writer = csv.writer(out_file)
            writer.writerow(rowHead)
        else :
            if changeOfWritingFile:
                #si on change de fichier on ferme l'ancienne ecriture on ajoute l'en-tête et n ouvre l'écriture
                out_file.close()
                print("closing"+str(out[currentFile]))
                currentFile+=1
                out_file = open(out[currentFile], 'w', newline='',encoding='utf-8')
                print("opening"+str(out[currentFile]))
                writer = csv.writer(out_file)
                writer.writerow(rowHead)
                changeOfWritingFile=False
            if row:
                writer.writerow([row[0][:-2]]) # ligne a commenter si decoupage uniquement
                #writer.writerow(row) on utilise cette ligne si il faut seulement découper le fichier sans nettoyage
                changeOfWritingFile=(rowNumber in cuts)            
        rowNumber+=1
        if rowNumber==(rowTot):
            # si on est à la dernière ligne on ferme le fichier en écriture
            out_file.close()
            print("closing"+str(out[currentFile]))
            break

