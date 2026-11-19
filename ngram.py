import nlftk
from nltk.until import ngrams
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nitk.download('point_tab')
test= "Data Visualization is a way to express your data in avisual context so that patterns,correlations,trends between the data can be easily understood"
words=word_tokenize(test)
unlarge=list(ugrams(words,1))
print("unlarge",unlarge)
bigram=list(ugrams(words,2))
print("bigram",bigram)
trigram=list(ngrams(word,3))
print("trigram",trigram)