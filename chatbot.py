import numpy as np
import nltk
import string
import random

f=open('chatbot.txt','r',errors='ignore')
raw_doc=f.read()
raw_doc=raw_doc.lower() #Converts text to lowercase
nltk.download('punkt') #using the Punkt tokenizer
nltk.download('wordnet') #using the WordNet dictionary
sent_tokens=nltk.sent_tokenize(raw_doc) #converts docto list of sentences
word_tokens=nltk.word_tokenize(raw_doc) #converts doc to list of words
sent_tokens[:2]