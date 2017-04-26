# encoding: utf-8
import re

###########
# Oppgave 1


#1a)
# Fra oblig1a

f = open("dev.txt")


num_lines = 0
num_words = 0

for line in f:
    num_lines = num_lines + 1
    for w in line.split():
        num_words = num_words + 1
        print(w)
f.close()

#1b)

#Feil i første versjon: 
#Tegnsetting og anførselstegn skilles ikke ut, feks:
#avstår,
#bevisst,
#«sette
#dette:
#dyr?


###########
#Oppgave 2

num_lines = 0
num_words = 0

for line in f:
    num_lines = num_lines + 1
    for token in re.findall("([,;:.!?\"]|[A-ZÆØÅa-zæøå-]+)", line):
        num_words = num_words + 1
        print(token)

f.close()


#Gjenstående feil:
#ord som inneholder tall, f.eks. 1960-tallet 
#initialer i navn, f.eks. "D.", skal ikke splittes
#ordinaltall, f.eks. "11.", skal ikke splittes
