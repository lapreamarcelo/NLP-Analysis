# -*- coding: utf-8 -*-

from config import TAGGER_MODEL
from config import POS_TAGGER_JAR_FILE
from config import STANFORD_TAGGER_NAME
from nltk.tag.stanford import StanfordPOSTagger

# noinspection PyMethodMayBeStatic
class POS_tagger_stanford(object):
    
    def __init__(self):
        """
        Initializes the tagger object
        """
        self.model = TAGGER_MODEL
        self.jar_file = POS_TAGGER_JAR_FILE
        self.tagger = StanfordPOSTagger(self.model, self.jar_file)
        self.tagger_type = STANFORD_TAGGER_NAME

    def get_tags(self, sentence):
        """
        Gets the tags for tokenized sentence
        The full list of tags is available online:
            https://nlp.stanford.edu/software/spanish-faq.shtml

        Args:
            sentence (list): the sentence used to obtain the POS tags, each word
                is an element in the list

        Returns:
            tags (list): List containing both the word and its corresponding tag
        """
        #tagger = self.get_tagger()
        tags = self.tagger.tag(sentence)
        return tags
