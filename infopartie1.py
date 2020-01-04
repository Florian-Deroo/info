###############################################
#Code disponnible sur GitHub:
#https://github.com/Florian-Deroo/info
###############################################

import matplotlib.pyplot as plt
from math import *

#Question 1)
f=open("position.txt","r") #Ouverture du fichier en mode lecture
masse=1 #On suppose la masse = 1kg pour la suite
temps,position,mem=[],[],""
f.readline() #On passe les 2 premières lignes
f.readline()
for i in f: #Lecture de chaque élément de position.txt (chaque ligne)
    for m in i: #Lecture de toutes les lettres d'une ligne
        if (m==" "): #Dès que l'on rencontre un espace c'est qu'on passe à la colone position
            temps.append(float(mem)) #On ajoute la mémoire qui contient tout ce qu'il y a avant l'espace
            mem="" #On réinitialise pour passer à la colone des positions
        else:
            mem=mem+m
    position.append(float(mem)) #On ajoute la mémoire qui contient tout ce qu'il y a après l'espace
    mem=""
f.close()
#Affichage de la courbe
plt.plot(temps,position)
plt.title("Position en fonction du temps")
axes = plt.gca()
axes.set_xlabel('Temps (s)')
axes.set_ylabel('Position (m)')
plt.show()
#On estime la période à 2s environs

#Question 2)a)
amplitude=max(position)

#Question 2)b)
indice=[]
n,memoire=0,0
#Ici on cherche d'abord à trouver les indices où les positions sont maximales
for i in position: #Lecture de chaque élément de la variable position
    if (i==amplitude and memoire!=n-1): #Si la position est au maximum (dans notre cas 2.0) et que le point d'avant n'a pas été enregistré
        memoire=n
        indice.append(n) #On a donc trouvé un indice où la position est maximale
    n=n+1
#Puis on utilise les indices pour trouver les temps où la position est maximale
tempsdesamplitudemax=[]
for i in indice:
    tempsdesamplitudemax.append(temps[i]) #On ajoute chaque temps à une variable
#On calcule des périodes
listeperiode=[]
for i in range (len(tempsdesamplitudemax)-1):
    listeperiode.append(tempsdesamplitudemax[i+1]-tempsdesamplitudemax[i])
#Puis on calcule la moyenne des périodes
sommeperiode=0
for i in range (len(listeperiode)):
    sommeperiode=sommeperiode+listeperiode[i]
periode=sommeperiode/len(listeperiode) #Période trouvée: 1.9875000000000003

pulsation=(2*pi)/periode
k=(pulsation**2)*masse

#Question 2)c)
phaseorigine=acos(position[0]/amplitude)

#Question 3)
positioninitiale=position[0] #Position à t=0
vitesseinitiale=-amplitude*pulsation*sin(phaseorigine) #On dérive l'équation de la position

#Question 4)
fichier = open("vitesse.txt", "w")
fichier.write("% Temps (s), Vitesse (m/s)\n")
vitesse=[]
for i in range (1000):
    vitesse.append(-amplitude*pulsation*sin(phaseorigine+pulsation*i/100)) #On utilise la dérivée de la position
    fichier.write(str(i/100)+" "+str(vitesse[i])+"\n") #Ecriture dans le fichier du temps puis de la vitesse
fichier.close()

#Question 5)
energiecinetique,energiepotentielle,energiemecanique,temps=[],[],[],[]
fenergie= open("energie.txt", "w")
fenergie.write("% Temps (s), Energie cinétique, Energie potentielle\n")
for i in range (1000):
    temps.append(i/100) #Utile pour tracer la courbe à la question 6)
    energiecinetique.append(0.5*masse*(vitesse[i]**2))
    energiepotentielle.append(0.5*k*(position[i])**2)
    energiemecanique.append(energiecinetique[i]+energiepotentielle[i])
    fenergie.write(str(i/100)+" "+str(energiecinetique[i])+" "+str(energiepotentielle[i])+"\n")
fenergie.close()

#Question 6) Affichage des courbes
plt.plot(temps,energiecinetique)
plt.plot(temps,energiepotentielle)
plt.plot(temps,energiemecanique)
plt.show()

