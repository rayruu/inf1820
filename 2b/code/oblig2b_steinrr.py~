import nltk
from nltk import bigrams
from lm import *



# Oppgave 1:
# opretter LM klasse til aa perpleksitere news og adventure
m = LM()

# Henter news og adventure for videre bruk
news=nltk.corpus.brown.sents(categories='news')
adventure=nltk.corpus.brown.sents(categories='adventure')

"""
# initial parametre
perpNews = 0.0
perpAdventure = 0.0

# beregner perplexitet:
perpNews = m.perplexity(news)
perpAdventure = m.perplexity(adventure)

# printer ut perplexitet.
print("Perpleksitet til news: %.2f" %perpNews)
print("Perpleksitet til adventure: %.2f" %perpAdventure)
"""

""" Oppgave 1 - evaluering av spraakmodeller

$ python oblig2b_steinrr.py
Perpleksitet til news: 55.01
Perpleksitet til adventure: 82.51

Perpleksiteten tiil adventure er hoeyeere fordi klassifikatoren vi benytter i LM er ikke trent paa dette korpuset.
Perpleksiteten til news ville ha veart lavere hvis klassifikatoren vi benytter hadde bare veart trent paa news.
Men dette er ikke bra pga da ville perpleksiteten til adventure veare enda hoyere enn den er naa.

"""
"""
zippy = m.zipfity(news)

for sekvens in zippy:
    print("Ord: %4s  Antall: %4d Sekvens: %.4f  " %(sekvens[0], sekvens[1], sekvens[2]))
"""
""" Oppgave 2 - Zipfianske distribusjon 

Ord:  the  Antall: 6386 Sekvens: 0.0635  
Ord:    ,  Antall: 5188 Sekvens: 0.0516  
Ord:    .  Antall: 4030 Sekvens: 0.0401  
Ord:   of  Antall: 2861 Sekvens: 0.0285  
Ord:  and  Antall: 2186 Sekvens: 0.0217  
Ord:   to  Antall: 2144 Sekvens: 0.0213  
Ord:    a  Antall: 2130 Sekvens: 0.0212  
Ord:   in  Antall: 2020 Sekvens: 0.0201  
Ord:  for  Antall:  969 Sekvens: 0.0096  
Ord: that  Antall:  829 Sekvens: 0.0082

"""

brown_tagged_sents = nltk.corpus.brown.tagged_sents(categories='adventure')
adventure = [[w.lower() for w in line] for line in nltk.corpus.brown.sents(categories='adventure')]

m.regularTagger(adventure)
checkTagg = m.analyseRegularTagger('adventure')
print("Hvor riktig regulear utrykk er: %.3f " %checkTagg)
