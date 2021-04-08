from math import*
a=float(input("Entrez le coefficient du terme de degré 2 de votre polynôme")) #je teste les commentaires
b=float(input("Entrez le coefficient du terme de degré 1 de votre polynôme"))
c=float(input("Entrez le coefficient du terme de degré 0 de votre polynôme"))
def delta(a,b,c):   #calcul du discriminant
    delta=b**2-4*a*c
    return delta
if delta(a,b,c)>0:     #calcul des racines
    d=delta(a,b,c)
    x1=(-b-sqrt(d))/(2*a)
    x2=(-b+sqrt(d))/(2*a)
    print("Le polynôme admet deux racines réelles : ",x1,"et",x2)
    if a>0 :
        if x1<x2:
            print("le trinôme est positif sur ]- ∞ ;{}] et [{} ; + ∞ [ et négatif sur [{};{}]".format(x1,x2,x1,x2))
        else:
            print("le trinôme est positif sur ]- ∞ ;{}] et [{} ; + ∞ [ et négatif sur [{};{}]".format(x2,x1,x2,x1))
    elif x1<x2:
        print("le trinôme est négatif sur ]- ∞ ;{}] et [{} ; + ∞ [ et positif sur [{};{}]".format(x1,x2,x1,x2))
    else:
        print("le trinôme est négatif sur ]- ∞ ;{}] et [{} ; + ∞ [ et positif sur [{};{}]".format(x2,x1,x2,x1))
elif delta(a,b,c)==0:
    x=(-b/2*a)
    print("Le polynôme admet une racine double :",x)
    if a>0:
        print("Le polynôme est positif sur R et s'annule en",x)
    else:
        print("Le polynôme est négatif sur R et s'annule en ",x)
else :   
    print("Le polynôme n'admet pas de racine réelle")
    if a>0:
        print("le polynôme est strictement positif sur R")
    else:
        print("Le polynôme est strictement négatif sur R")