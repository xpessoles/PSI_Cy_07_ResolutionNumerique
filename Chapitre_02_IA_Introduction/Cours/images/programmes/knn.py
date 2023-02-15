# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 14:37:22 2021

@author: xpess
"""
import math as m
def distance(x1:list, x2:list) -> float :
    distance = 0.
    for i in range(len(x1)):
        distance += (x1[i]-x2[i])**2
    return m.sqrt(distance)

def get_voisins(data_train:list, data_test :list, k:int) -> list :
    distances =[]
    for ligne in data_train : 
        d = distance(ligne,data_test)
        distances.append([ligne,d])
    # Tri de la liste suivant la seconde colonne (distances)
    distances.sort(key=lambda t : t[1]) 
    voisins = []
    for i in range(k) :
        voisins.append(distances[i][0])
    return voisins

def prediction(data_train:list, data_test, k:int) -> list :
    voisins = get_voisins(data_train, data_test, k)
    sorties = [ligne[-1] for ligne in voisins]
    predict = max(set(sorties), key=sorties.count)
    return predict

# import random as rd
# dt = [[rd.randrange(-10,10),rd.randrange(-10,10),rd.randrange(-1,1)] for i in range(10)]
train = [[-3, -6, 0],
 [-8, -8, -1],
 [4, 5, -1],
 [5, -6, -1],
 [0, 5, 0],
 [-3, -10, 0],
 [-3, -6, -1],
 [-4, -5, -1],
 [2, -10, -1],
 [9, 6, 0]]

test = [-4, 2, -1]
p = prediction(train,test,2)
print(p)

p = prediction(train,[2, -10, -1],2)
print(p)



