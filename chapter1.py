from __future__ import division
from nltk.book import *

text1.concordance("beautiful")
text1.similar("beautiful")
text3.count("ivory")
sorted(set(text3))

def lexical_diversity(text):
    return len(text)/ len(set(text))

def percentage(count, total):
    return 100 * count / total

lexical_diversity(text3)
