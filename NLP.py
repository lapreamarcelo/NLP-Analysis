#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 23:09:23 2018

@author: marcelolaprea
"""

"""
Librerias y Modulos
"""
from mysql import mysql_connection as MySQL
from pos.pos_nltk import nltk_pos_tagger as NLTK_Tagger
from pos.pos_spacy import spacy_pos_tagger as SPACY_Tagger
from pos.pos_stanford import pos_tagger as STANFORD_Tagger
from grounding.stemmer import stemmer
from grounding.lemmatizer import lemmatizer
from ner.ner_spacy import spacy_ner as NER
import words_extraction
import time

"""
Conexion con la Base de Datos y creacion de DataFrame
"""
mySQLConnection = MySQL.MySQLConnection("localhost", "marcelo", "pass", "noticias")
df = mySQLConnection.createDataFrame()

"""
Frecuencia de las diferentes palabras
"""

def returnWords(dataFrame): 
    words = []
    
    for word in dataFrame['Title']:
        word = word.split()
        words += (word)
    
    return words

start_time = time.time()
words = returnWords(df)
end_time = time.time() - start_time

wordsFreq = words_extraction.Words_Extraction().returnWordFrequency(words, 20)


"""
Analisis POS con NLTK
"""
start_time = time.time()
tokens = NLTK_Tagger.NLTK_POS_Tagger().returnTokens(df)


stemmerTokens = stemmer.Stemmer_Grounding().returnPorterStemmerTokens(tokens)
lemmatizerTokens = lemmatizer.Lemmatizer_Grounding().returnTokens(tokens)

tagged = NLTK_Tagger.NLTK_POS_Tagger().returnTaggedWords(tokens)

verbs = words_extraction.Words_Extraction().detect_verbs(stemmerTokens)
nouns = words_extraction.Words_Extraction().detect_nouns(stemmerTokens)
adjectives = words_extraction.Words_Extraction().detect_adjectives(stemmerTokens)

nounsFreq = words_extraction.Words_Extraction().returnWordFrequency(nouns, 20)
adjectivesFreq = words_extraction.Words_Extraction().returnWordFrequency(adjectives, 20)
verbsFreq = words_extraction.Words_Extraction().returnWordFrequency(verbs, 20)
end_time = time.time() - start_time

"""
Analisis POS con SPACY
"""
#Sin grounding
start_time = time.time()
tokens = SPACY_Tagger.SPACY_POS_Tagger.returnSpacy(df)
end_time = time.time() - start_time

stemmerTokens = stemmer.Stemmer_Grounding().returnPorterStemmerTokens(tokens)

#Con Lemma
start_time = time.time()
tokens = SPACY_Tagger.SPACY_POS_Tagger.returnLemmaSpacy(df)
end_time = time.time() - start_time

verbs = words_extraction.Words_Extraction().detect_verbs(tokens)
nouns = words_extraction.Words_Extraction().detect_nouns(tokens)
adjectives = words_extraction.Words_Extraction().detect_adjectives(tokens)

nounsFreq = words_extraction.Words_Extraction().returnWordFrequency(nouns, 20)
adjectivesFreq = words_extraction.Words_Extraction().returnWordFrequency(adjectives, 20)
verbsFreq = words_extraction.Words_Extraction().returnWordFrequency(verbs, 20)

"""
Analisis POS con STANFORD
"""
from nltk.corpus import stopwords
import string

start_time = time.time()
tokens = STANFORD_Tagger.POS_tagger().returnTokens(df)
end_time = time.time() - start_time

stanfordTokens = [word[0] for word in tokens]

#Cleaning
stanfordTokens = [word.lower() for word in stanfordTokens]
cleanPunctuation = str.maketrans('','', string.punctuation)
stanfordTokens = [word.translate(cleanPunctuation) for word in stanfordTokens]
stanfordTokens = [word for word in stanfordTokens if word.isalpha()]
stop_words = set(stopwords.words('spanish'))
stanfordTokens = [word for word in stanfordTokens if not word in stop_words]


stemmerTokens = stemmer.Stemmer_Grounding().returnPorterStemmerTokens(stanfordTokens)
lemmatizerTokens = lemmatizer.Lemmatizer_Grounding().returnTokens(stanfordTokens)

#Sin Grounding
verbs = STANFORD_Tagger.POS_tagger().detect_verbs(tokens)
nouns = STANFORD_Tagger.POS_tagger().detect_nouns(tokens)
adjectives = STANFORD_Tagger.POS_tagger().detect_adjectives(tokens)

#Con Grounding
verbs = words_extraction.Words_Extraction().detect_verbs(stemmerTokens)
nouns = words_extraction.Words_Extraction().detect_nouns(stemmerTokens)
adjectives = words_extraction.Words_Extraction().detect_adjectives(stemmerTokens)

nounsFreq = words_extraction.Words_Extraction().returnWordFrequency(nouns, 20)
adjectivesFreq = words_extraction.Words_Extraction().returnWordFrequency(adjectives, 20)
verbsFreq = words_extraction.Words_Extraction().returnWordFrequency(verbs, 20)


"""
Analisis NER con Spacy
"""
articles = NER.SPACY_NER().getArticles(df)
entities = NER.SPACY_NER().getEntities(articles)
counter = NER.SPACY_NER().countEntities(articles)
mostCommon = NER.SPACY_NER().mostCommons(articles, 10)
