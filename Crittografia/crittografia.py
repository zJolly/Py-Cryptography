import os

# Trasposizione
def trasposizione(fraseDaCod, chiaveTrasp):
    lunghezzaChiaveTrasp = len(chiaveTrasp)
    f=open("fileTrasp.txt", "a")
    i=0
    contatoreriga=0
    while(i<len(fraseDaCod)):
        if fraseDaCod[i]==" ":
            i+=1
        else:
            if contatoreriga == lunghezzaChiaveTrasp-1:
                f.write(fraseDaCod[i]+"\n")
                contatoreriga = 0
                i+=1
            else:
                f.write(fraseDaCod[i])
                contatoreriga += 1
                i+=1

    f.close()

    chiaveTrasp.lower()
    stringaTrasp = ""

    j = 0
    while j < len(chiaveTrasp):
        k = 0
        contatorePos = 1
        while k < len(chiaveTrasp):
            if chiaveTrasp[j] > chiaveTrasp[k]:
                contatorePos += 1
            k+=1
        stringaTrasp += str(contatorePos)
        j+=1

    f = open("fileTrasp.txt", "r")

    righe = f.readlines()

    f.close()

    f = open("fileTrasp.txt", "a")
    i = len(righe)
    if len(righe[i-1]) < len(chiaveTrasp):
        j = 0
        while j < (len(chiaveTrasp)-len(righe[i-1])):
            f.write("w")
            j+=1

    f.close()

    f = open("fileTrasp.txt", "r")

    righe = f.readlines()

    f.close()

    stringaDopoTrasp = ""

    l = 0

    while l < len(stringaTrasp):
        m = 0
        while True:
            if str(l+1) == stringaTrasp[m]:
                break
            else:
                m+=1
        for n in righe:
            stringaDopoTrasp += n[m]
        l+=1

    os.remove("fileTrasp.txt")

    return stringaDopoTrasp
# Cesare
def cesare(string, key):
    result=""
    for i in range(len(string)):
        char=string[i]
        if(char.isupper()):
            result+=chr((ord(char)+key-65)%26+65)
        else:
            result+=chr((ord(char)+key-97)%26+97)
    return result
# ASCII
def toascii(string, alfabeto):
    stringaASCII=[]
    i=0
    while(i<len(string)):
        j=0
        while(True):
            if(string[i]==alfabeto[j]):
                break
            else:
                j+=1
        stringaASCII.append(j+1+96)
        i+=1
    return stringaASCII
# BIN
def tobin(string):
    stringbin=[]
    for e in string:
        bins=bin(e)
        a, b=bins.split("b")
        stringbin.append(a+b)
    return stringbin
# XOR
def xor(string, key):
    stringxor=[]
    i=0
    while(i<len(string)):
        rigadascrivere=""
        rigaperXOR=string[i]
        j=0
        while(j<len(key)):
            if(rigaperXOR[j]==key[j]):
                rigadascrivere+="0"
            else:
                rigadascrivere+="1"
            j+=1
        stringxor.append(rigadascrivere)
        i+=1
    return stringxor
# Switch
def switch(string, key):
    stringSwitch=[]
    i = 0
    while i < len(string):
        riga=string[i]
        rigadascrivere=""
        j=0
        while(j<len(key)):
            rigadascrivere+=riga[int(key[j])-1]
            j+=1
        stringSwitch.append(rigadascrivere)
        i+=1
    return stringSwitch
# Shift
def shift(string, side, key):
    stringShift=[]
    if(side=="sx"):
        stringShift=string[int(key):]+string[:int(key)]
    elif(side=="dx"):
        stringShift=string[-int(key):]+string[:-int(key)]
    return stringShift
# Frase da codificare
fraseIniziale=input("Inserisci la frase da codificare: ")
fraseIniziale.lower()
# Key Trasposizione
keyTrasposizione=input("Inserisci la chiave di trasposizione: ")
keyTrasposizione.lower()
# Key Cesare
keyCesare=-1
while(keyCesare<0 or keyCesare>26):
    keyCesare=int(input("Inserisci la chiave di Cesare: "))
# Key XOR
checkXOR=False
while(checkXOR==False):
    keyXOR=input("Inserisci la chiave XOR: ")
    if(len(keyXOR)!=8):
        checkXOR=False
    else:
        checkXOR=True
    i=0
    while(i<len(keyXOR)):
        if(keyXOR[i]!="0" or keyXOR[i]!="1"):
            checkXOR==False
        i+=1
# Key Switch
checkSwitch=False
while(checkSwitch==False):
    keySwitch=input("Inserisci la chiave Switch: ")
    if(len(keySwitch)!=8):
        checkSwitch=False
    else:
        checkSwitch=True
# Key Shift
side=""
intShift=-1
while(side!="sx" and side!="dx"):
    side=input("Inserisci la direzione dello Shift(sx/dx): ")
    side.lower()
while(intShift<0):
    intShift=int(input("Inserisci il numero di quanto vuoi shiftare: "))
# Procedura
alfabeto="abcdefghijklmnopqrstuvwxyz"
stringTrasposizione=trasposizione(fraseIniziale, keyTrasposizione)
stringCesare=cesare(stringTrasposizione, keyCesare)
stringAscii=toascii(stringCesare, alfabeto)
stringBin=tobin(stringAscii)
stringXor=xor(stringBin, keyXOR)
stringSwitch=switch(stringXor, keySwitch)
stringShift=shift(stringSwitch, side, intShift)

print("Codifica finale del messaggio:\n")
print(stringShift)