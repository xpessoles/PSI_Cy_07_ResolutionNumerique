import numpy as np
import matplotlib.pyplot as plt
import random as rd

def perceptron(X,W,b,f):
    """
    Calcul de la sortie d'un neurone, en propagation avant. 
    Entrées : 
     * X(lst) : liste des entrées 
     * W(list) : liste des poids (même taille que les entrées)
     * b(float) : valeur du biais
     * f (function) : fonction d'activation
    """
    z = 0
    for i in range(len(X)):
        z = z+X[i]*W[i]
    z=z+b
    return f(z)
    

def ReLU(x):
    if x<0 : return 0
    else : return x
    

def influence_poids():
    w= np.linspace(-1,1,5)
    
    for i in range(len(w)):
        les_x = np.linspace(-10,10,200)
        les_y = [ReLU(w[i]*x) for x in les_x]
        plt.plot(les_x,les_y,label='w = '+str(w[i]))

    plt.grid()
    plt.legend()
    plt.savefig('poids.pdf')
    plt.show()


def influence_biais():
    b= np.linspace(-3,3,5)
    for i in range(len(b)):
        les_x = np.linspace(-5,5,200)
        les_y = [ReLU(x+b[i]) for x in les_x]
        plt.plot(les_x,les_y,label='b = '+str(b[i]))
    
    plt.grid()
    plt.legend()
    plt.savefig('biais.pdf')
    plt.show()
