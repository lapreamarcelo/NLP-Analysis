#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 23:56:24 2018

@author: marcelolaprea
"""

import nltk
from nltk.corpus import stopwords
import string

#Instalando las librerias faltantes
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download('treebank')

class NLTK_POS_Tagger:
  
    #Funcion para retornar los tokens a partir de la Libreria NLKT
    def returnTokens(self, dataFrame):
        tokens = []
        
        for sentence in dataFrame['Title']:
            token = nltk.word_tokenize(sentence)
            token = [word.lower() for word in token]
            
            #Quitar signos de puntuacion
            cleanPunctuation = str.maketrans('','', string.punctuation)
            token = [word.translate(cleanPunctuation) for word in token]
            
            #Eliminar palabras no alfabeticas
            token = [word for word in token if word.isalpha()]
            
            #Eliminamos los stopwords
            stop_words = set(stopwords.words('spanish'))
            token = [word for word in token if not word in stop_words]
            
            tokens += token
        
        return tokens
    
    
    #Funcion para retornar los tagged words
    def returnTaggedWords(self, tokens):
        tagged = nltk.pos_tag(tokens)
        
        return tagged
    
    #Funcion para retornar la entidad
    def returnEntities(self, tagged):
        entities = nltk.chunk.ne_chunk(tagged)
        
        return entities