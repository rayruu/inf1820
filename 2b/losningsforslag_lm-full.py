# encoding: utf-8

from math import log, pow
import nltk
from nltk import bigrams
from nltk.probability import ConditionalFreqDist, FreqDist, ConditionalProbDist, LaplaceProbDist

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
                self.bigrams[prev].inc(word)
                self.unigrams.inc(word)

        self.bigrams = ConditionalProbDist(self.bigrams, LaplaceProbDist)
        self.unigrams = LaplaceProbDist(self.unigrams)

    def p(self, w, prev):
        p = 0.5*self.unigrams.prob(w)
        if prev in self.bigrams:
            p += self.bigrams[prev].prob(w)
        return p

    def logprob(self, s):
        s = [None] + s + [None]
        logprob = 0.0
        for prev, word in bigrams(s):
            logprob += log(self.p(word, prev), 2)
        return logprob

    def perplexity(self, sents):
        logprob = 0.0
        words = 0
        for s in sents:
            words += len(s)
            logprob += self.logprob(s)
        return pow(2, -logprob/words)

