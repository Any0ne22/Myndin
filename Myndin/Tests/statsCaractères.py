# coding: utf-8
import codecs

def compteLettre(phrase): # def cesar ...
    tableau = []
    compte = []
    x = 0
    for lettre in phrase:
        try:
            position = tableau.index(lettre)
            compte[position] = compte[position] +1
        except :
            tableau.append(lettre)
            compte.append(1)
        x+= 1
        if(x%100000 == 0):
            print(x)
            
    return tableau, compte

    
stats = codecs.open("./statsFR.txt", encoding="utf-8", mode="r")
texte = stats.read()
stats.close()
tab, cpt = compteLettre(texte)

print("calcul des stats:")
l = len(texte)
sortieLettres = "["
sortieStats = "["
sum = 0
for a in range(0,len(tab)):
    sortieLettres += ",'"+ tab[a] + "'"
    sortieStats += "," + str((cpt[a]/l)*100)
    sum += cpt[a]/l
sortieLettres += "]"
sortieStats += "]"

print(sortieLettres)
print(sortieStats)
print(sum)