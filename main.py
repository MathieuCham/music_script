# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 21:01:49 2023

@author: mchamaillard
"""

import numpy as np

fichier = open("tempo_devine.txt", "r")
contenu = fichier.read()
fichier.close()
t=np.array([float(l) for l in contenu.split('\n')])

dt=np.diff(t)

import matplotlib.pyplot as plt

tempo_recherche=range(90,160)

erreurL2=np.zeros(len(tempo_recherche))

for ii in range(len(tempo_recherche)):

    tempo=tempo_recherche[ii]

    T=4*60/(tempo)

    pp=-np.floor(np.log(dt/T))


    erreur_1=abs(T*(2**-pp) -dt)
    erreur_2=abs(T*(2**(1+pp)) -dt)

    erreur=np.min([erreur_1,erreur_2],axis=0)

    erreurL2[ii]=np.sqrt(np.mean(erreur**2))
    
    
    
    
plt.plot(tempo_recherche,erreurL2)    