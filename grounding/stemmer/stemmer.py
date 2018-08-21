#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 00:28:30 2018

@author: marcelolaprea
"""

import Stemmer
from nltk.stem.porter import PorterStemmer

class Stemmer_Grounding:
    
    def return_stemmer_tokens(self, tokens):
        stemmer = Stemmer.Stemmer('spanish')
        words = stemmer.stemWords(tokens)
        
        return words
    
    
    def return_porter_stemmer_tokens(self, tokens):
        porter = PorterStemmer()
        stemmed = [porter.stem(word) for word in tokens]
    
        return stemmed