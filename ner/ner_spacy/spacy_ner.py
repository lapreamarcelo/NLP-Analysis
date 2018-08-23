#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 22:04:19 2018

@author: marcelolaprea
"""
import spacy
import pandas as pd

from nltk.corpus import stopwords
from collections import Counter

class SpacyNer:

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
    
    
    def most_commons(self, articles, filter_entity, most_common_number, isFilter):
        items = []
        
        for article in articles:
            
            for entity in article.ents:
                
                if isFilter == True:
                    
                    if filter_entity == entity.label_:
                        items.append(entity.text)
                        
                else:
                    items.append(entity.text)
        
        return Counter(items).most_common(most_common_number)
    
    
    def filter_articles(self, articles, filter_text):
        returnedArticles = []
        
        for article in articles:
            
            for entity in article.ents:
                
                if filter_text == entity.text:
                    returnedArticles.append(article)
        
        return returnedArticles
    
    
    def create_data_frame(self, articles):
        data_frame_content = []
        
        for article in articles:
            data_frame_content.append(article)
       
        data = {'Title': data_frame_content}
        
        data_frame = pd.DataFrame(data=data)
        
        return data_frame