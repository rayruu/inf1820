"""
Dette programmet skal uttføre "tokenisering", dvs bryte opp en tekst opp i ord. Tokenisering er nødvendig utgangspunkt for de aller fleste språkteknologiske oppgaver. 

- dev.txt skal ligge i samme mappe. 
- Programmet er laget for python 3

For å kjøre programmet: obliga_steinrr.py
"""
# encoding: utf-8

class readFile:
    """ Read filename and returns with content"""
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        text = open(self.filename)
        self.content = text.read()
        text.close()
        return (self.content)

###################################
########## main ###################

def main():
    # initial parameters:
    filename = "dev.txt"
    occur = "er"
    count = 0 
    liste = []
    
    # Task 1:
    ################################################################################	
    # Part a:
    ################################
    # Read text
    problem = readFile(filename)   # read file in same folder.
    text = problem.read()


    # Part b:
    #################################   
    counted_occur = text.count(occur)
    print ("------------------------")
    print ("Task 1b: Count instances ")
    print ("Combination \"%s\" occured %d in text: \"%s\"." %(occur, counted_occur, filename))

    text = text.split() # split up text
    
    for word in text:
        if word.endswith(occur):
            count += 1
            
        # NOTE: It does not say explicit in task C to ignore letters like: . , : - " etc.
        # However I have made extra effort to do so. 
        if (word[-1] == ".") or (word[-1] == ",") or (word[-1] == ":") or (word[-1] == "-"): # "." and "," is not a letter
            if len(word)>2:
                liste.append(word[-3:-1])
            else:
                liste.append(word)
        else:
            if len(word)>2:
                liste.append(word[-2:])
            else:
                liste.append(word)

    print ("While %d words ends with letter combination: \"%s\" in the same text" %(count, occur))

    # Part c:
    ####################################
    print ("------------------------")
    print ("task 1c:")

    # remove "-" from list
    for word in liste:
        if word[-1]=="-":
            liste.remove(word)

    for word in liste:
        if word[-1] == "-":
            print (word)
    
    print ("first 3 words in list: %s" %liste[:3])    
    # convert list to string:
    stringText = ' '.join(map(str, liste))
    print ("Converted list to string.")
    print ("First nine letters in string: %s" %stringText[:9])

    # Task 2:
    #######################################################################################
    # Part a and b:
    ####################################
    print ("------------------------")
    print ("Task 2a and 2b:")
    
    infile = open(filename)
    lines = []
    for line in infile:
        if (line != "\n"):       # split line and ignore lines with space (\n), we do not count empty lines
            lines.append(line)
    infile.close()
    print ("Read file: \"%s\" as a list" %filename)

    #print (lines)

    counted_words, counted_lines = countLine(lines)
    print ("Counted %d lines and %d words from file \"%s\"" %(counted_lines, counted_words, filename))


def countLine(lines):
    """ Count lines and words from list"""
    count_words = 0
    count_lines = 0

    for line in lines:
        words = line.split()
        for word in words:
            #if (word != "\n"):   # make sure a word is not equal "\n"
            count_words += 1

        count_lines += 1
        
    return (count_words, count_lines)
    


if __name__ == "__main__":
    main()

    
""" Run log:
 python oblig1a_steinrr.py ------------------------
Task 1b: Count instances 
Combination "er" occured 5093 in text: "dev.txt".
While 2625 words ends with letter combination: "er" in the same text
------------------------
task 1c:
first 3 words in list: ['er', 'nn', 'en']
Converted list to string.
First nine letters in string: er nn en 
------------------------
Task 2a and 2b:
Read file: "dev.txt" as a list
Counted 972 lines and 32243 words from file "dev.txt"

"""
