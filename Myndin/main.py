# coding: utf-8
#Tom G.
#https://github.com/Any0ne22/Myndin
from tkinter import *
from EZcipher import *
from Cesar import *
from CasseCesar import *
from Vigenere2 import *
from steganographie import *
import codecs

#Fenetre de base   
mainWindow = Tk()
mainWindow.geometry("960x585")
mainWindow.resizable(YES,YES)
mainWindow.title("Myndin")

framePage = 0	#appelé avec 'global framePage' pour l'acces depuis les fonctions

#Fonctions de l'interface
def nettoyer_fenetre():
    #supprime la frame contenant les elements de la fenetre si elle est définie
    global framePage
    if framePage != 0:
        framePage.pack_forget()
        framePage = 0
        
        
class menu_principal:
    def __init__(self):
        #definition des elements de l'interface
        self.frameContenu = Frame(mainWindow, borderwidth=2, relief=GROOVE)
        self.frameContenu.pack(fill='y')
        
        self.labelDeplacement=Label(self.frameContenu ,text='Bienvenue dans Myndin')
        self.boutonChiffrerTexte = Button(self.frameContenu, text="Chiffrer du texte", command=self.menu_chiffrer_texte)
        self.boutonChiffrerFichier = Button(self.frameContenu, text="Chiffrer un fichier", command=self.menu_chiffrer_fichier)
        self.boutonCryptoAsymetrique = Button(self.frameContenu, text="Cryptographie asymétrique", command=self.menu_cryptographie_asymetrique)
        self.boutonSteganographie = Button(self.frameContenu, text="Stéganographie", command=self.menu_steganographie)
        self.boutonDecryptage = Button(self.frameContenu, text="Casser le code de César", command=self.menu_crack_cesar)
        self.labelInfos=Label(self.frameContenu ,text='Denis L. / Pierre H. / Tom G.')

    def affichage(self):
        nettoyer_fenetre()
        global framePage
        self.__init__() #on reinitialise la page
        framePage = self.frameContenu
        self.labelDeplacement.grid(row=0,column=0, padx=10, pady=10)
        self.boutonChiffrerTexte.grid(row=1,column=0, pady=10)
        self.boutonChiffrerFichier.grid(row=2,column=0, pady=10)
        self.boutonCryptoAsymetrique.grid(row=3,column=0, pady=10, padx=10)
        self.boutonSteganographie.grid(row=4,column=0, pady=10)
        self.boutonDecryptage.grid(row=5,column=0, pady=10)
        self.labelInfos.grid(row=6,column=0, pady=20)

    def menu_chiffrer_texte(self):
        global menu_chiffrer_texte
        menu_chiffrer_texte.affichage()

    def menu_chiffrer_fichier(self):
        global menu_chiffrer_fichier
        menu_chiffrer_fichier.affichage()
    
    def menu_cryptographie_asymetrique(self):
        global menu_cryptographie_asymetrique
        menu_cryptographie_asymetrique.affichage()

    def menu_steganographie(self):
        global menu_steganographie
        menu_steganographie.affichage()

    def menu_crack_cesar(self):
        global menu_crack_cesar
        menu_crack_cesar.affichage()
    

