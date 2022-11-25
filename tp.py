# Créé par enzom, le 10/01/2021 en Python 3.7

from tkinter import *
from random import randint

def scores(mon_coup,ton_coup):
    global mon_score, ton_score
    if mon_coup == 1 and ton_coup == 2:
        ton_score = 1 + ton_score

    elif mon_coup == 3 and ton_coup == 1:
        ton_score = 1 + ton_score

    elif mon_coup == 2 and ton_coup == 3:
        ton_score = 1 + ton_score

    elif mon_coup == 2 and ton_coup == 1:
        mon_score = 1 + mon_score

    elif mon_coup == 1 and ton_coup == 3:
        mon_score = 1 + mon_score

    elif mon_coup == 3 and ton_coup == 2:
        mon_score = 1 + mon_score

def jouer(ton_coup):
    global mon_score, ton_score, score1, score2
    mon_coup = randint(1,3)

    if mon_coup==1:
        lab3.configure(image=pierre)
    elif mon_coup==2:
        lab3.configure(image=papier)
    else:
        lab3.configure(image=ciseaux)

    scores(mon_coup,ton_coup)
    score1.configure(text=str(ton_score))
    score2.configure(text=str(mon_score))

def ppierre():
    jouer(1)
    lab1.configure(image=pierre)

def ppapier():
    jouer(2)
    lab1.configure(image=papier)

def pciseaux():
    jouer(3)
    lab1.configure(image=ciseaux)

def reinit():
    global mon_score,ton_score,score1,score2,lab1,lab3
    ton_score = 0
    mon_score = 0

    score1.configure(text=str(ton_score))
    score2.configure(text=str(mon_score))
    lab1.configure(image=blanc)
    lab3.configure(image=blanc)


'''variables gérant le score des opposants'''

ton_score = 0

mon_score = 0

'''initie la fenêtre graphique'''

fenetre = Tk()

fenetre.title("Chifoumi")

'''introduit les images'''

blanc = PhotoImage(file ='blanc.png')

versus = PhotoImage(file ='versus.png',)

pierre = PhotoImage(file ='Pierre.png')

papier = PhotoImage(file ='Papier.png')

ciseaux = PhotoImage(file ='Ciseaux.png')

'''Permet d'organiser/indiquer le texte et les images'''

texte1 = Label(fenetre, text="Joueur", font=("Arial Black", 18))
texte1.grid(row=0,column=0)

texte2 = Label(fenetre, text="Ordinateur", font=("Arial Black", 18))
texte2.grid(row=0,column=2)

texte3 = Label(fenetre, text="Chose your move, you are on the left.")
texte3.grid(row=3, columnspan =3, pady =20,)

score1 = Label(fenetre, text="", font=("Futura", 18))
score1.grid(row=1, column=0)

score2 = Label(fenetre, text="", font=("Futura", 18))
score2.grid(row=1, column=2)

lab1 = Label(fenetre, image=blanc)
lab1.grid(row =2, column =0)

lab2 = Label(fenetre, image=versus)
lab2.grid(row =2, column =1)

lab3 = Label(fenetre, image=blanc)
lab3.grid(row =2, column =2)

'''gère les zones à intéractions'''

bouton1 = Button(fenetre,command=ppierre)
bouton1.configure(image=pierre)
bouton1.grid(row =4, column =0)

bouton2 = Button(fenetre,command=ppapier)
bouton2.configure(image=papier)
bouton2.grid(row =4, column =1,)

bouton3 = Button(fenetre,command=pciseaux)
bouton3.configure(image=ciseaux)
bouton3.grid(row =4, column =2)

bouton4 = Button(fenetre,text='Restart',command=reinit)
bouton4.grid(row =5, column =0, pady =15,)

bouton5 = Button(fenetre,text='Leave',command=fenetre.destroy)
bouton5.grid(row =5, column =2, pady =15,)


fenetre.mainloop()