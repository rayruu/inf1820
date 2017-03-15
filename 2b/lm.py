# encoding: utf-8

import nltk
from nltk import bigrams
from nltk.probability import ConditionalFreqDist, FreqDist, ConditionalProbDist, LaplaceProbDist
from nltk.tag import RegexpTagger
from math import log

class LM:
    def __init__(self):
        self.bigrams = ConditionalFreqDist()
        self.unigrams = FreqDist()
        sentences = nltk.corpus.brown.sents(categories=nltk.corpus.brown.categories()[1:])

        for sent in sentences:
            # Vi utvider setningen med None foran, for å angi start av
            # setningen, og en None etter, for å markere setningsslutt.
            sent = [None] + sent + [None]
            for prev, word in bigrams(sent):
                self.bigrams[prev][word] += 1
                self.unigrams[word] += 1
                
        self.bigrams = ConditionalProbDist(self.bigrams, LaplaceProbDist)
        self.unigrams = LaplaceProbDist(self.unigrams)

        # regular expression:
        self.patterns = [
            (r'(.*able|.*ish|.*ible)$', 'JJ'),                              # adjectives              # 1
            (r'(The|the|A|a|An|an)$', 'AT'),                                # articles                # 2
            (r'(a|an|my|some|the)$', 'DT'),                                 # determinative           # 3
            (r'(our|its|his|their|my|your|her|out|thy|mine|thine)$','PP$'), # determinative possesive # 4   
            (r'(.*ily|.*ly)$','ADV'),                                       # adverb                  # 5
            (r'(at|in|of|over|with)$','PP'),                                # preposition             # 6
            (r'(and|because|but|if|or)$','CNJ'),                            # conjuction              # 7
            (r'([\.?!;:]+)$','.'),                                          # sentence terminator     # 8
            (r'(\,)$',','),                                                 # comma                   # 9                    
            (r'(\-)$','-'),                                                 # dash                    # 10
            
            (r'.*ing$', 'VBG'),               # gerunds
            (r'.*ed$', 'VBD'),                # simple past
            (r'.*es$', 'VBZ'),                # 3rd singular present
            (r'.*ould$', 'MD'),               # modals
            (r'.*\'s$', 'NN$'),               # possessive nouns
            (r'.*s$', 'NNS'),                 # plural nouns
            (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
            (r'.*', 'NN')                     # nouns (default)
        ]

    def p(self, w, prev):
        p = 0.5*self.unigrams.prob(w)
        if prev in self.bigrams:
            p += self.bigrams[prev].prob(w)
        return p

    def logprob(self, s):
        P = 0.0
        for prevWord, word in bigrams(s):
            P += log(self.p(word, prevWord), 2)
            
        return P

    def perplexity(self, sents):
        N = 0.0
        l = 0.0
        
        for sent in sents:
            N += len(sent)
            l += self.logprob(sent)
        
        return 2**(-l/N)

    def zipfity(self, lst):
        frekvensOrd = FreqDist()
        frekvens = []

        for setning in lst:
            frekvensOrd += FreqDist(word.lower() for word in setning)

        r = frekvensOrd.N()

        for word, antall in frekvensOrd.most_common(10):
            frekvens.append([word, antall, antall/r])
        
        return frekvens


    def regularTagger(self, lst):
        regexp_tagger = RegexpTagger(self.patterns)
        #test = regexp_tagger.tag()
        test = []

        for sentence in lst:
            test.append(regexp_tagger.tag(sentence))
        
        return test

    def analyseRegularTagger(self, name):
        regexp_tagger = RegexpTagger(self.patterns)
        checkTagg = nltk.corpus.brown.tagged_sents(categories=name)

        return regexp_tagger.evaluate(checkTagg)
