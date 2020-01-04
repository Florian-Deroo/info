####################################
#   Partie 2 DM Informatique
####################################
import random as rd
#Question 7
def create_deck():
    cartes=["A","2","3","4","5","6","7","8","9","10","V","D","R"]
    deck=[]
    for i in range (52):
        if(i<13):
            deck.append(cartes[i]+"p")
        elif(i<26):
            deck.append(cartes[i%13]+"ca")
        elif(i<39):
            deck.append(cartes[i%13]+"co")
        else:
            deck.append(cartes[i%13]+"t")
    return deck
#Question 8
def shuffle():
    L=create_deck()
    for i in range(len(L)):
        n = rd.randrange(0, len(L))
        L[i], L[n] = L[n], L[i]
    return L

#Question 9
print("Avant mélange:",create_deck())
print("Après mélange:",shuffle())

#Question  10
def deal(joueur,cartesparjoueur,listecartes):
    L=listecartes
    cartes=[]
    main=[]
    for i in range (joueur):
        for i in range(cartesparjoueur):
            main.append(L[i])
            L.remove(L[i])
        cartes.append(main)
        main=[]
    return cartes

#Question 11
Liste=shuffle()
print("Mélange: ",Liste)
distribution=deal(5,4,Liste)
print("Distribution 5 cartes à 4 joueurs:",distribution)
cartesrestante=create_deck()
for i in distribution:
    for a in i:
        cartesrestante.remove(a) #On enlève les cartes déjà obtenue par les joueurs
print ("Cartes restantes:",cartesrestante)