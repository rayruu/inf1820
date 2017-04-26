# -*- coding: utf-8 -*-

#Løsningsforslag for Oblig 2a i INF1820
# Lilja Øvrelid


import nltk
import sys
from nltk.corpus import brown

#########
# Oppgave 1:

#conditional frequency distribution
#tar inn en liste av par, der første elementet blir betingelsen.

#en dictionary der hver tagg er en nøkkel og hver verdi er en dictionary på formen {ord:frekvens}. Feks {NN:{bil:2,tre:3,gutt:4,..}, VB:{skyte:1,løpe:3,..}}


# # #######
# # # emission probabilities:
# # # P(w_i | t_i)


brown_ord_tagger = brown.tagged_words()
brown_tagger_ord = [ (tag, word) for (word, tag) in brown_ord_tagger ]


# # frekvensdistribusjon
cfd_tagger_ord = nltk.ConditionalFreqDist(brown_tagger_ord)

max_nn = cfd_tagger_ord['NN'].most_common()[0]
f_nn = cfd_tagger_ord['NN']['linguist']
max_jj = cfd_tagger_ord['JJ'].most_common()[0]

print("Oppgave 1:")
print("1.2 (a) Mest frekvente substantivet:", max_nn)
print("1.2 (b) Antall forekomster av 'linguist':", f_nn)
print("1.2 (c) Mest frekvente adjektivet:", max_jj)

    
# # sannsynlighetsdistribusjon
cpd_tagger_ord = nltk.ConditionalProbDist(cfd_tagger_ord, nltk.MLEProbDist)
#print("Mest sannsynlige adjektivet:", cpd_tagger_ord['JJ'].max())
#print("Sannsynligheten for new gitt JJ:", cpd_tagger_ord['JJ'].prob("new"))


# # ########
# # # transition probabilities:
# # # P(t_i | t_{i-1})

# # bigram over tagger
brown_tagger = [tag for (word, tag) in brown_ord_tagger]
brown_tagg_par = nltk.bigrams(brown_tagger)


# # frekvensdistribusjon over bigrammene
cfd_tagger= nltk.ConditionalFreqDist(brown_tagg_par)
print(cfd_tagger['NN'])

#print(cfd_tagger.conditions())
max_etter_nn = cfd_tagger['NN'].most_common()[0]
f_dtnn = cfd_tagger['DT']['NN']

print("1.5 (a) Taggen som oftest etterfolger NN er:", max_etter_nn)
print("1.5 (b) Antall forekomster av bigrammet 'DT NN' er:", f_dtnn)

# # sannsynlighetsdistribusjon over taggbigram
cpd_tagger = nltk.ConditionalProbDist(cfd_tagger, nltk.MLEProbDist)

print("1.6 Sannsynligheten for NN gitt DT er:", cpd_tagger["DT"].prob("NN"))


# # ############
# # Oppgave 2

# # # #emission probabilities
w1a = cpd_tagger_ord['PP$'].prob("her")
w2a = cpd_tagger_ord['NN'].prob("duck")

print("Oppgave 2:")
print("P(her|PP$):", w1a)
print("P(duck|NN):", w2a)

w1b = cpd_tagger_ord['PPO'].prob("her")
w2b = cpd_tagger_ord['VB'].prob("duck")

print("P(her|PPO):", w1b)
print("P(duck|VB):", w2b)


# # # #transition probabilities
t1a = cpd_tagger["VBD"].prob("PP$")
t2a = cpd_tagger["PP$"].prob("NN")

print("P(PP$|VBD):", t1a)
print("P(NN|PP$):", t2a)

t1b = cpd_tagger["VBD"].prob("PPO")
t2b = cpd_tagger["PPO"].prob("VB")

print("P(PPO|VBD):", t1b)
print("P(VB|PPO):", t2b)

a = w1a * w2a * t1a * t2a
b = w1b * w2b * t1b * t2b

print("a: ", a)
print("b: ", b)

# # tolkning b er mer sannsynlig



#########
# Oppgave 3

#the/her/jane's smartest/dancing monkey


# grammar = r"""
#   NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and nouns
#       {<NNP>+}                # chunk sequences of proper nouns
# """


grammar = r"""
NP: {<DT>?<POS>?<CD>?<PRP$>?<JJ[RS]*>*<VBG>*<RB[R]*><NN>}
    {<DT>?<POS>?<CD>?<PRP$>?<JJ[RS]*>*<VBG>*<NN[PS]*><CC><DT>?<POS>?<CD>?<PRP$>?<JJ[RS]*>*<VBG>*<NN[PS]*>+} #coordination
    {<DT>?<POS>?<CD>?<JJ[RS]*>*<VBG>*<NN[PS]*>+} #compounds
    {<PRP>} #pronoun
    {<WDT>} #that
    {<EX>} #it/there expletive
"""

cp = nltk.RegexpParser(grammar)

from nltk.corpus import conll2000
training_chunks = conll2000.chunked_sents("train.txt", chunk_types=["NP"])
test_chunks = conll2000.chunked_sents("test.txt", chunk_types=["NP"])

print(training_chunks)

print("Oppgave 3:")
print("Evaluering på treningskorpuset:")
print(cp.evaluate(training_chunks))

print("Evaluering på testkorpuset:")
print(cp.evaluate(test_chunks))

# Oppgave 3:
# Evaluering på treningskorpuset:
# ChunkParse score:
#     IOB Accuracy:  87.0%%
#     Precision:     80.6%%
#     Recall:        74.5%%
#     F-Measure:     77.4%%
# Evaluering på testkorpuset:
# ChunkParse score:
#     IOB Accuracy:  86.9%%
#     Precision:     80.0%%
#     Recall:        73.9%%
#     F-Measure:     76.8%%




