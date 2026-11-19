
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')

test = "Data Visualization is a way to express your data in a visual context so that patterns, correlations, trends between the data can be easily understood"

# Tokenize the sentence
words = word_tokenize(test)

# Generate unigrams
unigram = list(ngrams(words, 1))
print("Unigram:", unigram)

# Generate bigrams
bigram = list(ngrams(words, 2))
print("Bigram:", bigram)

# Generate trigrams
trigram = list(ngrams(words, 3))
print("Trigram:", trigram)


