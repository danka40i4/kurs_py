import sys 
import math

#print ("hej ho");

# 210921
# typy danych, laczenieStringow, input, rzuty, listy
#print ('hej',3) #ze spacja

number = 8;
#print(type(number));
number = 8.5
#print(type(number));
name = "hejho"
name='hejho'
name='''kk
ff
gg
gfsd'''

number="hrjho"
#print(type(number))

number = True
n = None # js null, undefined
#print(type(n))

# aktualnie python3
# ew python3 main.py

name = "hejho"
number = 8
message = f"imie {name}" #fstring - format string
message = f"wiek {name} to {number}"
message = "Wiek {} to {}".format(name,number) #dla pythona2
message = "Wiek %s to %s"%(name,number) #dla py2 i 3, ale moze nie potem

# mapowanie
n=2 #int
#int(nn)
nn=str(n) #na string
nn="yo"
# nnn=int(nn) #value error
#print(type(n),type(nn),type(nnn))

#nn=4
'''
try:
     nnn=float(nn) #bedzie nope bo konwersja i bo wciecia
except:
    print("nope")
'''

# tab=4 spacje
# indentation err - wciecia

#print(bool())
#print ("imie")
#imie = input("imie: ")

'''
imie = input("imie: ")
wiek = input("wiek: ")
print(type(imie),type(wiek),imie,wiek)
'''
'''
# python main.py franek 5
print(sys.argv) # lista
print(sys.argv[2])
'''

lista = ["hej",3,None,True,"ho"]

# for x in lista:
    # print(type(x))
# index err - poza obszar

lista = ["hej",3,None,True,"ho","hh","kk","jj","ho"]
# lista[-1]
# print(lista[1:3])
# print(lista[1:]) 
#print(lista[1:6:2]) # od 1 do 4 co 2

'''
name="hejhohopsiup"
print(name[2:-1:2]) 
print(name[::-1]) # odwraca
print(name[::-2]) # piphhe
print(name[::-4]) # pph
'''
'''
# BLAD
name[3]="x"
print(name)
'''

lista.append("x") #dodaje na koniec
lista.insert(1,"c") #dodaje z indeksem 1
lista.remove("ho") #usuwa podaną w nawiasie wartosc, pierwsza z brzegu

temp = lista.remove("ho")
# print(temp) # ->none

'''
lista.pop(4) # usuwa indeks, przechowuje/zwraca
print(lista)
temp = lista.pop(4) 
print(lista)
print(temp)
'''

del lista[3] # usuwa indeks, nie przechowuje

lista=[]
# print(bool(lista)) # false
x=len(lista)



####
# msc zerowe funkcji z input

#funkcja = input("Podaj funkcję: ")
# ax2 + bx + c

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
delta = -b + 4*a*c
print(delta)
if delta>0:
    x1 = (-b-math.sqrt(delta))/2*a
    x2 = (-b+math.sqrt(delta))/2*a
    ans=str(x1)+", "+str(x2)
elif delta==0:
    x = (b-math.sqrt(delta))/2*a
    ans=x
else:
    ans="delta<0"

print("ans ",ans)



