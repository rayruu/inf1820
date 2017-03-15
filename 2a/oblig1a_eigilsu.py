# -*- coding: utf-8 -*-

import nltk
from collections import Counter
from operator import itemgetter
import time
start = time.time()

brown = nltk.corpus.brown.tagged_words(categories="news")
#Setter alle ordene til smaa bokstaver
brown = [(x.lower(),y) for x,y in brown]

#Oppgave 1
#Setter opp 2 Dictionaries og lager et med tags og et med ord
words = {}
tags = {}

for (i,j) in brown:
    words[i] = words.get(i, 0) + 1
    tags[j] = tags.get(j, 0) + 1

vanligste_ord = []
vanligste_tag = []
uvanlige_tags = []

#Oppgave 1a
#Bruker Counter og finner det vanligste ordet med most_common. Bruker en 
#while loop for check mot de neste ordene for aa se om de har like hoyt antall 
print("Ordet/ordene som er brukt mest og antall ganger:")
k=0
while Counter(words).most_common()[k][1] == Counter(words).most_common()[0][1]:
    vanligste_ord.append(Counter(words).most_common()[k])
    print("Ord: %s\nAntall: %d" % (Counter(words).most_common()[k][0],Counter(words).most_common()[k][1]))
    k += 1
    
#Oppgave 1b
#Bruker Counter og finner det vanligste taggene med most_common. Bruker en 
#while loop for check mot de neste taggene for aa se om de har like hoyt antall 
print("\nTag/tagene som er brukt mest og antall ganger:")
l=0
while Counter(tags).most_common()[l][1] == Counter(tags).most_common()[0][1]:
    vanligste_tag.append(Counter(tags).most_common()[l])
    print("Tag: %s\nAntall: %d" % (Counter(tags).most_common()[l][0],Counter(tags).most_common()[l][1]))
    l += 1

#Oppgave 1c
#Bruker Counter og finner det minst vanlige taggene med most_common. Bruker en 
#while loop for check mot de neste taggene for aa se om de har like lavt antall 
print("\nTag/tagene som er brukt minst og antall ganger:")
m=1
while Counter(tags).most_common()[-m][1] == Counter(tags).most_common()[-1][1]:
    uvanlige_tags.append(Counter(tags).most_common()[-m])
    print("Tag: %s \nAntall: %d" % (Counter(tags).most_common()[-m][0],Counter(tags).most_common()[-m][1]))
    m += 1
    
#Oppgave 2a
sett = set()
word = []
word_tag = []
antall_ord = 0

#Bruker et sett for aa faa ut alle de unike variantene av hvert ord.
#Lager en liste med kun ordene og en med ord + tags
for n in brown:
    if(n not in sett):
        word.append(n[0])
        sett.add(n)
        word_tag.append(n)

#Bruker Counter og en for - loop for aa finne antall ord med mer enn en tag
teller = Counter(word)

for o in teller.values():
    if(o > 1):
        antall_ord += 1
print("\nAntall ord med flere enn 1 tag er: %d" % antall_ord)

#Oppgave 2b
#Bruker en while loop for aa finne ordene med flest tags. Bruker saa en 
#dobbel for-loop for aa finne taggene til ordene
print("\nOrdet/ordene med flest tags og taggene:")
flest_tags = []
p = 0
while Counter(word).most_common()[p][1] == Counter(word).most_common()[0][1]:
    flest_tags.append(Counter(word).most_common()[p][0])
    p += 1

q=0
tag_rekke = []
for r in flest_tags:
    row = []
    for s in word_tag:
        if(s[0] == flest_tags[q]):
            row.append(s[1])
    tag_rekke.append(row)
    q += 1

for t in range(len(flest_tags)):
    print("Ord: %s\nTags: %s\n" % (flest_tags[t],tag_rekke[t][:]))


#Oppgave 2c
#Lager en funksjon freqs som finner frekvensen de forskjellige tagsene forekommer.
#Sorterer paa antall, saa ordet kommer forst, saa tags fordelt.
def freqs(w):
    freq = {}
    
    for (u,v) in brown:
        if(u == w):
            freq[u] = freq.get(u, 0) + 1
            freq[v] = freq.get(v,0) + 1
                
    return sorted(freq.items(), key=itemgetter(1), reverse=True)
    

#Oppgave 2d
#Bruker funksjonen freqs paa aa skrive ut ordene med flest tags og fordeling av antall
print ("\nFordelingen av taggene i ord med flest tags var slik:")

for x in flest_tags:
    temp = freqs(x)
    print ("Ord: %s\nTags: %s\n" % (temp[0], temp[1:]))
end = time.time()
print("runtime %f" %(end-start))
"""    
Ordene med flest tags er House og To. Begge ordene har 2 hovedgrupper de har mange
treff på:
"house" har NN-TL og NN. NN-TL er Substantiv men et spesifikt hus, skrevet med 
stor bokstav, NN er substantiv.
"to" har TO og IN. TO er infinitival to (to t') og IN er preposisjon.

Resten av taggene har faa treff og er stort sett spesialiseringer av de to 
hovedtaggene.

Kommentarer om oppgaven: 
Jeg vet jeg burde unngaa while looper, men fant ingen bedre maate aa finne
alle ordene naar det var flere enn 1 resultat. De er laget saan at de alltid 
vil finne et svar, saa lenge teksten er skrevet paa samme maate som brown corpus.
Det fungerer f.eks. bra om man legger inn tags='universal' under innhentingen
faar man resultater men med forenklede tags.
"""
