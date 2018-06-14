# -*- coding: utf-8 -*-

from config import *
from nltk.corpus import cess_esp as cess
from nltk import UnigramTagger as ut
import pickle

class POS_tagger_nltk(object):
    def __init__(self):
        """
        Initializes the tagger object
        """
        # nltk.download("cess_esp")
        # Read the corpus into a list, each entry in the list is one sentence.
        self.cess_sents = cess.tagged_sents()
        self.tagger_type = NLTK_TAGGER_NAME
        # This part is done only once, and we don't have to run it again.
        #   We keep the code here to understand how we created the model.
        # Train the unigram tagger
        # tagger = ut(self.cess_sents)
        # Store the trained tagger to a file
        # f = open('nltk_spanish_tagger.pickle', 'wb')
        # pickle.dump(tagger, f)
        # f.close()
        # Open the already trained model
        with open('nltk_spanish_tagger.pickle', 'rb') as f:
            # Load the tagger
            self.tagger = pickle.load(f)

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
        tags = self.tagger.tag(sentence)
        return tags
