import nltk
#from nltk import *

# TEst:
#grammar = nltk.CFG.fromstring("""
#    S   ->  NP VP
#    VP  ->  V NP | V NP PP
#    PP  ->  P NP
#    V   ->  "saw" | "ate" | "walked"
#    NP  ->  "John" | "Mary" | "Bob" | Det N | Det N PP
#    Det ->  "a" | "dog" | "cat" | "telescope" | "park"
#    P   ->  "in" | "on" | "by" | "with"
#""")
"""
print("Test")

sent = "Mary saw Bob".split()
print(sent)
rd_parser = nltk.RecursiveDescentParser(grammar)
for tree in rd_parser.parse(sent):
    print(tree)
"""
print("Oppgave 1: En grammatikk for norsk")
print("1.1")
grammarNorsk = nltk.CFG.fromstring("""
    S    ->  NP VP PP | NP VP
    VP   ->  V | V NP | V NP NP 
    PP   ->  P NP
    V    ->  "sover" | "spiser" | "gir" | "finner"
    NP   ->  "Per" | "Kari" | "Ola" | "boka" | "middag" | D N
    D    ->  "en"
    N    ->  "bok" 
    P    ->  "til"
""")
les_parser =  nltk.RecursiveDescentParser(grammarNorsk)
def skrivUtTree(setninger):
    for setning in setninger:
        for tree in les_parser.parse(setning):
            print(tree)


"""
(a) (S (NP Per) (VP (V gir) (NP (D en) (N bok)) (PP (P til) (NP Kari))))
(b) (S (NP Kari) (VP (V gir) (NP Per) (NP boka)))
(c) (S (NP Ola) (VP (V sover)))
(d) (S (NP Kari) (VP (V spiser)))
(e) (S (NP Kari) (VP (V spiser) (NP middag)))
(f) (S (NP Per) (VP (V finner) (NP boka)))

(a) Per gir en bok til Kari
(b) Kari gir Per boka
(c) Ola sover
(d) Kari spiser
(e) Kari spiser middag
(f) Per finner boka
"""
setninger = [["Per", "gir", "en", "bok", "til", "Kari"],
             ["Kari", "gir", "Per" ,"boka"],
             ["Ola", "sover"],
             ["Kari", "spiser"],
             ["Kari", "spiser",  "middag"],
             ["Per", "finner", "boka"]]

skrivUtTree(setninger)

print("1.2")
setninger12 = [["Kari", "sover", "boka"], ["Ola", "finner"]]
skrivUtTree(setninger12)

print("1.3")
grammarNorsk2 = nltk.CFG.fromstring("""
    S    ->  NP VP PP | NP VP
    VP   ->  V | V NP | V NP NP | TV NP | TV NP NP | iTV
    PP   ->  P NP
    V    ->  "spiser"
    TV   ->  "gir" | "finner"
    iTV  ->  "sover"
    NP   ->  "Per" | "Kari" | "Ola" | "boka" | "middag" | D N
    D    ->  "en"
    N    ->  "bok" 
    P    ->  "til"
""")
les_parser =  nltk.RecursiveDescentParser(grammarNorsk2)
skrivUtTree(setninger)
skrivUtTree(setninger12)

print("Oppgave 2: Manuell annotering av ordbetydning")
"""
1. But questions with which committee members taunted bankers appearing as witnesses left little doubt that they will recommend passage of it.

left - leave#3
Mener det er leave#3 fordi det er snakk om tvil, og tilstanden til tvil.

2. The departure of the Giants and the Dodgers to California left New York with only the Yankees.

left - leave#2 
Mener det er leave#2 fordi vi forlater Yankees i New York.

3. After the coach listed all the boy’s faults , Hartweger said , “Coach before I leave here , you’ll get to like me ”.

4. R. H. S. Crossman , M.P. , writing in The Manchester Guardian , states that departures from West
Berlin are now running at the rate not of 700 , but of 1700 a week , and applications to leave have
risen to 1900 a week.

5. The house has been swept so clean that contemporary man has been left with no means , or at best
with wholly inadequate means , for dealing with his experience of spirit .

"""

