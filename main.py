
############################## text tokenizer
# import nltk
# from nltk.tokenize import PunktSentenceTokenizer as PST
# from nltk.corpus import webtext
# from nltk.tokenize import sent_tokenize as st
#
# text = webtext.raw('/home/nfc/Desktop/train-tokenize.txt')
# sentTokenize =PST()
# sentences = sentTokenize.tokenize(text)
# print(sentences[-1])
################################ reading from file, tokenizing and removing stopwords
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer as PST
from nltk.corpus import webtext
from nltk.tokenize import word_tokenize as wt

englishStopwords = set(stopwords.words('english'))

text = webtext.raw('data/train-tokenize.txt')
words = wt(text)
result = [words for words in words if words not in englishStopwords]
print(result)