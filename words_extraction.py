#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 00:10:00 2018

@author: marcelolaprea
"""
import nltk
from nltk.probability import FreqDist

class Words_Extraction:

    #Funcion para extraer todos los Nouns
    def detect_nouns(self, tokens):
        is_noun = lambda pos: pos[:2] == "NN"
        nouns = [word for (word, pos) in nltk.pos_tag(tokens) if is_noun(pos)]
        
        return nouns
    
    #Funcion para extraer todos los Adjetivos
    def detect_adjectives(self, tokens):
        is_adjective = lambda pos: pos[:2] == "JJ"
        adjectives = [word for (word, pos) in nltk.pos_tag(tokens) if is_adjective(pos)]
        
        return adjectives
    
    #Funcion para extraer todos los Verbos
    def detect_verbs(self, tokens):
        is_verb = lambda pos: pos[:2] == "VB"
        verbs = [word for (word, pos) in nltk.pos_tag(tokens) if is_verb(pos)]
        
        return verbs
    
    #Distribucion de las palabras
    def returnWordFrequency(self, words, mostCommon):
        freq = FreqDist(words)
    
        return freq.most_common(mostCommon)
