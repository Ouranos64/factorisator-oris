from math import*
from cmath import*
L=[]
for i in range (4):
    print("Vous allez pouvoir entrez le coefficient de degré",3-i,"de votre ponynôme")
    h=float(input("Quel est ce coefficient ?")) 
    L=L+[h]               #Choix des coeffcients dun polynôme
L.reverse()   #inversion des éléments de la liste pour que le rang corresponde au degré du monome
r=float(input("Quelle est la racine évidente de votre polynôme ?"))
a=L[3] 
if r==0:
    c=L[1]
else:
    c=-L[0]/r   
b=L[2]+a*r        #calcul des coefficients du polynôme de degré 2
d=b**2-4*a*c
def racine(a,b,c):
    if d>0:
        x1=(-b-sqrt(d))/(2*a)
        x2=(-b+sqrt(d))/(2*a)          #calcul des racines dans le cas delta positif
        return [x1.real,x2.real]
    elif d==0:         #calcul des racines dans le cas delta nul
        x=(-b/(2*a))
        return [x.real]
    else:                    #calcul des racines dans le cas delta négatif 
        z1=(-b-(0+1j)*sqrt(-d))/(2*a)
        z2=(-b+(0+1j)*sqrt(-d))/(2*a)  
        return [z1,z2]
Q=racine(a,b,c)  
if len(Q)==2:
    print("Une factorisation du polynôme est [z-({})][z-({})][z-({})]".format(r,Q[0],Q[1]))       #Écriture de la forme factorisée 
else:
    print("Une factorisation du polynôme est[z-({})][z-({})]^2".format(r,x))