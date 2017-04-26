import nltk

class HMM:
    def __init__(self,tekst):
        self.tekst = tekst
        
    def freqDist(self, ord_inn=None, tag_inn=None):
        if(ord_inn == None and tag_inn == None):
            dist1 = nltk.ConditionalFreqDist((tag,word) for (word,tag) in self.tekst)
            return dist1
        elif ((ord_inn != None and tag_inn == None)):
            dist2 = nltk.ConditionalFreqDist((tag,word) for (word,tag) in self.tekst 
                                             if word == ord_inn)
            return dist2
        elif (ord_inn == None and tag_inn != None):
            dist3 = nltk.ConditionalFreqDist((tag,word) for (word,tag) in self.tekst 
                                           if tag.startswith(tag_inn))
            return dist3
        elif (ord_inn != None and tag_inn != None):
            dist4 = nltk.ConditionalFreqDist((tag,word) for (word,tag) in self.tekst 
                                           if tag.startswith(tag_inn) and word == ord_inn)
            return dist4
        
    def freqDist_tags(self, tag1_inn=None, tag2_inn=None):
        if (tag1_inn != None and tag2_inn == None):
            dist1 = nltk.ConditionalFreqDist((tag1,tag2) for (tag1,tag2) in self.tekst 
                                    if tag1 == tag1_inn)
            return dist1
        
        elif (tag1_inn != None and tag2_inn != None):
            dist2 = nltk.ConditionalFreqDist((tag1,tag2) for (tag1,tag2) in self.tekst 
                                    if tag1 == tag1_inn and tag2 == tag2_inn)
            return dist2
        elif(tag1_inn == None and tag2_inn == None):
            dist3 = nltk.ConditionalFreqDist((tag1,tag2) for (tag1,tag2) in self.tekst)
            return dist3
       
    def dictonary(self,dist):
        dictonary = dict((tag,dist[tag].most_common(1)) for tag in dist.conditions())
        mostcommon = sorted(dictonary)[0]
        return (mostcommon, dictonary)
        
    def tag_list(self):
        tags_list = []
        for word,tags in self.tekst:
            tags_list.append(tags)
        return tags_list

brown = HMM(nltk.corpus.brown.tagged_words(categories=nltk.corpus.brown.categories()))

#Oppgave 1.2 a)
(mostcommon, substantiv) = brown.dictonary(brown.freqDist(None,"NN"))
for tag in substantiv:
    if(tag == mostcommon):
        print("Den mest brukte taggen av substantiv og ordet som har taggen mest:")
        print(tag, substantiv[tag])
        
#Oppgave 1.2 b)
(mostcommon, ling) = brown.dictonary(brown.freqDist("linguist",None))
print("\nForekomstene av linguist med tagger:")
print(ling)

#Oppgave 1.2 c)
(mostcommon, adjektiv) = brown.dictonary(brown.freqDist(None,"JJ"))
for tag in adjektiv:
    if(tag == mostcommon):
        print("\nDen mest brukte taggen av adjektiv og ordet som har taggen mest:")
        print(tag, adjektiv[tag])

#Oppgave 1.3
cfd = brown.freqDist(None,None)
cpd = nltk.ConditionalProbDist(cfd, nltk.MLEProbDist)
print("\nSetter inn samme som i eksempelet for testing")
print("Ordet: %s" % cpd['JJ'].max())
print("Sannsynlighet: %0.4f" % cpd['JJ'].prob('new'))

#Oppgave 1.4
tag_list_bigram = nltk.bigrams(brown.tag_list())

#Oppgave 1.5a)
brown2 = HMM(nltk.bigrams(brown.tag_list()))
(mostcommon, tagdistNN) = brown2.dictonary(brown2.freqDist_tags("NN",None))
for tag in tagdistNN:
    if(tag == mostcommon):
        print("\nDen mest brukte taggen etter substantiv og antall ganger er:")
        print(tagdistNN[tag])