class menu_chiffrer_texte:
    def __init__(self):
        #definition des elements de l'interface
        self.frameContenu = Frame(mainWindow, borderwidth=2, relief=GROOVE)
        self.frameContenu.pack(fill='y')
        
        self.boutonRetour = Button(self.frameContenu, text="Retour", command=self.retour_menu_principal)
        self.labelDeplacement = Label(self.frameContenu ,text='Chiffrer du texte')
        self.labelTexteAChiffrer = Label(self.frameContenu, text='Entrée')
        self.TextTexteAChiffrer = Text(self.frameContenu, height=5, width=50)
        self.labelCle = Label(self.frameContenu, text='Clé')
        self.EntryCle = Entry(self.frameContenu, width=44)
        self.ListBoxChiffrement = Listbox(self.frameContenu, height=2)
        self.labelTexteSortie = Label(self.frameContenu, text='Sortie')
        self.TextTexteSortie = Text(self.frameContenu, height=5, width=50)
        self.boutonChiffrer = Button(self.frameContenu, text="Chiffrer", command=self.chiffrer_texte)
        self.boutonDechiffrer = Button(self.frameContenu, text="Déchiffrer", command=self.dechiffrer_texte)
        self.statut = StringVar()
        self.labelStatut = Label(self.frameContenu ,textvariable=self.statut)
        self.statut.set("Statut:")
        self.labelInformations = Label(self.frameContenu, text="Informations: Les clef pour le chiffrement de César sont des nombres entiers", justify=LEFT)        

    def affichage(self):
        nettoyer_fenetre()
        global framePage
        self.__init__() #on reinitialise la page
        framePage = self.frameContenu
        self.boutonRetour.grid(row=0,column=0, pady=10, sticky=W)
        self.labelDeplacement.grid(row=0,column=1, columnspan=2, padx=10, pady=5)
        self.labelTexteAChiffrer.grid(row=1,column=0, padx=10, pady=5, sticky=N)
        self.TextTexteAChiffrer.grid(row=1,column=1, columnspan=2, rowspan=2, pady=5)
        self.TextTexteAChiffrer.insert(END, "Texte à chiffrer")
        self.labelCle.grid(row=3,column=0, padx=10, pady=5, sticky=N)
        self.EntryCle.grid(row=3, column=1, columnspan=2, pady=5)
        self.ListBoxChiffrement.grid(row=3, column=3, pady=5)
        self.ListBoxChiffrement.insert(1, "César")
        self.ListBoxChiffrement.insert(2, "Vigenère")
        self.labelTexteSortie.grid(row=4,column=0, padx=10, pady=5, sticky=N)
        self.TextTexteSortie.grid(row=4, column=1, columnspan=2, padx=10, pady=5)
        self.TextTexteSortie.insert(END, "Texte chiffré")
        self.boutonChiffrer.grid(row=1,column=3, pady=5, sticky=N)
        self.boutonDechiffrer.grid(row=2,column=3, pady=5, sticky=N)
        self.labelStatut.grid(row=6, column=0, columnspan=3, pady=5, padx=10, sticky=W)
        self.labelInformations.grid(row=7, column=0, columnspan=4, pady=5, padx=10, sticky=W)
    
    def retour_menu_principal(self):
        global menu_principal
        menu_principal.affichage()

    def chiffrer_texte(self):
        selectionAlgo = None
        try:
            selectionAlgo = self.ListBoxChiffrement.curselection()[0]
        except Exception as e:
            self.statut.set("Statut: Veuillez selectionner un algorithme de chiffrement!")

        if selectionAlgo != None:
            texteClair = self.TextTexteAChiffrer.get(1.0, END)
            if texteClair[-1] == "\n":
                texteClair = texteClair[0:-1]
            cle = self.EntryCle.get()
            cle = self.EntryCle.get()
            if cle == "":
                self.statut.set("Statut: veuillez entrer une clé!")
            else:
                if selectionAlgo == 0:	#Cesar
                    if str.isnumeric(cle):
                        try:
                            self.TextTexteSortie.delete(1.0, END)
                            texteChiffre = cesar(texteClair, int(cle), 4)
                            self.TextTexteSortie.insert(END, texteChiffre)
                            self.statut.set("Statut: Chiffrement effectué!")
                        except ValueError as e:
                            self.statut.set("Statut: Caractère invalide!")
                    
                    else:
                        self.statut.set("Statut: Clé invalide!")
                elif selectionAlgo == 1:			#Vigenère
                    try:
                        texteChiffre = vigenereChiffre(texteClair, cle, 4)
                        self.TextTexteSortie.delete(1.0, END)
                        self.TextTexteSortie.insert(END, texteChiffre)
                        self.statut.set("Statut: Chiffrement effectué!")
                    except ValueError as e:
                        self.statut.set("Statut: Caractère invalide!")
    
    def dechiffrer_texte(self):
        selectionAlgo = None
        try:
            selectionAlgo = self.ListBoxChiffrement.curselection()[0]
        except Exception as e:
            self.statut.set("Statut: Veuillez selectionner un algorithme de chiffrement!")

        if selectionAlgo != None:
            texteChiffre = self.TextTexteAChiffrer.get(1.0, END)
            if texteChiffre[-1] == "\n":
                texteChiffre = texteChiffre[0:-1]
            cle = self.EntryCle.get()
            if cle == "":
                self.statut.set("Statut: veuillez entrer une clé!")
            else:
                if selectionAlgo == 0:	#Cesar
                    if str.isnumeric(cle):
                        try:
                            self.TextTexteSortie.delete(1.0, END)
                            texteClair = cesar(texteChiffre, -int(cle), 4)
                            self.TextTexteSortie.insert(END, texteClair)
                            self.statut.set("Statut: Déchiffrement effectué!")
                        except ValueError as e:
                            self.statut.set("Statut: Erreur lors du déchiffrement!")
                        
                    else:
                        self.statut.set("Statut: Clé invalide!")
                elif selectionAlgo == 1:			#Vigenère
                    try:
                        texteClair = vigenereDechiffre(texteChiffre, cle, 4)
                        self.TextTexteSortie.delete(1.0, END)
                        self.TextTexteSortie.insert(END, texteClair)
                        self.statut.set("Statut: Déchiffrement effectué!")
                    except ValueError as e:
                        self.statut.set("Statut: Erreur lors du déchiffrement!")


