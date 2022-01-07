
#ex1

def table(base, debut, fin, incrementation):
    result = debut
    while result < fin :
        result = result + incrementation
        if result < fin :
            print(result)
    

base=int(input("quelle table de multiplication voulez vous choisir ?"))
debut=int(input("a quel nombre voulez vous commencer ?"))
incr=int(input("quelle valeur d'incrémentation ?"))
fin=int(input("jusqu'a quelle valeur de fin ?"))


table(base, debut, fin, incr)

#ex2
pi = 3.1416
def cube(val):
    cube = val **3
    return cube
    
def volumeSphere(r):
    return 4*pi*cube(r)/3
    
    
print("le volume de cette sphère est de ",volumeSphere(5))

#€xo3

def tuple(val):
    if val < 0 :
        signe = "négatif"
    else:
        signe ="positif"
    typeval = type(val)
    valabsol = abs(val)
    tupl = (signe, typeval, valabsol)
    return tupl

print(tuple(-150))

#exo4

def tuple(val):
    if val < 0 :
        signe = "négatif"
    else:
        signe ="positif"
    typeval = type(val)
    valabsol = abs(val)
    tupl = (signe, typeval, valabsol)
    return tupl

print(tuple(-150))


#exo5

def somme(test_tup):
    res = sum(list(test_tup))  
    return str(res)

tupl = (7, 8, 9, 1, 10, 7)  
print(somme(tupl))
