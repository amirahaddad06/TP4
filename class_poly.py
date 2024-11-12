# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:17:58 2024

@author: AHADDAD AMIR
"""

class polynome : 
    def __init__(self,coeff):
        self.coefficient=coeff
        
    def afficher(self):
        N=len(self.coefficient)
       
        for i in range (N-1,-1,-1):
            if (i!=0):
                print(self.coefficient[i],'* X ^',i,'+',end=' ')
            else: 
                print(self.coefficient[i],end=' ')
    def get_valeur(self,x):
        N=len(self.coefficient)
        polynome=0 
        for i in range(N):
            polynome=polynome+self.coefficient[i]*x**i
        return polynome 
    
coefficients = [1.2, -0.1, -1.3, 0.1, 0.1]
p = polynome(coefficients)

# Afficher le polynôme
print("Polynôme p(x) :")
p.afficher()
print("\n")

# Calculer la valeur du polynôme pour différentes valeurs de x
for x in [-2, -1, 0, 1, 2]:
    valeur = p.get_valeur(x)
    print(f"p({x}) = {valeur}")  