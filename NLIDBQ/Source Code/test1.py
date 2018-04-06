#!/usr/bin/python2.7

import nltk
from nltk.tokenize import word_tokenize


str = "Pranav is"

toke = word_tokenize(str)

newToke = nltk.pos_tag(toke)

toke = newToke[0]

print toke[1]