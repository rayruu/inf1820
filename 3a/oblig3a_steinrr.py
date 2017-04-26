# encoding: utf-8
import nltk
from hmm import *

##### 1 Betinget sannsynliget
### 1.1
# hentet fra NLTK:
wsj = nltk.corpus.brown.tagged_words()

mostCommon = 1
### 1.2
# a og c -  tolker som at jeg bare skal finne NN og JJ, men for sikkerhetskyld har jeg satt opp for aa finne flere
# substantiv:
#             NN     - singular substantiv
#             NN$    - bestemt singular sub
#             NNS    - flertall sub
#             NP     - riktig  sub
#             NP$    . bestemt flertall sub
#             NPS    - riktig flertall sub
#             NPS$   - bestemt flertall sub
#             NR     - adverb subs  (home, today, west)
tagNN = hmm(0, "NN")
tagdicNN = tagNN.findTags(mostCommon)
listeNN = [[tag, tagdicNN[tag]] for tag in sorted(tagdicNN)]

print("Oppgave 1")
print("1a:")
print(listeNN[0])

# b:
linguist = hmm("linguist", 0)
named = linguist.findName(mostCommon)


print("1b:")
print(named)

# Adjektiv:
#           JJ        - adjektiv
#           JJR       - komperativ adj
#           JJS       - semantisk superlativ adj (chief, top)
#           JJT       - morfologisk superlativ adj (biggest)

tagJJ = hmm(0, "JJ")
tagdicJJ = tagJJ.findTags(mostCommon)
listeJJ = [[tag, tagdicJJ[tag]] for tag in sorted(tagdicJJ)]

print("1c:")
print(listeJJ[0])

#### 1.3
print("oppgave 1.3")

# Obsjervasjonssansynlighet - (Lexical Likelihood)
cpdNN = tagNN.findCPD()
print("NN max: %s"  %cpdNN["NN"].max())
print("P(time|NN) %.3f" %cpdNN["NN"].prob("time")) #(P(time|NN))

cpdJJ = tagJJ.findCPD()
print("JJ max: %s"  %cpdJJ["JJ"].max()) 
print("P(new|JJ): %.3f" %cpdJJ["JJ"].prob("new")) #(P(new|JJ))

#### 1.4
print("oppgave 1.4")
#lagt mest inn i klassen hmm.
bigramNN = tagNN.findBigrams()
tagdicBiNN = tagNN.biFrekvens(mostCommon)
listeBiNN = [[tag, tagdicBiNN[tag]] for tag in sorted(tagdicBiNN)]

sortListeBiNN = sorted(listeBiNN, key=lambda antall: antall[1][0][1], reverse = True)

print("oppgave 1.5")
print("a: tagg som oftest etterfulger substantiv(NN) er IN - Preposisjon:")
print(sortListeBiNN[2])
print("b: DT - NN forekommer: ")
print(sortListeBiNN[19])

print("oppgave 1.6")
#transisjonssansynlighet (transition probabilities / taggsekvens)
cpdBiNN = tagNN.findCPD("bi")
print("P(NN|DT): %.4f" %cpdBiNN["DT"].prob("NN"))
print("P(IN|NN): %.4f" %cpdBiNN["IN"].prob("NN"))

print("\noppgave 2:")
# setter opp for PP:
taggPP = hmm(0,"PP")
taggdicPP = taggPP.findTags()
cpdPP = taggPP.findCPD()

#Obsjervasjonssansynlighet - (Lexical Likelihood)
p_her_PPS = cpdPP["PP$"].prob("her")   # P(her|PP$)
p_her_PPO = cpdPP["PPO"].prob("her")   # P(her|PPO)

# setter opp for VB:
taggVB = hmm(0,"VB")
tagdicVB = taggVB.findTags()
cpdVB = taggVB.findCPD()

p_duck_NN = cpdNN["NN"].prob("duck")   # P(duck|NN)
p_duck_VB = cpdVB["VB"].prob("duck")   # P(duck|VB)

#Obsjervasjonssansynlighet - (Lexical Likelihood)
obsprob1 = p_her_PPS*p_duck_NN
obsprob2 = p_her_PPO*p_duck_VB
#print("Observasjonssansynlighet for P(her|PP$) og P(duck|NN): %.6f" %obsprob1)
#print("Observasjonssansynlighet for P(her|PPO) og P(duck|VB): %.6f" %obsprob2)

