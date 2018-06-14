#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:30:45 2018

@author: marcelolaprea
"""

from config import LEMMATIZATION_FILE_PATH
from collections import defaultdict

class Lemmatizer_Grounding(object):
    """
    Gets the lemmatization dictionary obtained from
            http://www.lexiconista.com/datasets/lemmatization/
    """

    def __init__(self):
        self.dict_lemmas = self.get_lemmas_dictionary()

    def get_lemmas_dictionary(self):
        """
        Gets the lemmatization dictionary
        :return: Dictionary where the keys are the words, and the values are the lemmas.
        """
        ftr = open(LEMMATIZATION_FILE_PATH, 'r')
        all_lines = ftr.read()
        ftr.close()
        file_with_lemmas = all_lines.split("\n")
        dict_lemmas = defaultdict(lambda: '')
        for line in file_with_lemmas:
            parts = line.split("\t")
            if len(parts) == 2:
                lemma = parts[0].lower()
                word = parts[1].strip().lower()
                dict_lemmas[word] = lemma
        return dict_lemmas

    def get_lemma(self, word):
        """
        Gets the lemma for a word.
        :param word: Word to be lemmatized
        :return: The lemma for the word
        """
        lemma = self.dict_lemmas[word.lower()]
        if lemma == '':
            lemma = word.lower()
        return lemma
    
    
    def returnTokens(self, tokens):
        
        lemmatizerTokens = [self.get_lemma(word) for word in tokens]
        
        return lemmatizerTokens