class menu_chiffrer_fichier:
    def __init__(self):
        #definition des elements de l'interface
        self.frameContenu = Frame(mainWindow, borderwidth=2, relief=GROOVE)
        self.frameContenu.pack(fill='y')
        
        self.boutonRetour = Button(self.frameContenu, text="Retour", command=self.retour_menu_principal)
        self.labelDeplacement = Label(self.frameContenu ,text='Chiffrer un fichier')
        self.labelTexteAChiffrer = Label(self.frameContenu, text='Emplacement du fichier à (dé)chiffrer')
        self.EntryFichierAChiffrer = Entry(self.frameContenu, width=44)
        self.labelCle = Label(self.frameContenu, text='Clé')
        self.EntryCle = Entry(self.frameContenu, width=44)
        self.ListBoxChiffrement = Listbox(self.frameContenu, height=2)
        self.labelTexteSortie = Label(self.frameContenu, text='Emplacement du fichier (dé)chiffré')
        self.EntryFichierSortie = Entry(self.frameContenu, width=44)
        self.boutonChiffrer = Button(self.frameContenu, text="Chiffrer", command=self.chiffrer_texte)
        self.boutonDechiffrer = Button(self.frameContenu, text="Déchiffrer", command=self.dechiffrer_texte)
        self.statut = StringVar()
        self.labelStatut = Label(self.frameContenu ,textvariable=self.statut)
        self.statut.set("Statut:")
        self.labelInformations = Label(self.frameContenu, text="Informations: Les clef pour le chiffrement de César sont des nombres entiers", justify=LEFT)        

    def affichage(self):
        nettoyer_fenetre()
        global framePage
        self.__init__() #on reinitialise la page
        framePage = self.frameContenu
        self.boutonRetour.grid(row=0,column=0, pady=10, sticky=W)
        self.labelDeplacement.grid(row=0,column=1, columnspan=2, padx=10, pady=5)
        self.labelTexteAChiffrer.grid(row=1,column=0, padx=10, pady=5, sticky=N)
        self.EntryFichierAChiffrer.grid(row=1,column=1, columnspan=2, rowspan=2, pady=5, sticky=N)
        self.labelCle.grid(row=3,column=0, padx=10, pady=5, sticky=N)
        self.EntryCle.grid(row=3, column=1, columnspan=2, pady=5, sticky=N)
        self.ListBoxChiffrement.grid(row=3, column=3, pady=5)
        self.ListBoxChiffrement.insert(1, "César")
        self.ListBoxChiffrement.insert(2, "Vigenère")
        self.labelTexteSortie.grid(row=4,column=0, padx=10, pady=5, sticky=N)
        self.EntryFichierSortie.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

        self.boutonChiffrer.grid(row=1,column=3, pady=5, sticky=N)
        self.boutonDechiffrer.grid(row=2,column=3, pady=5, sticky=N)
        self.labelStatut.grid(row=6, column=0, columnspan=3, pady=5, padx=10, sticky=W)
        self.labelInformations.grid(row=7, column=0, columnspan=4, pady=5, padx=10, sticky=W)
    
    def retour_menu_principal(self):
        global menu_principal
        menu_principal.affichage()

    def chiffrer_texte(self):
        selectionAlgo = None
        try:
            selectionAlgo = self.ListBoxChiffrement.curselection()[0]
        except Exception as e:
            self.statut.set("Statut: Veuillez selectionner un algorithme de chiffrement!")

        if selectionAlgo != None:
            emplacementFichier = self.EntryFichierAChiffrer.get()
            if emplacementFichier == "":
                self.statut.set("Statut: veuillez préciser un fichier d'entrée!")
            else:
                texte=""
                try:
                    fichier = codecs.open(emplacementFichier, encoding="utf-8", mode="r")
                    texte = fichier.read()
                    print(texte)
                    fichier.close()
                except:
                    self.statut.set("Statut: fichier d'entrée introuvable!")
                cle = self.EntryCle.get()
                if cle == "":
                    self.statut.set("Statut: veuillez entrer une clé!")
                else:
                    if selectionAlgo == 0:	#Cesar
                        if str.isnumeric(cle):
                            try:
                                texteChiffre = cesar(texte, int(cle), 4)
                                fichierSortie = self.EntryFichierSortie.get()
                                if fichierSortie == "":
                                    fichier = codecs.open(emplacementFichier, encoding="utf-8", mode="w")
                                else:
                                    fichier = codecs.open(fichierSortie, encoding="utf-8", mode="w")
                                fichier.write(texteChiffre)
                                fichier.close()
                                self.statut.set("Statut: Chiffrement effectué!")
                            except ValueError as e:
                                self.statut.set("Statut: Caractère invalide!")
                        
                        else:
                            self.statut.set("Statut: Clé invalide!")
                    elif selectionAlgo == 1:			#Vigenère
                        try:
                            texteChiffre = vigenereChiffre(texte, cle, 4)
                            fichierSortie = self.EntryFichierSortie.get()
                            if fichierSortie == "":
                                fichier = codecs.open(emplacementFichier, encoding="utf-8", mode="w")
                            else:
                                fichier = codecs.open(fichierSortie, encoding="utf-8", mode="w")
                            fichier.write(texteChiffre)
                            fichier.close()
                            self.statut.set("Statut: Chiffrement effectué!")
                        except ValueError as e:
                            self.statut.set("Statut: Caractère invalide!")
    
    def dechiffrer_texte(self):
        selectionAlgo = None
        try:
            selectionAlgo = self.ListBoxChiffrement.curselection()[0]
        except Exception as e:
            self.statut.set("Statut: Veuillez selectionner un algorithme de chiffrement!")

        if selectionAlgo != None:
            emplacementFichier = self.EntryFichierAChiffrer.get()
            if emplacementFichier == "":
                self.statut.set("Statut: veuillez préciser un fichier d'entrée!")
            else:
                texte=""
                try:
                    fichier = codecs.open(emplacementFichier, encoding="utf-8", mode="r")
                    texte = fichier.read()
                    fichier.close()
                except:
                    self.statut.set("Statut: fichier d'entrée introuvable!")
                cle = self.EntryCle.get()
                if cle == "":
                    self.statut.set("Statut: veuillez entrer une clé!")
                else:
                    if selectionAlgo == 0:	#Cesar
                        if str.isnumeric(cle):
                            try:
                                texteDechiffre = cesar(texte, -int(cle), 4)
                                fichierSortie = self.EntryFichierSortie.get()
                                if fichierSortie == "":
                                    fichier = codecs.open(emplacementFichier, encoding="utf-8", mode="w")
                                else:
                                    fichier = codecs.open(fichierSortie, encoding="utf-8", mode="w")
                                fichier.write(texteDechiffre)
                                fichier.close()
                                self.statut.set("Statut: Déchiffrement effectué!")
                            except ValueError as e:
                                self.statut.set("Statut: Caractère invalide!")
                        
                        else:
                            self.statut.set("Statut: Clé invalide!")
                    elif selectionAlgo == 1:			#Vigenère
                        try:
                            texteDechiffre = vigenereDechiffre(texte, cle, 4)
                            fichierSortie = self.EntryFichierSortie.get()
                            if fichierSortie == "":
                                fichier = codecs.open(emplacementFichier, encoding="utf-8", mode="w")
                            else:
                                fichier = codecs.open(fichierSortie, encoding="utf-8", mode="w")
                            fichier.write(texteDechiffre)
                            fichier.close()
                            self.statut.set("Statut: Déchiffrement effectué!")
                        except ValueError as e:
                            self.statut.set("Statut: Caractère invalide!")


