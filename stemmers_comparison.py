#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:40:19 2020

@author: user
"""


from farasa.stemmer import FarasaStemmer
from nltk.stem.isri import ISRIStemmer
from tashaphyne.stemming import ArabicLightStemmer



sentence = "عجلات"

stemmer = FarasaStemmer()

result = stemmer.stem(sentence)
print(f"\nFarasa: {result}")


stemmer = ISRIStemmer()

result = " ".join([stemmer.stem(token) for token in sentence.split()])
print(f"\nISRIStemmer: {result}")


stemmer = ArabicLightStemmer()

result = " ".join([stemmer.light_stem(token) for token in sentence.split()])
print(f"\nTashaphyne Stem: {result}")







#result = " ".join([stemmer.get_root() for token in sentence.split() if stemmer.light_stem(token)])
#print(f"\nTashaphyne Root: {result}")

