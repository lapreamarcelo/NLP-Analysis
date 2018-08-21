#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 00:18:48 2018

@author: marcelolaprea
"""
import string
import spacy

from nltk.corpus import stopwords

class SPACY_POS_Tagger:
    
    def return_lemma_spacy(dataFrame):
        nlp = spacy.load('es_core_news_sm')
        tokens = []
        
        for sentence in dataFrame['Title']:
            doc = nlp(sentence)
            
            for token in doc:
                pos_token = token.lemma_
                pos_token = pos_token.lower()
                
                #Quitar signos de puntuacion
                clean_punctuation = str.maketrans('','', string.punctuation)
                pos_token = pos_token.translate(clean_punctuation)
                
                #Eliminamos los stopwords
                stop_words = set(stopwords.words('spanish'))
                
                if pos_token.isalpha() and pos_token not in stop_words:
                    tokens.append(pos_token)
                
        return tokens
    
    
    def return_spacy(dataFrame):
        nlp = spacy.load('es_core_news_sm')
        tokens = []
        
        for sentence in dataFrame['Title']:
            doc = nlp(sentence)
            
            for token in doc:
                pos_token = token.text
                pos_token = pos_token.lower()
                
                #Quitar signos de puntuacion
                clean_punctuation = str.maketrans('','', string.punctuation)
                pos_token = pos_token.translate(clean_punctuation)
                
                #Eliminamos los stopwords
                stop_words = set(stopwords.words('spanish'))
                
                if pos_token.isalpha() and pos_token not in stop_words:
                    tokens.append(pos_token)
                
        return tokens