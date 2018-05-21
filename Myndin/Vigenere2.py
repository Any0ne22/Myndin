#coding: utf-8
#Denis L.

def vigenere ( phraseAChiffrer, clef, alphabetChoisi) :
    alphabet0 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 "
    alphabet3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789' "

	if alphabetChoisi == 0 :
        alphabet = alphabet0
    elif alphabetChoisi == 1 :
        alphabet = alphabet1
    elif alphabetChoisi == 2 :
        alphabet = alphabet2
    elif alphabetChoisi == 3 :
        alphabet = alphabet3
    else :
        raise ValueError("Alphabet invalide")

	sortie = ""

	for lettre in phraseAChiffrer:
        positionLettre = alphabet.find(lettre)
        if positionLettre == -1 :
            raise ValueError("Caractère invalide")
		positionLettreClef = alphabet.find(lettreClef)
		alphabetDecale = alphabet[positionLettreClef:] + alphabet[:positionLettreClef]
		lettreD = alphabetDecale[positionLettre]
		sortie = sortie + lettreD

	return sortie
   
   
   lettreClef = clef[numeroCaractere % (tailleClef-1)]


   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   def DecodeVigenere(phraseAChiffrer, clef):
    return vigenere(phraseAChiffrer, clef, True)

def CodeVigenere(phraseAChiffrer, clef):
    return vigenere(phraseAChiffrer, clef)


