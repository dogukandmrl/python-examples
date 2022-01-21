import math
def topla(x,y):
    return x+y
def cikart(x,y):
    return x-y
def bolme(x,y):
    return x/y;
def carpma(x,y):
    return x*y
def usAlma():
    x = int(input("x:"))
    y = int(input("y:"))
    print(pow(x,y))
def logaritma():
    x = int(input("x:"))
    y = int(input("y:"))
    print(math.log(x,y))
def karekok():
    x = float(input("x:"))
    print(math.sqrt(x))
def sinus():
    x= float(input("x:"))
    print(math.sin(x))
def cikisi():
    return 0
print("Yapmak istediginiz islemi giriniz: ")
print("1= TOPLAMA ,2= CIKARTMA, 3= CARPMA, 4=BOLME, 5=US ALMA, 6=LOGARITMA, 7=KAREKOK, 8=SIN,9=CİKİS")
deger = int(input("Islem no:"))
if(deger==1 or deger==2 or deger==3 or deger ==4):
    x=int(input("x:"))
    y=int(input("y:"))
    if (deger==1):
        print(str("toplama:")+str(topla(x,y)))
    if(deger==2):
        print(str("Cikartma:")+str(cikart(x,y)))
    if (deger==3):
        print(str("Carpma:")+str(carpma(x,y)))
    if (deger ==4):
        print(str("Bolme:") + str(bolme(x, y)))
if (deger==5):
    usAlma()
if (deger==6):
    logaritma()
if (deger==7):
    karekok()
if (deger==8):
    sinus()
if (deger== 9):
    cikisi()
