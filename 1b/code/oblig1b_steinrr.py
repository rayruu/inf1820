# oppgave 1 a:
f = open("dev.txt")
outfile = open("obligtekst.txt", "w")

for line in f:
    for w in line.split():
        outfile.write("%s\n" %w)
outfile.close()
f.close()

# oppgave 1 b:
"""
Bruker kommando:
$ python3 oblig1b_steinrr.py && diff obligtekst.txt dev_gold.txt >difftekst.txt

funksjonen .split() skiller bare paa whitespace
det vil si at tegnene som er forskjellig fra
dev_gold er:
    ,«.?:()! osv.

"""
import re
# oppgave 1 c:
gyldig_ord = r'[\d]+-[\w]+|[\.\.\.]|[\d]+\.?[\d]+|[\wæøå]+-[\w]+|[\w]+\.[\w]|[\w]+\'[\w]+|[\wæøå]+|[,«»\.:;(!)"\?\+-§]'

f = open("dev.txt")
outfile = open("obligtekst.txt", "w")
teller = 0
for line in f:
    funnetOrd = re.findall(gyldig_ord, line)
    for ord in funnetOrd:
        outfile.write("%s\n" %ord)
outfile.close()
f.close()

"""
Dette kan jeg jobbe med til tidenes morgen. Tenker det er et poeng med dette. Det
hjelper ikke bare bruke re.findall fordi i teksten er det for eksempel punkter: ... og
dette klarer ikke mitt reguleare uttrykk skille ut. Det er ogsaa noen tall i forholdt til fasit som
har punktum etter seg. Dette klarer jeg aa skille ut, men det er andre steder det ikke skal veare
punktum. Det vil si det skal mer til for aa skille ut og la det bli 100 % likt.

Rekkefolgen jeg har skrevet regulearte utrykkket har ogsaa litt og si. Det er mange ord igjen, men
dette krever ytterligere analyse

Sette inn if-statement kan veare noe, eller segmentere det for aa se paa ordene. Slik at vi
vet hva som for eksempel er egenavn osv.

Konklusjon jeg fant vell ogsaa flere feil enn naar jeg bare saa tegnene.
"""

    
