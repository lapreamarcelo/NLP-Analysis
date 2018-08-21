#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 22:04:19 2018

@author: marcelolaprea
"""
import spacy
from collections import Counter

class spacy_ner:

    def get_articles(self, data_frame):
        articles = []
        nlp = spacy.load('es_core_news_sm')
        
        for sentence in data_frame['Title']:
            doc = nlp(sentence)
            articles.append(doc)
            
        return articles
    
    
    def get_entities(self, articles):
        entities = []
        
        for article in articles:
            
            for entity in article.ents:
                entities.append({entity.label_: entity.text})
                
        return entities
    
    
    def count_entities(self, articles):
        labels = []
        
        for article in articles:
            
            for entity in article.ents:
                labels.append(entity.label_)
                
        return Counter(labels)
    
    
    def most_commons(self, articles, most_common):
        items = []
        
        for article in articles:
            
            for entity in article.ents:
                items.append(entity.text)
        
        return Counter(items).most_common(most_common)



def getArticles(dataFrame):
        articles = []
        nlp = spacy.load('es_core_news_sm')
        
        for sentence in dataFrame['Title']:
            article = ""
            
            doc = nlp(sentence)
            articles.append(doc)
            
        return articles
    
    
articles = getArticles(df)