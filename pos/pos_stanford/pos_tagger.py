#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:47:58 2018

@author: marcelolaprea
"""

from config import STANFORD_TAGGER_NAME
from config import NLTK_TAGGER_NAME
from config import SPANISH_TAG_SET_NLTK
from config import SPANISH_TAG_SET_STANFORD
from pos.pos_stanford import POS_tagger_stanford as stanford_tagger
from pos.pos_stanford import POS_tagger_nltk as nltk_tagger
from nltk.tokenize import word_tokenize

class POS_tagger(object):
    def __init__(self):
        """
        Initialize the tagger as specified in the configuration
        The available tagger_types are:
          * TAGGER_TYPE = STANFORD_TAGGER_NAME
          * TAGGER_TYPE = NLTK_TAGGER_NAME
        """
        self.TAGGER_TYPE = STANFORD_TAGGER_NAME
        tagger_type = STANFORD_TAGGER_NAME
        # The default tagger is NLTK tagger
        if tagger_type == STANFORD_TAGGER_NAME:
            tagger = stanford_tagger.POS_tagger_stanford()
            tagset = SPANISH_TAG_SET_STANFORD
        else:
            tagger = nltk_tagger.POS_tagger_nltk()
            tagset = SPANISH_TAG_SET_NLTK
        self.tagger = tagger
        self.tagset = tagset

    def get_tags(self, sentence):
        """
        Method to get the tags from a sentence
        """
        tags = self.tagger.get_tags(sentence)
        return tags

    def extract_elem_using_tags(self, element_tags, tags_in_sentence):
        """
        Method to extract certain elements given the tags from a sentence
        """
        elements = []
        for t in tags_in_sentence:
            word = t[0]
            tag = t[1]
            if self.TAGGER_TYPE == NLTK_TAGGER_NAME:
                if tag != None:
                    tag = tag[0].lower()
            if tag in element_tags:
                elements.append(word)
        return elements

    def detect_nouns(self, tags_in_sentence):
        """
        Method to extract the nouns from a sentence given the tags
        """
        noun_tags = self.tagset["nouns"]
        nouns_in_one_sentence = self.extract_elem_using_tags(noun_tags, tags_in_sentence)
        return nouns_in_one_sentence

    def detect_adjectives(self, tags_in_sentence):
        """
        Method to extract the adjectives from a sentence given the tags
        """
        noun_tags = self.tagset["adjectives"]
        nouns_in_one_sentence = self.extract_elem_using_tags(noun_tags, tags_in_sentence)
        return nouns_in_one_sentence

    def detect_verbs(self, tags_in_sentence):
        """
        Method to extract the verbs from a sentence given the tags
        """
        verb_tags = self.tagset["verbs"]
        verbs_in_one_sentence = self.extract_elem_using_tags(verb_tags, tags_in_sentence)
        return verbs_in_one_sentence
    
    
    def returnTokens(self, dataFrame):
        tokens = []
    
        for sentence in dataFrame['Title']:
            sentence_words = word_tokenize(sentence)
            stanfordTokens = self.get_tags(sentence_words)
            
            tokens += stanfordTokens
            
        return tokens