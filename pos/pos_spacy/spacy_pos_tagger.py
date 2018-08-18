#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 00:18:48 2018

@author: marcelolaprea
"""

import spacy
from nltk.corpus import stopwords
import string

class SPACY_POS_Tagger:
    
    def returnLemmaSpacy(dataFrame):
        nlp = spacy.load('es_core_news_sm')
        tokens = []
        
        for sentence in dataFrame['Title']:
            doc = nlp(sentence)
            
            for token in doc:
                posToken = token.lemma_
                posToken = posToken.lower()
                
                #Quitar signos de puntuacion
                cleanPunctuation = str.maketrans('','', string.punctuation)
                posToken = posToken.translate(cleanPunctuation)
                
                #Eliminamos los stopwords
                stop_words = set(stopwords.words('spanish'))
                
                if posToken.isalpha() and posToken not in stop_words:
                    tokens.append(posToken)
                
        return tokens
    
    
    def returnSpacy(dataFrame):
        nlp = spacy.load('es_core_news_sm')
        tokens = []
        
        for sentence in dataFrame['Title']:
            doc = nlp(sentence)
            
            for token in doc:
                posToken = token.text
                posToken = posToken.lower()
                
                #Quitar signos de puntuacion
                cleanPunctuation = str.maketrans('','', string.punctuation)
                posToken = posToken.translate(cleanPunctuation)
                
                #Eliminamos los stopwords
                stop_words = set(stopwords.words('spanish'))
                
                if posToken.isalpha() and posToken not in stop_words:
                    tokens.append(posToken)
                
        return tokens