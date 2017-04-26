# -*- coding: utf-8 -*-

# Løsningsforslag for Oblig 2a i INF1820
# Natalia Smirnova, basert på Lilja Øvrelid


import nltk

brown_news = nltk.corpus.brown.tagged_words(categories="news")




#########
# Oppgave 1: Ordfrekvens og taggfrekvens
# bruker dictionaries, get for default
# bruker lambda til sortering

word_counts = {}
pos_counts = {}

for w, pos in brown_news:
    word = w.lower()
    word_counts[word] = word_counts.get(word,0) + 1
    pos_counts[pos] = pos_counts.get(pos,0) + 1


sortert_w = sorted(word_counts.items(), key = lambda pair: pair[1], reverse = True)
sortert_p = sorted(pos_counts.items(), key = lambda pair: pair[1], reverse = True)

max_word = sortert_w[0]
max_pos = sortert_p[0]
min_pos = sortert_p[len(sortert_p)-1]

#Hvis det er flere ord med like få tagger:
hapax_tag = [w for w, c in sortert_p if c == min_pos[1]]

print("Det mest frekvente ordet:", max_word)
print("Den mest frekvente ordklassen:", max_pos)
print("Den minst frekvente ordklassen:", min_pos)
print("Antall minst frekvente ordklasser:", len(hapax_tag))


#Det mest frekvente ordet: ('the', 6386)
#Den mest frekvente ordklassen: ('NN', 13162)
#Den minst frekvente ordklassen: ('FW-IN+AT-TL', 1)
#Antall minst frekvente ordklasser: 55



#########
# Oppgave 2a: Finne flertydige ord
# Hvert ord er nøkkel i en dictionary der verdien er en liste av POS-taggene ordet har forekommet med.
# Sjekker om ordklassen fins i listen allerede, så vi unngår duplikater

tags = {}

for w, pos in brown_news:
    word = w.lower()
    
    if word not in tags:
        tags[word] = []
    if pos not in tags[word]:
        tags[word].append(pos) 

ambig = [ w for w, l in tags.items() if len(l) > 1]

print("Antall ord som er flertydige:", len(ambig))

# 2166

########
# Alternativ 2
# Bruker mengder som verdier i dictionaryen.
# Trenger ikke sjekke om en tag er lagt inn fra før.
tags = {}

for w, pos in brown_news:
    word = w.lower()
    if word not in tags:
        tags[word] = set([])
    tags[word].add(pos) 

ambig2 = [ w for w, l in tags.items() if len(l) > 1]

#print "Antall ord som er flertydige:", len(ambig2)




#########
# Oppgave 2b: Det mest flertydige ordet
# Sorterer på *lengden* av pos-listen
# Merk: det er to ord som er like flertydige

# to
ambw, ambposlst = sorted(tags.items(), key = lambda pair: len(pair[1]), reverse = True)[0]
print("Mest flertydige ord:", ambw, ", med", len(ambposlst), "forskjellige tagger", ambposlst)

# house
ambw1, ambposlst1 = sorted(tags.items(), key = lambda pair: len(pair[1]), reverse = True)[1]
print("Mest flertydige ord:", ambw1, ", med", len(ambposlst1), "forskjellige tagger", ambposlst1)



#Oppgave 2c: Hvor ofte hvert ord forekommer med hver av taggene

def freqs(word):
    stats = {}
    for w, pos in brown_news:
        if w.lower() == word.lower():
            if pos not in stats:
                stats[pos] = 1
            else:
                stats[pos]+=1
    return stats



#Oppgave 2c

print("Statistics for house:", freqs(ambw1))
print("Statistics for to:", freqs(ambw))








