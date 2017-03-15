# encoding: utf-8
import re

def beskriver(regeksp, ord):
	reg= "^("+regeksp+")$"
	if re.search(reg, ord):
		return True
	else: 
		return False
        
def finnOrdListe(regeksp,liste):
        reg = r"^("+regeksp+")$)"
        return re.findall(reg, liste)

def test_1():
        regeks = "(a|b|c)*bbb(a|b|c)*"
        word = ["abba", "abbaccaabbaa", "abbbbba","abcbbbababbabbbbaa" ]

        for i in word:
                trueOrFalse = beskriver(regeks,i)
                print("Regulære uttrykket: %s beskriver %s som %s" %(regeks, i, trueOrFalse))

def test_2():
        regeks = "(a|c)*((ba|bba|bc|bbc|)(a|c)*)*(b|bb)"
        word = ["abb", "abbaccaab", "abbaccaabbb","abcbbbababbabbbbaa" ]
        for i in word:
                trueOrFalse = beskriver(regeks,i)
                print("Regulære uttrykket: %s beskriver %s som %s" %(regeks, i, trueOrFalse))

def test_3():
        regeks = "(((a|c)*b(a|c)*b(a|c)*b(a|c)*)*|((b|c)*a(b|c)*a(b|c)*)*)"
        word = ["abcbacacacab", "acbaccbac","bcacbabb","aaaaaaabbccccc"]
        for i in word:
                trueOrFalse = beskriver(regeks,i)
                print("Regulære uttrykket: %s beskriver %s som %s" %(regeks, i, trueOrFalse))

if __name__ == "__main__":
        print("##################################")
        test_1()
        print("##################################")
        test_2()X+
        print("##################################")
        test_3()
