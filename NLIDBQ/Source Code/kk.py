#!/usr/bin/python2.7

import nltk
from nltk.tokenize import word_tokenize


str = "who teaches Physics"

toke = word_tokenize(str)

newToke = nltk.pos_tag(toke)
print newToke