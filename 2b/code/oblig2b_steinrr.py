import nltk
from nltk import bigrams
from lm import *

# Oppgave 1:
# opretter LM klasse til aa perpleksitere news og adventure
m = LM()

# Henter news og adventure for videre bruk
news=nltk.corpus.brown.sents(categories='news')
adventure=nltk.corpus.brown.sents(categories='adventure')

# initial parametre
perpNews = 0.0
perpAdventure = 0.0

# beregner perplexitet:
perpNews = m.perplexity(news)
perpAdventure = m.perplexity(adventure)

# printer ut perplexitet.
print("Perpleksitet til news: %.2f" %perpNews)
print("Perpleksitet til adventure: %.2f" %perpAdventure)


""" Oppgave 1 - evaluering av spraakmodeller

$ python oblig2b_steinrr.py
Perpleksitet til news: 72.69
Perpleksitet til adventure: 117.41


Perpleksiteten tiil adventure er hoeyeere fordi klassifikatoren vi benytter i LM er ikke trent paa dette korpuset.
Perpleksiteten til news ville ha veart lavere hvis klassifikatoren vi benytter hadde bare veart trent paa news.
Men dette er ikke bra pga da ville perpleksiteten til adventure veare enda hoyere enn den er naa.

"""

zippy = m.zipfity(news)

for sekvens in zippy:
    print("Ord: %4s  Antall: %4d Sekvens: %.4f  " %(sekvens[0], sekvens[1], sekvens[2]))

""" Oppgave 2 - Zipfianske distribusjon
 
Ord:  the  Antall: 6386 Sekvens: 6386.0000  
Ord:    ,  Antall: 5188 Sekvens: 2594.0000  
Ord:    .  Antall: 4030 Sekvens: 1343.3333  
Ord:   of  Antall: 2861 Sekvens: 715.2500  
Ord:  and  Antall: 2186 Sekvens: 437.2000  
Ord:   to  Antall: 2144 Sekvens: 357.3333  
Ord:    a  Antall: 2130 Sekvens: 304.2857  
Ord:   in  Antall: 2020 Sekvens: 252.5000  
Ord:  for  Antall:  969 Sekvens: 107.6667  
Ord: that  Antall:  829 Sekvens: 82.9000  

"""

brown_tagged_sents = nltk.corpus.brown.tagged_sents(categories='adventure')
adventure = [[w.lower() for w in line] for line in nltk.corpus.brown.sents(categories='adventure')]

#m.regularTagger(adventure)
checkTaggStandardAdv = m.analyseRegularTagger('adventure')
checkTaggStandardFic = m.analyseRegularTagger('fiction')
checkTaggModifiedAdv = m.analyseRegularTagger('adventure', 'modified')
checkTaggModifiedFic = m.analyseRegularTagger('fiction', 'modified')

print("Standard vs modifisert tagging ved hjelp av reguleart uttrykk")
print("Med corpus: 'adventure'")
print(" Standard: %4.2f Modifisert: %4.2f " %(checkTaggStandardFic, checkTaggModifiedAdv))
print("Med corpus: 'fiction'")
print(" Standard: %4.2f Modifisert: %4.2f " %(checkTaggStandardFic, checkTaggModifiedFic))

infile = open("test_setninger.txt")
tekst = []

for line in infile:
    words = line.split(" ")
    tekst.append(words)
infile.close()

# fikser at alle ord har smaa bokstaver:
tekst = [[w.lower() for w in line] for line in tekst]

taggerTekst = m.regularTagger(tekst, 'modified')

for sentence in taggerTekst:
    for taggs in sentence:
        print(taggs)

""" Oppgave 3 - Ordklassetagging med regulære uttrykk
Standard vs modifisert tagging ved hjelp av reguleart uttrykk
Med corpus: 'adventure'
 Standard: 0.18 Modifisert: 0.41 
Med corpus: 'fiction'
 Standard: 0.18 Modifisert: 0.40 
...
..
... skriver ut tagger som blir kopiert inn til test_setninger_m_taggs.txt
..

Kommentarer for ytterligere forbedrelser:
1. said skulle ha veart kattegorisert som verb: VBD
2. he burde veare et pronom
3. had burde veare et verb til have

oppdatere reguleare utrykk:
1 og 3: (r'(.*ed|.*id|had)$', 'VBD')

2. regler for pronoum har jeg ikke lagt inn i det hele tatt saa dette er noe som
kan  tilfoeres
"""
