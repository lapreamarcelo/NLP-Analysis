#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 00:18:48 2018

@author: marcelolaprea
"""
import string
import spacy

from nltk.corpus import stopwords
from collections import Counter

class SPACY_POS_Tagger:
    
    def get_articles(self, data_frame):
        articles = []
        nlp = spacy.load('es_core_news_sm')
        
        for sentence in data_frame['Title']:
            doc = nlp(sentence)
            
            articles.append(doc)
            
        return articles
    
    
    def return_lemma_tokens(self, articles):
        tokens = []
        
        for article in articles:

            for token in article:
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
        
    
    def return_tokens(self, articles):
        tokens = []
        
        for article in articles:
            
            for token in article:
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
    
    
    def return_pos_tags(self, articles):
        tags = []
        
        for article in articles:
            
            for token in article:
                pos_token = token.text
                pos_token = pos_token.lower()
                
                #Quitar signos de puntuacion
                clean_punctuation = str.maketrans('','', string.punctuation)
                pos_token = pos_token.translate(clean_punctuation)
                
                #Eliminamos los stopwords
                stop_words = set(stopwords.words('spanish'))
                
                if pos_token.isalpha() and pos_token not in stop_words:
                    tags.append({token.pos_: pos_token})
                
        return tags
    
    
    def return_lemma_pos_tags(self, articles):
        tags = []
        
        for article in articles:

            for token in article:
                pos_token = token.lemma_
                pos_token = pos_token.lower()
                
                #Quitar signos de puntuacion
                clean_punctuation = str.maketrans('','', string.punctuation)
                pos_token = pos_token.translate(clean_punctuation)
                
                #Eliminamos los stopwords
                stop_words = set(stopwords.words('spanish'))
                
                if pos_token.isalpha() and pos_token not in stop_words:
                    tags.append({token.pos_: pos_token})
                
        return tags
    
    
    def count_tags(self, articles):
        labels = []
        
        for article in articles:
            
            for entity in article:
                stop_words = set(stopwords.words('spanish'))
                
                if entity.text.isalpha() and entity not in stop_words:
                    labels.append(entity.pos_)   
                
        return Counter(labels)