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
from grounding.stemmer import stemmer
from grounding.lemmatizer import lemmatizer
import words_extraction

"""
Conexion con la Base de Datos y creacion de DataFrame
"""
mySQLConnection = MySQL.MySQLConnection("localhost", "user", "pass", "noticias")
df = mySQLConnection.createDataFrame()

"""
Analisis POS con NLTK
"""
tokens = NLTK_Tagger.NLTK_POS_Tagger().returnTokens(df)
stemmerTokens = stemmer.Stemmer_Grounding().returnPorterStemmerTokens(tokens)
lemmatizerTokens = lemmatizer.Lemmatizer_Grounding().returnTokens(tokens)

tagged = NLTK_Tagger.NLTK_POS_Tagger().returnTaggedWords(tokens)

verbs = words_extraction.Words_Extraction().detect_verbs(tokens)
nouns = words_extraction.Words_Extraction().detect_nouns(tokens)
adjectives = words_extraction.Words_Extraction().detect_adjectives(tokens)

nounsFreq = words_extraction.Words_Extraction().returnWordFrequency(nouns, 10)
adjectivesFreq = words_extraction.Words_Extraction().returnWordFrequency(adjectives, 10)
verbsFreq = words_extraction.Words_Extraction().returnWordFrequency(verbs, 10)

"""
Analisis POS con SPACY
"""
tokens = SPACY_Tagger.SPACY_POS_Tagger.returnSpacy(df)

verbs = words_extraction.Words_Extraction().detect_verbs(tokens)
nouns = words_extraction.Words_Extraction().detect_nouns(tokens)
adjectives = words_extraction.Words_Extraction().detect_adjectives(tokens)

nounsFreq = words_extraction.Words_Extraction().returnWordFrequency(nouns, 10)
adjectivesFreq = words_extraction.Words_Extraction().returnWordFrequency(adjectives, 10)
verbsFreq = words_extraction.Words_Extraction().returnWordFrequency(verbs, 10)