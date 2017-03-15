import nltk
from collections import defaultdict
from operator import itemgetter
import time
start = time.time()

brown = nltk.corpus.brown.tagged_words(categories="news")
brown = sorted([(ordformer.lower(), tagger) for ordformer, tagger in brown])

def freqs(w):
   Frkv = defaultdict(int)
   totalt = 0
   for ordform, tags in brown:
      if ordform == w:
         totalt += 1
         Frkv[tags] +=1
   return sorted(Frkv.items(), key=itemgetter(1), reverse=True), totalt   

# oppgave 1:
antallFrkvtOrd = defaultdict(int)
antallFrkvtTag = defaultdict(int)

# setter opp bibliotek med ordform og tagg som nokkelord
# teller antall ganger ordform eller tagg oppstaar:
for i in range(len(brown)):
   ordform, tags = brown[i]
   antallFrkvtOrd[ordform] += 1
   antallFrkvtTag[tags] += 1

# Finner min og max
maxVerdiOrdFrkv = max(antallFrkvtOrd.values())
maxOrdFrkvns = [key for key,val in sorted(antallFrkvtOrd.items(), key=itemgetter(1), reverse=True)
                if val == maxVerdiOrdFrkv]

maxVerdiTagFrkv = max(antallFrkvtTag.values())
maxTagFrkvns = [key for key, val in sorted(antallFrkvtTag.items(), key=itemgetter(1), reverse=True)
                if val == maxVerdiTagFrkv]

minVerdiTagFrkv = min(antallFrkvtTag.values())
minTagFrkvns = [key for key, val in sorted(antallFrkvtTag.items(), key=itemgetter(1), reverse=True)
                if val == minVerdiTagFrkv]

print("Oppgave 1.1: Maks frekvente orde[t/ene[ er '%s' med antall %s " 
      %(maxOrdFrkvns, maxVerdiOrdFrkv))
print("Oppgave 1.2: Maks frekvente ordklasse[r] er '%s' med antall %i " 
      %(maxTagFrkvns,maxVerdiTagFrkv))
print("Oppgave 1.3: Min frekvente ordklasse[r] er \n '%s'\n med antall %i " 
      %(minTagFrkvns,minVerdiTagFrkv))

# oppgave 2:
ordformToTagg = {}
distinktTagg = set()

# setter opp bibliotek som knytter flere tag til samme ord.
# teller ogsaa distinkte tagger som oppstaar
for ordform, tagg in brown:
   ordformToTagg.setdefault(ordform, [])
   distinktTagg.add(tagg)
   if ordform in ordformToTagg:
      if tagg not in ordformToTagg[ordform]:
          ordformToTagg[ordform].append(tagg)

flertydigOrd = 0
for ord in ordformToTagg:
   if len(ordformToTagg[ord]) > 1:
      flertydigOrd += 1
      
ordValueFlestTagg = len(max(ordformToTagg.values(), key=lambda k: len(k)))
ordFlestTagg = [tagg for tagg, ordform in sorted(ordformToTagg.items(), key=itemgetter(1), reverse=True)
                if ordValueFlestTagg == len(ordform)]

print("Oppgave 2.1: Det forekommer %d ord med mer enn en ordklassetagg" %flertydigOrd)
print("Oppgave 2.2: Der ordene: %s har %d disjunkte klasser som vil si at disse ordene har flest tagger"
      %(ordFlestTagg, ordValueFlestTagg))

print("Oppgave 2.4:" )
for ord in ordFlestTagg:
   forekommer, totalt = freqs(ord)
   print("Ord '%s' forekommer totalt %d ganger med frekvensliste: %s" %(ord, totalt, forekommer))

end = time.time()
print("Runtime: %f" %(end-start))


""" run log:
$ python oblig2a_steinrr.py 
Oppgave 1.1: Maks frekvente orde[t/ene[ er '['the']' med antall 6386 
Oppgave 1.2: Maks frekvente ordklasse[r] er '['NN']' med antall 13162 
Oppgave 1.3: Min frekvente ordklasse[r] er 
 '['NNS-TL-HL', 'UH-TL', 'BE-HL', 'VBD-TL', 'FW-VB', 'MD*-HL', 'VBN-TL-HL', 'FW-PP$-NC', 'MD+HV', 'AP-TL', 'FW-*', 'BED*', 'ABN-HL', 'PN$', 'RB$', 'PPSS-HL', 'JJ-NC', 'JJR-NC', 'DT-HL', 'HVD-HL', 'FW-IN+AT-TL', 'FW-CC', 'BER-TL', 'FW-DT', '*-HL', 'NR$-TL', 'PPS+BEZ-HL', 'WQL', 'NP+BEZ', 'TO-TL', 'PN-HL', 'CS-HL', 'MD-TL', 'DT$', 'FW-AT-HL', 'NPS$-TL', 'HVZ*', 'FW-VB-NC', 'OD-HL', 'BER-HL', 'NP-TL-HL', 'PP$-TL', 'VB+PPO', 'WDT+BEZ', 'FW-IN+NN-TL', 'RB+BEZ', 'FW-WDT', 'BEDZ-HL', 'QL-TL', 'PN+HVZ', 'FW-IN-TL', 'FW-CD', 'DO-HL', 'AP$', 'PPSS+HVD']'
 med antall 1 
Oppgave 2.1: Det forekommer 2166 ord med mer enn en ordklassetagg
Oppgave 2.2: Der ordene: ['house', 'to'] har 7 disjunkte klasser som vil si at disse ordene har flest tagger
Oppgave 2.4:
Ord 'house' forekommer totalt 97 ganger med frekvensliste: [('NN-TL', 68), ('NN', 24), ('NN-HL', 1), ('VB', 1), ('NP', 1), ('NP-TL-HL', 1), ('NN-TL-HL', 1)]
Ord 'to' forekommer totalt 2144 ganger med frekvensliste: [('TO', 1237), ('IN', 889), ('TO-HL', 6), ('IN-TL', 5), ('IN-HL', 5), ('NPS', 1), ('TO-TL', 1)]
Runtime: 0.768130
"""
