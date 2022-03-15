from tkinter import *
from tkinter import ttk
from functools import *
from pathlib import Path
import random


#Variable global de la grille :

c = 50 #Longueur du mot len(solution)*10
n = 6 #Nombre de tentative de ligne
cases = []    # Liste contenant les objets cases
fichier = Path(__file__).parent / "dico.txt"

dico = []

with open(fichier, "r", encoding="utf8") as f:
    for ligne in f.readlines():
            dico = ligne.lower().split()
print(dico)
    
# myfile = open(fichier, "r")
# for ligne in myfile.readlines():
#     dico = ligne.lower().split()
# myfile.close()

solution = random.choice(dico)
print(solution)
resultat = ["","","","","",""]
center_x = 25
center_y = 25
essai = 0
offset_point = [0,0,1] #décalage_x, décalage_y,pôsition de la ligne


def recupProposition(decalage_case):
    decalage_case[0] = 0
    choix_utilisateur = entree.get() #get la valeur du bouton entree
    print("avant",resultat)

    if len(choix_utilisateur) == 6:      
        
        for colonne in range(n):   # Conception des cases d'une ligne
            
            if choix_utilisateur[colonne] == solution[colonne]:
        
                resultat[colonne] = choix_utilisateur[colonne]
                
            cnv.create_text(center_x+decalage_case[0],center_y+decalage_case[1]+50, text=resultat[colonne],font="bold 20",tag=f"case_{colonne}_{decalage_case[2]+1}") #afficher les bons lettres trouvées
            print(f"Tag des bonnes lettres : case_{colonne}_{decalage_case[2]+1}")
            cnv.create_text(center_x+decalage_case[0],center_y+decalage_case[1], text=choix_utilisateur[colonne],font="bold 20",tag=f"case_{colonne}_{decalage_case[2]}") #afficher l'entrée utilisateur
            
            print(f"Tag des lettres user : case_{colonne}_{decalage_case[2]}")
            
            # if resultat[colonne] != solution[colonne]:
            #     cnv.delete(f"case_0_3")
                
            decalage_case[0] += 50 #décalage x (vers la droite)
        decalage_case[1] += 50 #décalage y (vers le bas)
    else:
        erreur = Label(cadre,text = "Entrer un mot à 6 lettres ou présent dans notre dicotionnaire")
        erreur.pack()
    
    if choix_utilisateur == solution :
        print("T'as gagné enfoiré")
        gagne = Label(cadre,text="T'as gagné enfoiré")
        gagne.pack()
        btn_saisie["state"] = DISABLED
        btn_saisie["text"] = "Recommencer ?"
    print("apres",resultat)
    
    decalage_case[2] += 1
    

jeu = Tk()

jeu.title("Motus")

title = Frame(jeu)
title.pack(padx =5, pady=5)

#titre du jeu
title_lable = Label(title,text="Bienvenue à vous hardcore g@merz dans le jeu de survie le plus hardu de 2032 💻🖱️")
title_lable.pack()

#cadre de l'entrée utilisateur
cadre = Frame(jeu)
cadre.pack()

etiquette = Label(cadre, text='👉 Devinez le mot mystère :')
etiquette.pack()

entree = Entry(cadre, width=50)
entree.pack()
entree.focus_force()

btn_saisie = Button(cadre, text="Valider", command=partial(recupProposition, offset_point)) # command=jeu.destroy faire fonction bouton
btn_saisie["fg"] = "red"
btn_saisie.pack()

grille = Frame(jeu)
grille.pack()
cnv=Canvas(cadre, bg="ivory",width=300, height=300,highlightbackground="black") #highlightthickness=10 

for ligne in range(n):
    
    transit=[] # Les cases de chaque ligne seront stockées dans "transit"
    for colonne in range(n):    # Conception des cases d'une ligne
        transit.append(cnv.create_rectangle(colonne*c+2, ligne*c+2, (colonne+1)*c+2, (ligne+1)*c+2))
    cases.append(transit) # Ajout de la ligne à la liste principale

cnv.pack(padx=10,pady=10)


def changer_couleur(event):
    print("click !")
    color=cnv.itemconfigure("mobile", "fill")[-1]
    if color=="red":
        color="blue" 
    else:
        color="red"
    cnv.itemconfigure("mobile", fill=color)

cnv.tag_bind("mobile", "<Button-1>", changer_couleur)

btnAffiche = Button(jeu, text='Quitter', command=jeu.destroy)
btnAffiche["fg"] = "red"
btnAffiche.pack()

jeu.mainloop() 

# def afficheZoneSaisie():
#     global entree
#     zoneSaisie = entree.get()
#     print('Votre mot de passe secret est : '+zoneSaisie)
#     # return inutile : modification d'une variable globale