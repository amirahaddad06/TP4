# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:45:40 2024

@author: AHADDAD AMIR
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:57:36 2024

@author: AHADDAD AMIR  
 Tp 02 : Tableaux et Fonctions 
"""
#-------------------------------------------------------------------------------------------------------------------
       #---------------------------------------------Exercice 01--------------------------------------------------- 

def afficher (p): # la variable p est une liste 
      N=len(p)
     
      for i in range (N-1,-1,-1):
          if (i!=0):
              print(p[i],'* X ^',i,'+',end=' ')
          else: 
              print(p[i],end=' ')
        
        
def get_valeur(p, x): 
    N=len(p)
    polynome=0 
    for i in range(N):
        polynome=polynome+p[i]*x**i
    return polynome 


def deriver(p):
    dérivé=[]
    N=len(p)
    for i in range (1,N):
        dérivé.append(p[i]*i)
    return dérivé


 # programme principal qui test les 3 fonction 
 
polynome =[2,2,6,2]
x=2
afficher(polynome)
Poly_en_x=get_valeur(polynome, x)
print(' ')
print(Poly_en_x)
poly_derive=deriver(polynome)
print('')
print(poly_derive)