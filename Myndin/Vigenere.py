#coding: utf-8
#Pierre H.

def vigenere ( phraseAChiffrer, clef, decode = False) :
   	alphabet26 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
	alphabet52 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
	alphabet62 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 "
	
alphabetDecale = decalage(alphabet26, clef)

	message_code = ""
    for i,c in enumerate(phraseAChiffrer) :
        d = clef[ i % len(clef) ]
        d = ord(d) - 65
        if decode : d = 26 - d
        message_code = message_code + chr((ord(c)-65+d)%26+65)
    return message_code

	alphabetChoisi
	
	if alphabetChoisi == 0 :
		alphabet = alphabet26
	elif alphabetChoisi == 1 :
		aphabet = alphabet52
	elif alphabetChoisi == 2 :
		alphabet = alphabet62
		
def DecodeVigenere(phraseAChiffrer, clef):
    return vigenere(phraseAChiffrer, clef, True)

def CodeVigenere(phraseAChiffrer, clef):
    return vigenere(phraseAChiffrer, clef)
	

