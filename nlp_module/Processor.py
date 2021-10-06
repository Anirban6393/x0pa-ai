import numpy as np
import pandas as pd
import nltk
from nltk.stem import SnowballStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Normalizer
import re
import unicodedata

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
stop = set(stopwords.words('english'))

def strip_accents(text):
    """
    Strip accents from input String.
    Returns string in plain English format.
    """
    try:
        text = unicode(text, 'utf-8',errors='ignore')
    except (TypeError, NameError): 
        pass
    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
    return text

class StemmerTokenizer(object):
    def __init__(self):
        self.stemmer = SnowballStemmer(language='english')
        self.stop = set(stopwords.words('english'))

    def __call__(self, doc):
        # Remove special characters & accents like diatrics
        doc = re.sub(r"[^A-Za-z0-9]", " ", doc)
        doc = strip_accents(doc)

        # tokenize text into word tokens
        tokens = word_tokenize(doc)
        
        # strip out punctuation & integers
        words = [t for t in tokens if t.isalpha()]

        #convert to lowercase
        words = [t.lower() for t in words]
        
        #remove accents
        words = [strip_accents(t) for t in words]
        
        # strip out stopwords
        words = [t for t in words if t not in self.stop]
        
        # stemming each token
        return [self.stemmer.stem(t) for t in words]