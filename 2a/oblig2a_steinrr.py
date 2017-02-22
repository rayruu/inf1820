import nltk
from collections import defaultdict

brown = nltk.corpus.brown.tagged_words(categories="news")
brown = sorted([(ordformer.lower(), tagger) for ordformer, tagger in brown])

# oppgave 1:
antallFrkvtOrd = defaultdict(int)
antallFrkvtTag = defaultdict(int)

# setter opp bibliotek med ordform og tagg som nokkelord
# teller antall ganger ordform eller tagg oppstaar:
for i in range(len(brown)):
   ordform, tags = brown[i]
   antallFrkvtOrd[ordform] += 1
   antallFrkvtTag[tags] += 1

# finner min og max:
maxVerdiOrdFrkv = max(antallFrkvtOrd.values())
maxOrdFrkvns = [key for key in antallFrkvtOrd.keys() if antallFrkvtOrd[key]==maxVerdiOrdFrkv]
maxOrdFrkvns = max(antallFrkvtOrd.items(), key=lambda k: k[1])

maxVerdiTagFrkv = max(antallFrkvtTag.values())
maxTagFrkvns = [key for key in antallFrkvtTag.keys() if antallFrkvtTag[key]==maxVerdiTagFrkv]

minVerdiTagFrkv = min(antallFrkvtTag.values())
minTagFrkvns = [key for key in antallFrkvtTag.keys() if antallFrkvtTag[key]==minVerdiTagFrkv]

#minFrekventTag = min(antallFrekventTag.items(), key=lambda k: k[1])

print("Oppgave 1.1: Maks frekvente ordet er '%s' med antall %s " 
      %(maxOrdFrkvns))
print("Oppgave 1.2: Maks frekvente ordklassen er '%s' med antall %i " 
      %(maxTagFrkvns,maxVerdiTagFrkv))
print("Oppgave 1.2: Min frekvente ordklassene er \n '%s'\n med antall %i " 
      %(minTagFrkvns,minVerdiTagFrkv))
#print("Oppgave 1.2: Maks frekvente ordklassen er '%s' med antall %s " %maxFrekventTag)
#print("Oppgave 1.3: Minst frekvente ordklasse er '%s' med antall %s " %minFrekventTag)

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
ordFlestTagg = max(ordformToTagg.items(), key=lambda k: len(k[1]))

print("Oppgave 2.1: %d forekommer med mer enn en ordklassetagg" %flertydigOrd)
print("Oppgave 2.2: Det er %d disjunkte klasser der ordet '%s' har flest tagger"
      %(len(distinktTagg), ordFlestTagg[0]))
print("%s%s"  %ordFlestTagg)

#print(ordformToTagg)
#print(flertydigOrd)
#print(len(ordformToTagg))

"""
for i in range(5):
    temp, temp2 = brown[i]
    print(temp)
    print(temp2)
    
print(type(brown))
"""
