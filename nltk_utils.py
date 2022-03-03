import nltk
nltk.download('punkt')       #downloading a package with a pretrained tokenizer
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):      #splitting a string into meaningful units
    return nltk.word_tokenize(sentence)

def stem(word):              #Generating the root form of the words
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    pass
