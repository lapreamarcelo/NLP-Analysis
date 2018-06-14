# -*- coding: utf-8 -*-
LEMMATIZATION_FILE_PATH = "/Users/marcelolaprea/Desktop/nlp/grounding/lemmatizer/lemmatization-es.txt"

# Configuration needed to use Stanford Tagger
TAGGER_MODEL = "/Users/marcelolaprea/Desktop/nlp/pos/pos_stanford/stanford-postagger-full-2014-08-27/models/spanish.tagger"
POS_TAGGER_JAR_FILE = "/Users/marcelolaprea/Desktop/nlp/pos/pos_stanford/stanford-postagger-full-2014-08-27/stanford-postagger-3.4.1.jar"
# Custom configuration
STANFORD_TAGGER_NAME = "stanford"
NLTK_TAGGER_NAME = "nltk"
SPANISH_TAG_SET_STANFORD = {
    "adjectives": ["ao0000", "aq0000"], \
    "conjunctions": ["cc", "cs"], \
    "determiners": ["da0000", "dd0000", "de0000", "di0000", "dn0000", \
        "do0000", "dp0000", "dt0000"], \
    "punctuation": ["f0", "faa", "fat", "fc", "fca", "fct", "fd", "fe", \
        "fg", "fh", "fia", "fit", "fp", "fpa", "fpt", "fra", "frc", \
        "fs", "ft", "fx", "fz"], \
    "interjections": ["i"], \
    "nouns": ["nc00000", "nc0n000", "nc0p000", "nc0s000", "np00000"], \
    "pronouns": ["p0000000", "pd000000", "pe000000", "pi000000", \
        "pn000000", "pp000000", "pr000000", "pt000000", "px000000"], \
    "adverbs": ["rg", "rn"], \
    "prepositions": ["sp000"], \
    "verbs": ["va00000", "vag0000", "vaic000", "vaif000", "vaii000", \
        "vaip000", "vais000", "vam0000", "van0000", "vap0000", "vasi000", \
        "vasp000", "vmg0000", "vmic000", "vmif000", "vmii000", "vmip000", \
        "vmis000", "vmm0000", "vmn0000", "vmp0000", "vmsi000", "vmsp000", \
        "vsg0000", "vsic000", "vsif000", "vsii000", "vsip000", "vsis000", \
        "vsm0000", "vsn0000", "vsp0000", "vssf000", "vssi000", "vssp000"], \
    "dates": ["w"], \
    "numerals": ["z0", "zm", "zu"], \
    "other": ["word"]}
# Obtained from: http://www.lsi.upc.edu/~nlp/semeval/docs/tagset_POS.pdf
# "abbreviations" are not included in Stanford's tagset (only in NLTK's tagset)
# "other" is not included in Stanford's tagset (only in NLTK's tagset)
SPANISH_TAG_SET_NLTK = {
    "adjectives": ["a"], \
    "adverbs": ["r"], \
    "determiners": ["d"], \
    "nouns": ["n"], \
    "verbs": ["v"], \
    "pronouns": ["p0"], \
    "conjunctions": ["c"], \
    "interjections": ["i"], \
    "abbreviations": ["y"], \
    "prepositions": ["s"], \
    "punctuation": ["f"], \
    "numerals": ["z"], \
    "dates": ["w"]}