class menu_cryptographie_asymetrique:
    def __init__(self):
        #definition des elements de l'interface
        self.frameContenu = Frame(mainWindow, borderwidth=2, relief=GROOVE)
        self.frameContenu.pack(fill='y')
        
        self.boutonRetour = Button(self.frameContenu, text="Retour", command=self.retour_menu_principal)
        self.labelDeplacement = Label(self.frameContenu ,text='Cryptographie asymétrique')
        
        self.labelClePrivee = Label(self.frameContenu ,text='Clé privée')
        self.TextClePrivee = Text(self.frameContenu, height=5, width=50)
        self.labelClePublique = Label(self.frameContenu, text='Clé publique')
        self.TextClePublique = Text(self.frameContenu, height=5, width=50)
        self.boutonGenererCle = Button(self.frameContenu, text="Générer les clés", command=self.generer_cles)
        self.labelCle = Label(self.frameContenu, text='Taille des clefs:')
        self.EntryCle = Entry(self.frameContenu, width=8)

        self.labelTexteAChiffrer = Label(self.frameContenu, text='Entrée')
        self.TextTexteAChiffrer = Text(self.frameContenu, height=5, width=50)
        self.labelTexteSortie = Label(self.frameContenu, text='Sortie')
        self.TextTexteSortie = Text(self.frameContenu, height=5, width=50)
        self.boutonChiffrer = Button(self.frameContenu, text="Chiffrer", command=self.chiffrer_texte)
        self.boutonDechiffrer = Button(self.frameContenu, text="Déchiffrer", command=self.dechiffrer_texte)
        self.statut = StringVar()
        self.labelStatut = Label(self.frameContenu ,textvariable=self.statut)
        self.statut.set("Statut:")
        self.labelInformations = Label(self.frameContenu, text="Informations: La génération des clés peut prendre plusieurs secondes.\nLes tailles de clés doivent être multiples de 8 et être comprises entre 512 et 16384.", justify=LEFT)
        
    def affichage(self):
        nettoyer_fenetre()
        global framePage
        self.__init__() #on reinitialise la page
        framePage = self.frameContenu
        self.boutonRetour.grid(row=0,column=0, pady=10, sticky=W)
        self.labelDeplacement.grid(row=0,column=1, columnspan=2, padx=10, pady=5)

        self.labelClePrivee.grid(row=1,column=0, padx=10, pady=5, sticky=N)
        self.TextClePrivee.grid(row=1,column=1, columnspan=2, rowspan=2, pady=5)
        self.labelClePublique.grid(row=4,column=0, padx=10, pady=5, sticky=N)
        self.TextClePublique.grid(row=4, column=1, columnspan=2, padx=10, pady=5)
        self.boutonGenererCle.grid(row=2,column=3, pady=10, sticky=S)
        self.labelCle.grid(row=1,column=3, pady=0, sticky=N)
        self.EntryCle.grid(row=1,column=3, pady=0, sticky=S)
        self.EntryCle.insert(0, "2048")

        self.labelTexteAChiffrer.grid(row=5,column=0, padx=10, pady=5, sticky=N)
        self.TextTexteAChiffrer.grid(row=5,column=1, columnspan=2, rowspan=2, pady=5)
        self.TextTexteAChiffrer.insert(END, "Texte à chiffrer")
        self.labelTexteSortie.grid(row=8,column=0, padx=10, pady=5, sticky=N)
        self.TextTexteSortie.grid(row=8, column=1, columnspan=2, padx=10, pady=5)
        self.TextTexteSortie.insert(END, "Texte chiffré")

        self.boutonChiffrer.grid(row=5,column=3, pady=5, sticky=N)
        self.boutonDechiffrer.grid(row=6,column=3, pady=5, sticky=N)
        self.labelStatut.grid(row=9, column=0, columnspan=3, pady=5, padx=10, sticky=W)
        self.labelInformations.grid(row=10, column=0, columnspan=4, pady=5, padx=10, sticky=W)

    def retour_menu_principal(self):
        global menu_principal
        menu_principal.affichage()

    def generer_cles(self):
        rsa = CryptoRSA()
        tailleCle = self.EntryCle.get()
        if str.isnumeric(tailleCle):
            try:
                rsa.GenerateKeys(int(tailleCle))
                self.TextClePrivee.delete(1.0, END)
                self.TextClePrivee.insert(END, rsa.ExportPrivateKeyString())
                self.TextClePublique.delete(1.0, END)
                self.TextClePublique.insert(END, rsa.ExportPublicKeyString())
                self.statut.set("Statut: Clés générées!")
            except Exception as e:
                self.statut.set("Statut: Taille de clé invalide!")
        else:
            self.statut.set("Statut: Taille de clé invalide!")

    def chiffrer_texte(self):
        clePublique = self.TextClePublique.get(1.0, END)
        texteClair = self.TextTexteAChiffrer.get(1.0, END)
        rsa = CryptoRSA()
        try:
            rsa.ImportPublicKeyString(clePublique)
            try:
                texteChiffre = rsa.EncryptString(texteClair)
                self.TextTexteSortie.delete(1.0, END)
                self.TextTexteSortie.insert(END, texteChiffre)
                self.statut.set("Statut: Chiffrement effectué!")
            except Exception as e:
                self.statut.set("Statut: Erreur de chiffrement (trop de données à chiffrer)")
        except Exception as e:
            self.statut.set("Statut: Erreur d'importation de la clé publique")
        


    def dechiffrer_texte(self):
        clePrivee = self.TextClePrivee.get(1.0, END)
        texteChiffre = self.TextTexteAChiffrer.get(1.0, END)
        rsa = CryptoRSA()
        
        try:
            rsa.ImportPrivateKeyString(clePrivee)
            try:
                texteClair = rsa.DecryptString(texteChiffre)
                self.TextTexteSortie.delete(1.0, END)
                self.TextTexteSortie.insert(END, texteClair)
                self.statut.set("Statut: Déchiffrement effectué!")
            except Exception as e:
                self.statut.set("Statut: Erreur de déchiffrement (données incorrectes)")
        except Exception as e:
            self.statut.set("Statut: Erreur d'importation de la clé privée")
        

