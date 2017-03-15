import re
from regtex import beskriver, finnOrdListe

epost1 = "steinrr@student.matlab.no"
epost2 = "stein.rayruu@student.matlab.no"

reg_utrykk = r"(\w+[\.?\w+]*@\w+[\.?\w+]*)"

print(beskriver(reg_utrykk, epost1))

#print(finnOrdListe(reg_utrykk, epost1))

print(re.findall(reg_utrykk, epost1))

filename = open("email.txt", 'r')
tekst = filename.read()
filename.close()

print(re.findall(reg_utrykk, tekst))
