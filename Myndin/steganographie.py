# coding: utf-8
#Tom G.
from PIL import Image
import time

#Constantes
_DEBUTCHAINE = bytearray([0,129])
_FINCHAINE = bytearray([129,0])


def steganographie_ecrire(cheminImage, texteACacher):
    image = ouvrir_fichier(cheminImage)
    if(image != 0):
        tailleImage = taille_image(image)
        tableauCaracteres = bytearray(texteACacher.encode('utf8'))
        
        tableauCaracteres = _DEBUTCHAINE + tableauCaracteres + _FINCHAINE
        
        chaineBinaire = ""
        for i in range(0, len(tableauCaracteres)):
            chaineBinaire += bin(tableauCaracteres[i])[2:].zfill(8)	#Convertion en binaire

        
        if (tailleImage >= len(tableauCaracteres)):
            colonne, ligne = image.size
            
            x = 0
            ligne = int(len(chaineBinaire)/(colonne*3))+ 1 #on reduit le nombre de lignes à parcourir en fonction du nombre de données à cacher
            for l in range(0, ligne):
                for c in range(0, colonne):
                    if (x < len(chaineBinaire)):
                        pixel = image.getpixel((c,l))
                        
                        rouge  = pixel[0]
                        vert = pixel[1]
                        bleu = pixel[2]
                    
                    
                        rouge = rouge - (rouge%2)	#On met le dernier bit du pixel à 0
                        rouge = rouge + int(chaineBinaire[x])
                        x = x + 1
                        if (x < len(chaineBinaire)):
                            vert = vert - (vert%2)
                            vert = vert + int(chaineBinaire[x])
                            x = x + 1
                            if (x < len(chaineBinaire)):
                                bleu = bleu - (bleu%2)
                                bleu = bleu + int(chaineBinaire[x])
                                x = x + 1
                    
                        image.putpixel((c,l),(rouge,vert,bleu))
                    
            image.save(cheminImage)
            image.close()
            return len(tableauCaracteres)*8, tailleImage
        else:
            image.close()
            raise ValueError("Texte à cacher trop long")
            
    else:
        raise ValueError("Chemin invalide")


def steganographie_lire(cheminImage):
    image = ouvrir_fichier(cheminImage)
    if(image != 0):
        colonne, ligne = image.size
        
            
        chaineBinaire = ""
        for l in range(0, ligne):		#On parcours les pixels de l'image
            for c in range(0, colonne):
                pixel = image.getpixel((c,l))
                        
                rouge  = pixel[0]
                vert = pixel[1]
                bleu = pixel[2]
                
                chaineBinaire += (str(rouge%2) + str(vert%2)+ str(bleu%2)) #On recupère le dernier bit de chaque pixel
            
        tableauOctets = []              
        for i in range(0, int((len(chaineBinaire) - len(chaineBinaire)%8)/8)):		#Conversion binaire vers décimal optimisée (gain de temps pour le calcul)
            x = int(chaineBinaire[i*8]) * 128
            x = x + int(chaineBinaire[i*8 + 1]) * 64
            x = x + int(chaineBinaire[i*8 + 2]) * 32
            x = x + int(chaineBinaire[i*8 + 3]) * 16
            x = x + int(chaineBinaire[i*8 + 4]) * 8
            x = x + int(chaineBinaire[i*8 + 5]) * 4
            x = x + int(chaineBinaire[i*8 + 6]) * 2
            x = x + int(chaineBinaire[i*8 + 7]) * 1
            
            if(i > 0 and x == 0 and tableauOctets[i-1] == 129):
                break
                
            tableauOctets.append(x)
            
        tableauOctets = bytearray(tableauOctets) #conversion en tableau d'octets
            
        try:
            debut = tableauOctets.index(_DEBUTCHAINE) 	#on cherche le début des données
            fin = tableauOctets.index(_FINCHAINE)	#on cherche la fin des données
            donnees = tableauOctets[(debut+2):fin] 	#on recupere les donnees qui nous interessent
            return donnees.decode("utf-8")
        except:						#si aucunes données n'ont pas été trouvées
            raise ValueError("Pas de données dans l'image")
            
    else:
        raise ValueError("Chemin invalide")

def ouvrir_fichier(chemin):
    try:
        image=Image.open(chemin)
        return image
    except:
        return 0
    
def taille_image(image):
    colonne, ligne = image.size
    tailleEnBits = colonne * ligne * 3
    return int(tailleEnBits/8)


