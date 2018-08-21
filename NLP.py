#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 23:09:23 2018

@author: marcelolaprea
"""

"""
Librerias y Modulos
"""
import time
import words_extraction as extraction

from mysql import mysql_connection as MySQL
from pos.pos_nltk import nltk_pos_tagger as NLTK_Tagger
from pos.pos_spacy import spacy_pos_tagger as SPACY_Tagger
from pos.pos_stanford import pos_tagger as STANFORD_Tagger
from grounding.stemmer import stemmer
from grounding.lemmatizer import lemmatizer
from ner.ner_spacy import spacy_ner as NER

"""
Conexion con la Base de Datos y creacion de DataFrame
"""
my_sql_connection = MySQL.MySQLConnection("localhost", 
                                          "marcelo", 
                                          "pass", 
                                          "noticias")

df = my_sql_connection.create_data_frame()

"""
Frecuencia de las diferentes palabras
"""

def return_words(data_frame): 
    words = []
    
    for word in data_frame['Title']:
        word = word.split()
        words += (word)
    
    return words

start_time = time.time()
words = return_words(df)
end_time = time.time() - start_time

words_freq = extraction.Words_Extraction().return_word_frequency(words, 20)

"""
Analisis POS con NLTK
"""
start_time = time.time()
tokens = NLTK_Tagger.NLTK_POS_Tagger().return_tokens(df)


stemmer_tokens = stemmer.Stemmer_Grounding().return_porter_stemmer_tokens(tokens)
lemmatizer_tokens = lemmatizer.Lemmatizer_Grounding().return_tokens(tokens)

tagged = NLTK_Tagger.NLTK_POS_Tagger().return_tagged_words(tokens)

verbs = extraction.Words_Extraction().detect_verbs(stemmer_tokens)
nouns = extraction.Words_Extraction().detect_nouns(stemmer_tokens)
adjectives = extraction.Words_Extraction().detect_adjectives(stemmer_tokens)

nouns_freq = extraction.Words_Extraction().return_word_frequency(nouns, 20)
adjectives_freq = extraction.Words_Extraction().return_word_frequency(adjectives, 20)
verbs_freq = extraction.Words_Extraction().return_word_frequency(verbs, 20)
end_time = time.time() - start_time

"""
Analisis POS con SPACY
"""
articles = SPACY_Tagger.SPACY_POS_Tagger().get_articles(df)

#Sin grounding
start_time = time.time()
tokens = SPACY_Tagger.SPACY_POS_Tagger().return_tokens(articles)
end_time = time.time() - start_time

stemmer_tokens = stemmer.Stemmer_Grounding().return_porter_stemmer_tokens(tokens)

#Con Lemma
start_time = time.time()
tokens = SPACY_Tagger.SPACY_POS_Tagger().return_lemma_tokens(articles)
end_time = time.time() - start_time

verbs = extraction.Words_Extraction().detect_verbs(tokens)
nouns = extraction.Words_Extraction().detect_nouns(tokens)
adjectives = extraction.Words_Extraction().detect_adjectives(tokens)

nouns_freq = extraction.Words_Extraction().return_word_frequency(nouns, 20)
adjectives_freq = extraction.Words_Extraction().return_word_frequency(adjectives, 20)
verbs_freq = extraction.Words_Extraction().return_word_frequency(verbs, 20)

#Tags
tags_lemma = SPACY_Tagger.SPACY_POS_Tagger().return_lemma_pos_tags(articles)
tags = SPACY_Tagger.SPACY_POS_Tagger().return_pos_tags(articles)

"""
Analisis POS con STANFORD
"""
from nltk.corpus import stopwords
import string

start_time = time.time()
tokens = STANFORD_Tagger.POS_tagger().return_tokens(df)
end_time = time.time() - start_time

stanford_tokens = [word[0] for word in tokens]

#Cleaning
stanford_tokens = [word.lower() for word in stanford_tokens]
clean_punctuation = str.maketrans('','', string.punctuation)
stanford_tokens = [word.translate(clean_punctuation) for word in stanford_tokens]
stanford_tokens = [word for word in stanford_tokens if word.isalpha()]
stop_words = set(stopwords.words('spanish'))
stanford_tokens = [word for word in stanford_tokens if not word in stop_words]

stemmer_tokens = stemmer.Stemmer_Grounding().returnPorterStemmerTokens(stanford_tokens)
lemmatizer_tokens = lemmatizer.Lemmatizer_Grounding().returnTokens(stanford_tokens)

#Sin Grounding
verbs = STANFORD_Tagger.POS_tagger().detect_verbs(tokens)
nouns = STANFORD_Tagger.POS_tagger().detect_nouns(tokens)
adjectives = STANFORD_Tagger.POS_tagger().detect_adjectives(tokens)

#Con Grounding
verbs = extraction.Words_Extraction().detect_verbs(stemmer_tokens)
nouns = extraction.Words_Extraction().detect_nouns(stemmer_tokens)
adjectives = extraction.Words_Extraction().detect_adjectives(stemmer_tokens)

nouns_freq = extraction.Words_Extraction().returnWordFrequency(nouns, 20)
adjectives_freq = extraction.Words_Extraction().returnWordFrequency(adjectives, 20)
verbs_freq = extraction.Words_Extraction().returnWordFrequency(verbs, 20)

"""
Analisis NER con Spacy
"""
articles = NER.SpacyNer().get_articles(df)
entities = NER.SpacyNer().get_entities(articles)
counter = NER.SpacyNer().count_entities(articles)
most_common = NER.SpacyNer().most_commons(articles, 10)