class menu_steganographie:
    def __init__(self):
        #definition des elements de l'interface
        self.frameContenu = Frame(mainWindow, borderwidth=2, relief=GROOVE)
        self.frameContenu.pack(fill='y')
        
        self.boutonRetour = Button(self.frameContenu, text="Retour", command=self.retour_menu_principal)
        self.labelDeplacement = Label(self.frameContenu ,text='Cacher des données dans une image')
        self.labelDonnees = Label(self.frameContenu, text='Données')
        self.TextDonnees = Text(self.frameContenu, height=5, width=50)
        self.labelLienImage = Label(self.frameContenu, text='Chemin de l\'image')
        self.EntryLienImage = Entry(self.frameContenu, width=44)
        self.statut = StringVar()
        self.labelStatut = Label(self.frameContenu ,textvariable=self.statut)
        self.statut.set("Statut:")
        self.labelInformations = Label(self.frameContenu, text="\n\nInformations: La lecture ou l'écriture des données peut prendre plusieurs secondes selon la taille de l'image.\nLes images utilisant la transparence alpha peuvent être altérées par le programme.", justify=LEFT)

        self.boutonEcrire = Button(self.frameContenu, text="Enregister données", command=self.ecrire_donnees)
        self.boutonLire = Button(self.frameContenu, text="Lire données", command=self.lire_donnees)
        
    def affichage(self):
        nettoyer_fenetre()
        global framePage
        self.__init__() #on reinitialise la page
        framePage = self.frameContenu
        self.boutonRetour.grid(row=0,column=0, pady=10, sticky=W)
        self.labelDeplacement.grid(row=0,column=1, columnspan=2, padx=10, pady=5)
        self.labelDonnees.grid(row=1,column=0, padx=10, pady=5, sticky=N)
        self.TextDonnees.grid(row=1,column=1, columnspan=2, rowspan=2, pady=5)
        self.TextDonnees.insert(END, "Données")
        self.labelLienImage.grid(row=3,column=0, padx=10, pady=5, sticky=N)
        self.EntryLienImage.grid(row=3, column=1, columnspan=2, pady=5)
        self.labelStatut.grid(row=4, column=0, columnspan=3, pady=5, padx=10, sticky=W)
        self.labelInformations.grid(row=5, column=0, columnspan=4, pady=5, padx=10, sticky=W)

        self.boutonEcrire.grid(row=1,column=3, pady=5, sticky=N)
        self.boutonLire.grid(row=2,column=3, pady=5, sticky=N)
    
    def retour_menu_principal(self):
        global menu_principal
        menu_principal.affichage()

    def ecrire_donnees(self):
        texteClair = self.TextDonnees.get(1.0, END)
        lienImage = self.EntryLienImage.get()
        texteClair = texteClair[0:-1]
        try:
            tailleTexte, tailleImage = steganographie_ecrire(lienImage, texteClair)
            self.statut.set("Statut: Enregistré (" + str(tailleTexte) + "/" + str(tailleImage) + " bits)")
        except ValueError as e:
            self.statut.set("Statut: Erreur (" + str(e) + ")")

    def lire_donnees(self):
        lienImage = self.EntryLienImage.get()

        try:
            donnees = steganographie_lire(lienImage)
            self.TextDonnees.delete(1.0, END)
            self.TextDonnees.insert(END, donnees)
            self.statut.set("Statut: Données lues")
        except ValueError as e:
            self.statut.set("Statut: Erreur (" + str(e) + ")")

