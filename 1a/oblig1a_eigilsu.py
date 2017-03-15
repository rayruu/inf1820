# encoding: utf-8

#Oppgave 1: Strenger i Python

#Del a: Leser inn filen i filinnhold og stenger den
f = open("dev.txt") #Har tekstfilen i samme mappe som programfilen
filinnhold = f.read()
f.close()

#Del b: Teller og skriver ut forekomstene av "er"
print('Oppgave 1: \nTeller forekomstene av "er"\nAntall ganger: %d' % filinnhold.count("er"))

#Teller ordene som har "er" som endelse
textsplit = filinnhold.split() #Deler teksten opp i individuelle strenger

i=0
count = 0

while i < len(textsplit): #Sjekker alle strengene og teller når endswith er sann
    if textsplit[i].endswith("er") == True:
        count += 1
    i += 1

print ('Teller ord som slutter på "er"\nAntall ord: %d\n' %count)

#Del c: Lage en ny liste med de to siste bokstavene fra hvert ord
j=0
endlist = []
while j < len(textsplit):
    if textsplit[j][-1].isalpha() != True: #Sjekker om siste tegn i ordet er en bokstav
        endlist.append(textsplit[j][-3:-1])
    else:
        endlist.append(textsplit[j][-2:]) #Plukker ut de to siste bokstavene i hvert ord
    j += 1
    
#Sett sammen listen med endelsenr til en liste med mellomrom  
endstring = " ".join(endlist)

#Oppgave 2: Tokenisering

f = open("dev.txt") #Henter inn fila
linjer = []
words = 0
antall_linjer = 0
tomme_linjer = 0

for line in f: #Går gjennom linje for linje
    linjer = line.split() #Deler opp linjene i ord og legger dem i liste
    for i in linjer: #Deler opp ordene i hver linje
        words += 1  #Teller ordene
    if line.isspace() == True:
        tomme_linjer +=1 #Teller tomme linjer
    else:
        antall_linjer += 1 #Teller Linjene
f.close()
print ('Oppgave 2: \nTelling av antall ord og linjer i fila\nAntall linjer med tekst: %d\
    \nAntall tomme linjer: %d\nAntall ord: %d' % (antall_linjer, tomme_linjer, words))
    
"""
runfile('D:/Skole/INF1820/Oblig1a/oblig1a_eigilsu.py', wdir='D:/Skole/INF1820/Oblig1a')
Oppgave 1: 
Teller forekomstene av "er"
Antall ganger: 5093
Teller ord som slutter på "er"
Antall ord: 2625

Oppgave 2: 
Telling av antall ord og linjer i fila
Antall linjer med tekst: 972    
Antall tomme linjer: 340
Antall ord: 32243
"""
