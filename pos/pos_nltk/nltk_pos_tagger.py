#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 23:56:24 2018

@author: marcelolaprea
"""
import string
import nltk

from nltk.corpus import stopwords

#Instalando las librerias faltantes
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download('treebank')

class NLTK_POS_Tagger:
  
    #Funcion para retornar los tokens a partir de la Libreria NLKT
    def return_tokens(self, data_frame):
        tokens = []
        
        for sentence in data_frame['Title']:
            token = nltk.word_tokenize(sentence)
            token = [word.lower() for word in token]
            
            #Quitar signos de puntuacion
            clean_punctuation = str.maketrans('','', string.punctuation)
            token = [word.translate(clean_punctuation) for word in token]
            
            #Eliminar palabras no alfabeticas
            token = [word for word in token if word.isalpha()]
            
            #Eliminamos los stopwords
            stop_words = set(stopwords.words('spanish'))
            token = [word for word in token if not word in stop_words]
            
            tokens += token
        
        return tokens
    
    
    #Funcion para retornar los tagged words
    def return_tagged_words(self, tokens):
        tagged = nltk.pos_tag(tokens)
        
        return tagged
    
    #Funcion para retornar la entidad
    def return_entities(self, tagged):
        entities = nltk.chunk.ne_chunk(tagged)
        
        return entities