# encoding: utf-8

import nltk
from nltk import bigrams
from nltk.probability import ConditionalFreqDist, FreqDist, ConditionalProbDist, MLEProbDist


class hmm:
    def __init__(self, name = 0, tag = 0):
        self.name = name
        self.tag = tag

        self.wsj = nltk.corpus.brown.tagged_words()
        self.sentences = nltk.corpus.brown.sents()
        #self.cfdTagAll = ConditionalFreqDist(tag, word for (word, tag) in self.wsj)

    def findTags(self, mostCommon = 5):
        if self.tag != 0:
            self.tag_prefix = self.tag
            self.cfdTag = ConditionalFreqDist((tag, word) for (word, tag) in self.wsj
                                              if tag.startswith(self.tag_prefix))
            return dict((tag, self.cfdTag[tag].most_common(mostCommon)) for tag in self.cfdTag.conditions())
        else:
            print("invalid method")
            

    def findAllTags(self, mostCommon = 5):
        self.cfdTagAll = ConditionalFreqDist((tag, word) for (word, tag) in self.wsj)
        for tag in sorted(self.cfdTagAll):
            print(tag, self.cfdTagAll[tag].most_common())
            #print(self.cfdTagAll)
        return dict(self.cfdTagAll)


    def findBigrams(self):
        self.bigram = bigrams([tag for word, tag in self.wsj])
        return self.bigram

    def biFrekvens(self, mostCommon = 5):
        self.cfdBigram = ConditionalFreqDist(self.bigram)
        return dict((tag, self.cfdBigram[tag].most_common(mostCommon)) for tag in self.cfdBigram)
                

    def findName(self, mostCommon = 5):
        if self.name != 0:
            self.cfdName = ConditionalFreqDist((word.lower(), tag) for (word, tag) in self.wsj)
            return [self.name, self.cfdName[self.name].most_common(mostCommon)]
        else:
            print("invalid method")

    def findCPD(self, typecfd = None):
        if(typecfd == None):
            self.cpdTag = nltk.ConditionalProbDist(self.cfdTag, nltk.MLEProbDist)
            return self.cpdTag
        elif (typecfd == "bi"):
            return ConditionalProbDist(self.cfdBigram, nltk.MLEProbDist)
        else:
            print("invalid method")

"""
def findtags(tag_prefix, tagged_text, mostCommon):
    # reverserer slik at tag blir tilstand og ord blir event og henter ut tags som har lik prefix
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                   if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(mostCommon)) for tag in cfd.conditions())

def findName(name, text_tagged, mostCommon):
    cfd = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in text_tagged)
    return [name, cfd[name].most_common(mostCommon)]

    def transProb(self):
        liste = list(self.findAllTags().keys())
        return bigrams(liste)
                             

"""