class menu_crack_cesar:
    def __init__(self):
        #definition des elements de l'interface
        self.frameContenu = Frame(mainWindow, borderwidth=2, relief=GROOVE)
        self.frameContenu.pack(fill='y')
        
        self.boutonRetour = Button(self.frameContenu, text="Retour", command=self.retour_menu_principal)
        self.labelDeplacement = Label(self.frameContenu ,text='Casser le code de César')
        self.labelTexteAChiffrer = Label(self.frameContenu, text='Texte à décrypter')
        self.TextTexteADecrypter = Text(self.frameContenu, height=5, width=50)
        self.labelTexteSortie = Label(self.frameContenu, text='Texte déchiffré')
        self.TextTexteSortie = Text(self.frameContenu, height=5, width=50)
        self.boutonDecrypter = Button(self.frameContenu, text="Décrypter", command=self.decrypter_texte)
        self.statut = StringVar()
        self.labelStatut = Label(self.frameContenu ,textvariable=self.statut)
        self.statut.set("Statut:")
        self.labelInformations = Label(self.frameContenu, text="Informations: Cette méthode de déchiffrement a été optimisée pour la langue française et fonctionne mieux sur des messages longs.", justify=LEFT)        

    def affichage(self):
        nettoyer_fenetre()
        global framePage
        self.__init__() #on reinitialise la page
        framePage = self.frameContenu
        self.boutonRetour.grid(row=0,column=0, pady=10, sticky=W)
        self.labelDeplacement.grid(row=0,column=1, columnspan=2, padx=10, pady=5)
        self.labelTexteAChiffrer.grid(row=1,column=0, padx=10, pady=5, sticky=N)
        self.TextTexteADecrypter.grid(row=1,column=1, columnspan=2, rowspan=2, pady=5)
        self.labelTexteSortie.grid(row=3,column=0, padx=10, pady=5, sticky=N)
        self.TextTexteSortie.grid(row=3, column=1, columnspan=2, pady=5)
        self.boutonDecrypter.grid(row=1,column=3, pady=5, sticky=N)
        self.labelStatut.grid(row=5, column=0, columnspan=3, pady=5, padx=10, sticky=W)
        self.labelInformations.grid(row=6, column=0, columnspan=4, pady=5, padx=10, sticky=W)
    
    def retour_menu_principal(self):
        global menu_principal
        menu_principal.affichage()

    def decrypter_texte(self):
        texteClair = self.TextTexteADecrypter.get(1.0, END)
        if (texteClair == ""):
            self.statut.set("Statut: Veuillez renseigner le texte à décrypter!")
        else:
            if texteClair[-1] == "\n":
                texteClair = texteClair[0:-1]
            decalage, texteDecrypte = CasseCesar(texteClair)
            self.TextTexteSortie.delete(1.0, END)
            self.TextTexteSortie.insert(END, texteDecrypte)
            self.statut.set("Statut: Clé trouvée: " + str(abs(decalage)))
        
#Code principal
menu_principal = menu_principal()
menu_chiffrer_texte = menu_chiffrer_texte()
menu_chiffrer_fichier = menu_chiffrer_fichier()
menu_cryptographie_asymetrique = menu_cryptographie_asymetrique()
menu_steganographie = menu_steganographie()
menu_crack_cesar = menu_crack_cesar()
menu_principal.affichage()
mainWindow.mainloop()
