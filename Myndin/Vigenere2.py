# coding: utf-8
#Denis L.

def vigenereChiffre ( phraseAChiffrer, clef, alphabetChoisi) :
    alphabet0 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 "
    alphabet3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789' "
    alphabet4 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~ ¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöœ÷øùúûüýþÿ\n\r\t\\"
	
    if alphabetChoisi == 0 : #Condition
        alphabet = alphabet0
    elif alphabetChoisi == 1 :
        alphabet = alphabet1
    elif alphabetChoisi == 2 :
        alphabet = alphabet2
    elif alphabetChoisi == 3 :
        alphabet = alphabet3
    elif alphabetChoisi == 4 :
        alphabet = alphabet4
    else :
        raise ValueError("Alphabet invalide") #Message d'erreure

    sortie = "" #Definition de "sortie" comme une variable de texte
    
    numeroLettre = 0 #Donne la position de la lettre dans la phrase a chiffrer
    for lettre in phraseAChiffrer: #Boucle "pour chaque lettre dans la phrase à chiffrer"
        positionLettre = alphabet.find(lettre) #On cherche la position des lettres de la phrase à chiffrer dans l'alphabet choisi
        if positionLettre == -1 :
            print(str(numeroLettre) + ": " +lettre)
            raise ValueError("Caractère invalide: " + lettre) #Erreur si un caractère utilisé n'est pas dans l'alphabet choisi
            
        lettreClef = clef[numeroLettre%len(clef)] #Permet de récupérer la lettre dans la clef
        positionLettreClef = alphabet.find(lettreClef) #On cherche la position des lettres de la clef dans l'alphabet choisi 
        alphabetDecale = alphabet[positionLettreClef:] + alphabet[:positionLettreClef] #Décalage alphabet
        lettreD = alphabetDecale[positionLettre]
        sortie = sortie + lettreD #Ajouter la dernière lettre à la phrase chiffrée
        numeroLettre += 1

    return sortie

   
def vigenereDechiffre ( phraseChiffree, clef, alphabetChoisi) :
   
    alphabet0 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 "
    alphabet3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789' "
    alphabet4 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~ ¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöœ÷øùúûüýþÿ\n\r\t\\"


    if alphabetChoisi == 0 : #Condition
        alphabet = alphabet0
    elif alphabetChoisi == 1 :
        alphabet = alphabet1
    elif alphabetChoisi == 2 :
        alphabet = alphabet2
    elif alphabetChoisi == 3 :
        alphabet = alphabet3
    elif alphabetChoisi == 4 :
        alphabet = alphabet4
    else :
        raise ValueError("Alphabet invalide") #Message d'erreure
   
    sortie = "" #Definition de "sortie" comme une variable de texte
    
    numeroLettre = 0 #Donne la position de la lettre dans la phrase chiffrée
    for lettreChiffree in phraseChiffree: #Boucle "pour chaque lettre dans la phrase chiffrée"
        lettreClef = clef[numeroLettre%len(clef)]
        positionLettreClef = alphabet.find(lettreClef) #On cherche la position des lettres de la clef dans l'alphabet choisi
        alphabetDecale = alphabet[positionLettreClef:] + alphabet[:positionLettreClef] #Décalage alphabet
        positionLettreChiffree = alphabetDecale.find(lettreChiffree) #On cherche la position des lettres de la phrase chiffrée dans l'alphabet décalé
        lettreD = alphabet[positionLettreChiffree]
        sortie = sortie + lettreD #Ajouter la dernière lettre à la phrase chiffrée
        numeroLettre += 1
    return sortie
