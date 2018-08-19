#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 22:04:19 2018

@author: marcelolaprea
"""
import spacy
from collections import Counter

class SPACY_NER:

    def getArticles(self, dataFrame):
        articles = []
        nlp = spacy.load('es_core_news_sm')
        
        for sentence in dataFrame['Title']:
            doc = nlp(sentence)
            articles.append(doc)
            
        return articles
    
    
    def getEntities(self, articles):
        entities = []
        
        for article in articles:
            
            for X in article.ents:
                entities.append({X.label_: X.text})
                
        return entities
    
    
    def countEntities(self, articles):
        labels = []
        
        for article in articles:
            
            for x in article.ents:
                labels.append(x.label_)
                
        return Counter(labels)
    
    
    def mostCommons(self, articles, mostCommon):
        items = []
        
        for article in articles:
            
            for x in article.ents:
                items.append(x.text)
        
        return Counter(items).most_common(mostCommon)