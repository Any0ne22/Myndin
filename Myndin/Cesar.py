#coding: utf-8
#Denis L.

def cesar(phraseAChiffrer, decalage, alphabetChoisi): # def cesar ...
	alphabet0 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
	alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
	alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 "
	alphabet3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789' \n"
	
	alphabet = ""
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
		
	
	
	tailleAlphabet = len(alphabet)
	sortie = ""
	
	for lettre in phraseAChiffrer:
		position = alphabet.find(lettre)
		if position == -1 :
			raise ValueError("Caractère invalide")
		positionD = (position + decalage) % tailleAlphabet
		lettreD = alphabet[positionD]
		sortie = sortie + lettreD
	
	
	return sortie
	
