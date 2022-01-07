#Expression usuelles

##Exo2
print("Exo2\n")
pos=input('Entrer un flottant positif: ')
pos=float(pos)
if pos >= 0 :
    print("%.2f" %pos)
else:
    print("Le nombre n'est pas positif")


##Exo3
print("Exo3\nA:")
a,b=0,10
while a<b:
    print(a, end=" ")
    a+=1
print("\nB :")
while b>0:
    b -= 1
    if b%2 != 0:
        print(b, end=" ")

##Exo4
print("\nExo4\nA:")
n = 0
while not(1 <= n <= 10):
    n = int(input("Entrez un entier entre 1 et 10 : "))
print("\nValeur saisie :", n)

 
##Exo5
print("\nExo5\n")
for i in range(0,15,3):
    print(i, end=" ")
print("\n")
liste=[print(i, end=" ") for i in range(0,15,3)]

##Exo6
print("\nExo6\n")
str1,str2="abc","de"
liste=[i+j for i in str1 for j in str2]
print(liste)

##Exo7
print("\nExo7\n")
for i in range(1,10+1):
    if i == 5:
        continue
    else:
        print(i, end=' ')

