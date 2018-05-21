#coding: utf-8
from tkinter import *
from EZcipher import *
from Cesar import *
from steganographie import *


#Fenetre de base   
mainWindow = Tk()
mainWindow.geometry("800x450")
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
        self.boutonChiffrerFichier = Button(self.frameContenu, text="Chiffrer un fichier", command=0)
        self.boutonSteganographie = Button(self.frameContenu, text="Stéganographie", command=self.menu_steganographie)

    def affichage(self):
        nettoyer_fenetre()
        global framePage
        self.__init__() #on reinitialise la page
        framePage = self.frameContenu
        self.labelDeplacement.grid(row=0,column=0, padx=10, pady=10)
        self.boutonChiffrerTexte.grid(row=1,column=0, pady=10)
        self.boutonChiffrerFichier.grid(row=2,column=0, pady=10)
        self.boutonSteganographie.grid(row=3,column=0, pady=10)
        print("page principale")
        
    def menu_chiffrer_texte(self):
        global menu_chiffrer_texte
        menu_chiffrer_texte.affichage()
    
    def menu_steganographie(self):
        global menu_steganographie
        menu_steganographie.affichage()
    

class menu_chiffrer_texte:
    def __init__(self):
        #definition des elements de l'interface
        self.frameContenu = Frame(mainWindow, borderwidth=2, relief=GROOVE)
        self.frameContenu.pack(fill='y')
        
        self.boutonRetour = Button(self.frameContenu, text="Retour", command=self.retour_menu_principal)
        self.labelDeplacement = Label(self.frameContenu ,text='Chiffrer du texte')
        self.labelTexteAChiffrer = Label(self.frameContenu, text='Texte à chiffrer')
        self.TextTexteAChiffrer = Text(self.frameContenu, height=5, width=50)
        self.labelCle = Label(self.frameContenu, text='Clé')
        self.EntryCle = Entry(self.frameContenu, width=44)
        self.ListBoxChiffrement = Listbox(self.frameContenu)
        self.labelTexteSortie = Label(self.frameContenu, text='Sortie')
        self.TextTexteSortie = Text(self.frameContenu, height=5, width=50)
        self.boutonChiffrer = Button(self.frameContenu, text="Chiffrer", command=self.chiffrer_texte)
        self.boutonDechiffrer = Button(self.frameContenu, text="Déchiffrer", command=self.dechiffrer_texte)
        
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
        self.ListBoxChiffrement.insert(3, "AES")
        self.labelTexteSortie.grid(row=4,column=0, padx=10, pady=5, sticky=N)
        self.TextTexteSortie.grid(row=4, column=1, columnspan=2, padx=10, pady=5)
        self.TextTexteSortie.insert(END, "Texte chiffré")
        self.boutonChiffrer.grid(row=1,column=3, pady=5, sticky=N)
        self.boutonDechiffrer.grid(row=2,column=3, pady=5, sticky=N)
    
    def retour_menu_principal(self):
        global menu_principal
        menu_principal.affichage()

    def chiffrer_texte(self):
        texteClair = self.TextTexteAChiffrer.get(1.0, END)
        texteClair = texteClair[0:-1]   #le dernier caractère d'un Text est un saut de ligne, on le supprime
        cle = self.EntryCle.get()
        self.TextTexteSortie.delete(1.0, END)
        #texteClair = texteClair.replace('\n', '')
        texteClair = texteClair[0:-1]
        TexteChiffre = cesar(texteClair, int(cle), 3)
        
        self.TextTexteSortie.insert(END, TexteChiffre)
    
    def dechiffrer_texte(self):
        texteClair = self.TextTexteAChiffrer.get(1.0, END)
        #texteClair = texteClair[0:-1]   #le dernier caractère d'un Text est un saut de ligne, on le supprime
        cle = self.EntryCle.get()
        self.TextTexteSortie.delete(1.0, END)
        #texteClair = texteClair.replace('\n', '')
        texteClair = texteClair[0:-1]
        TexteChiffre = cesar(texteClair, -int(cle), 3)
        
        self.TextTexteSortie.insert(END, TexteChiffre)

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
        self.labelInformations = Label(self.frameContenu, text="\n\nInformations: la lecture ou l'écriture des données peut prendre plusieurs plusieurs secondes selon la taille de l'image.\nLes images utilisant la transparence alpha peuvent être altérées par le programme.", justify=LEFT)

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
            self.statut.set("Statut: données lues")
        except ValueError as e:
            self.statut.set("Statut: Erreur (" + str(e) + ")")

        
#Code principal
menu_principal = menu_principal()
menu_chiffrer_texte = menu_chiffrer_texte()
menu_steganographie = menu_steganographie()
menu_principal.affichage()
mainWindow.mainloop()
