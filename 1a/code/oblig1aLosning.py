# encoding: utf-8

###########
#Oppgave 1

#1a)
#les inn hele filen som en streng
f = open("dev.txt")
filinnhold = f.read()
f.close()

#1b)
#Tell forekomster av er
er = filinnhold.count("er")
print ("Antall forekomster av 'er' er:",er)

#Tell forekomster av er til slutt
cnt = 0
for w in filinnhold.split():
    if w.endswith("er"):
        cnt += 1
print("Antall ord som slutter på `er':",cnt)

#1c)
# Den mest avanserte varianten, med list comprehension:
l = [w[-2:] for w in filinnhold.split()]

# Litt enklere med en for-løkke:
l = []
for w in filinnhold.split():
    l.append(w[-2:])

print(' '.join(l))


###########
#Oppgave 2

f = open("dev.txt")

num_lines = 0
num_words = 0

for line in f:
    num_lines = num_lines + 1
    for w in line.split():
        num_words = num_words + 1

f.close()

print("Antall linjer er: ",num_lines)
print("Antall ord er: ",num_words)