#Oppgave 1.5b)
brown3 = HMM(nltk.bigrams(brown.tag_list()))
(mostcommon, tagdistDT) = brown3.dictonary(brown3.freqDist_tags("DT","NN"))         
print("\n'DT NN' forekommer %d ganger" % list(tagdistDT.values())[0][0][1])

#Oppgave 1.6
brown4 = HMM(nltk.bigrams(brown.tag_list()))
tagdist = brown4.freqDist_tags()
cpd2 = nltk.ConditionalProbDist(tagdist, nltk.MLEProbDist)
print("Det er %0.4f sannsynligheten for et substantiv, gitt et determinativ" % cpd2["DT"].prob("JJ"))

"""
Lagde en klasse med alle metodene jeg trenger for aa lose oppgavene i 1.
Lagde en metode for sammenligning av tagger og en for ord med tagger, det var for 
korrekt sortering i dictionary. 
"""


#Oppgave 2
transA = cpd2["VBD"].prob("PP$") * cpd2["PP$"].prob("NN")
obervA = cpd["PP$"].prob("her") * cpd["NN"].prob("duck")

transB = cpd2["VBD"].prob("PPO") * cpd2["PPO"].prob("VB")
obervB = cpd["PPO"].prob("her") * cpd["VB"].prob("duck")

totalA = transA*obervA
totalB = transB*obervB

print("""\nFor oppgave a) er transisjonssannsynligheten: %0.5f, observasjonssannsynligheten: %0.5e. 
Total sansynlighet for lesning a) er: %0.5e""" % (transA,obervA,totalA))
print("""\nFor oppgave b) er transisjonssannsynligheten: %0.5f, observasjonssannsynligheten: %0.5e. 
Total sansynlighet for lesning b) er: %0.5e\n""" % (transB,obervB,totalB))


"""
Jeg bruker cpd og cpd2 fra oppgave 1, cpd finner ordene og cpd2 ser på tagger.
Setter saa inn forskjellene for de to setningene og regner ut de forskjellige sannsynlighetene.

b) varianten er mest sannsynlig. Altsa, "Jeg saa henne dukke" er mer sannsynlig enn
"Jeg saa hennes and". Det virker jo ganske rimelig.

"""
#Oppgave 3 
from nltk.corpus import conll2000
training_chunks = conll2000.chunked_sents("train.txt", chunk_types=["NP"])

grammar = r"""
NP:  
     {<DT|PP\$>?<JJ.*>*<NN.*>+}
     {<DT|PP|PRP>?<NN.*>*<CC|TO>?<NN.*>+}
     """
              
cp = nltk.RegexpParser(grammar)
test_chunks = conll2000.chunked_sents("test.txt", chunk_types=["NP"])
print(cp.evaluate(test_chunks))

"""
ChunkParse score:
    IOB Accuracy:  80.9%
    Precision:     71.9%
    Recall:        62.3%
    F-Measure:     66.8%
    
Mine metoder i parseren ser paa forskjellige konfigurasjoner av NP'er.
{<DT|PP\$>?<JJ.*>*<NN.*>+} finner chunks som starter med en 
Determinant (DT) eller Preposisjon (PP), ser saa om det er en adjektiver (JJ) 
saa til slutt Substantiver (NN) ved bruk av .* saa vil taggene som starter med 
NN og JJ finnes, ikke bare rene NN og JJ.

{<DT|PP|PRP>?<NN.*>*<CC|TO>?<NN.*>+} finner preposisjoner som eventuelt kan er 
etterfulgt av and eller to saa substantiv.

Jeg hadde flere setninger i parseren min, men endte opp med disse mer kompliserte 
istedet for de enklere jeg hadde. Det gjorde jeg for aa faa flere chunks, de finner
fortsett de enklere mulighetene ogsaa. Endte dermed opp med mindre enn fem totalt, men 
alt som trengs ligger inne i disse 2.

"""