bigramPP   = taggPP.findBigrams()
tagdicBiPP = taggPP.biFrekvens()

cpdBiPP    = taggPP.findCPD("bi")

p_PPS_VBD  = cpdBiPP["VBD"].prob("PP$")
p_PPO_VBD  = cpdBiPP["VBD"].prob("PPO")

p_NN_PPS = cpdBiPP["PP$"].prob("NN")
p_VB_PPO = cpdBiPP["PPO"].prob("VB")

#transisjonssansynlighet (transition probabilities / taggsekvens)
trans1 = p_PPS_VBD*p_NN_PPS
trans2 = p_PPO_VBD*p_VB_PPO
#print("Transjisjonssannsynslighet for P(PP$|VBD) og P(NN|PP$): %.6f" %trans1)
#print("Transjisjonssannsynslighet for P(PPO|VBD) og P(VB|PPO): %.6f" %trans2)

totalProbNN = p_NN_PPS*p_PPS_VBD*p_duck_NN*p_her_PPS*1000  # duck = and
totalProbVB = p_VB_PPO*p_PPO_VBD*p_duck_VB*p_her_PPO*1000  # duck = dykk

print("total sannsynlighet for at setningen avslutter med duck som substantiv er: %.2e" %totalProbNN)
print("total sannsynlighet for at setningen avslutter med duck som et verb er: %.2e" %totalProbVB)



# Oppgave 3:

print("\noppgave 3")
from nltk.corpus import conll2000
training_chunks = conll2000.chunked_sents("train.txt", chunk_types=["NP"])

grammar = r"""
      NP: {<DT|PP\$>?<JJ.*>*<NN.*>+}   
          {<NNP>+}                
          {<NN>*<CD>+<NN>+}
          {<JJ\$><NN.*>+}
          {<JRR\$>?<IN>*<NNS>}   
          {<DT|PP|PRP>?<NN.*>*<CC|TO>?<NN.*>+}    
"""

cp = nltk.RegexpParser(grammar)
evaluate_training = cp.evaluate(training_chunks)
test_chunks = conll2000.chunked_sents("test.txt", chunk_types=["NP"])
evaluate_testing = cp.evaluate(test_chunks)

print("Evaluerer med treningsett:")
print(evaluate_training)
print("Evaluerer med testsett:")
print(evaluate_testing)

"""
Legger loggen nederst.

Oppsummering:
Jeg inser at jeg kunne kjoert en felles taggliste og forbedret min klasse slik at jeg ikke trenger aa lage en klasse for hver av
ordklassene: NN, VB, JJ osv. Men dette fikk jeg ikke tid til aa justere.

Ellers saa tror jeg at det ser ryddig ut i forhold til fremgangen jeg bruker. Det er muligens lite kommentarer i klassen, men
 bear with me.

Oppgave 2. Saa faar jeg mest sannsynlighet paa "Jeg saa henne dukke" som virker ogsaa mest sansynlig for meg aa faa.

I oppgave 3 saa provde jeg en del forskjellig, men jeg fikk ikke saa mye bedre resultatt enn dette:

Run logg:

$ python oblig3a_steinrr.py 
Oppgave 1
1a:
['NN', [('time', 1547)]]
1b:
['linguist', [('NN', 9)]]
1c:
['JJ', [('new', 1036)]]
oppgave 1.3
NN max: time
P(time|NN) 0.010
JJ max: new
P(new|JJ): 0.016
oppgave 1.4
oppgave 1.5
a: tagg som oftest etterfulger substantiv(NN) er IN - Preposisjon:
['NN', [('IN', 42256)]]
b: DT - NN forekommer: 
['DT', [('NN', 4367)]]
oppgave 1.6
P(NN|DT): 0.4876
P(IN|NN): 0.1429

oppgave 2:
total sannsynlighet for at setningen avslutter med duck som substantiv er: 3.30e-05
total sannsynlighet for at setningen avslutter med duck som et verb er: 6.12e-05

oppgave 3
Evaluerer med treningsett:
ChunkParse score:
    IOB Accuracy:  80.8%
    Precision:     71.5%
    Recall:        61.5%
    F-Measure:     66.1%
Evaluerer med testsett:
ChunkParse score:
    IOB Accuracy:  80.9%
    Precision:     71.9%
    Recall:        62.3%
    F-Measure:     66.8%

"""
