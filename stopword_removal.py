import nltk
from nltk.corpus import stopwords, wordnet
from string import punctuation
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.collocations import *
from nltk.stem.lancaster import LancasterStemmer
from nltk.wsd import lesk

customStopWords = set(stopwords.words('english') + list(punctuation))

text = "Mary had a little lamb. Her fleece was white as snow"


#Tokenize
sents = sent_tokenize(text)
words = word_tokenize(text)
# print(sents)
# print(words)

#Remove StopWords
textWithoutStopWords = [word for word in word_tokenize(text) if word not in customStopWords]
# print(textWithoutStopWords)

#Identify N-Grams
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(textWithoutStopWords)
# print(sorted(finder.ngram_fd.items()))

#Stemming
text2 = "Mary closed on closing night when she was in the mood to close."
st = LancasterStemmer()
stemmedWords = [st.stem(word) for word in word_tokenize(text2)]
# print(stemmedWords)

#Acronym list can be found at https://pythonprogramming.net/natural-language-toolkit-nltk-part-speech-tagging/

wordsWithPOSTag = nltk.pos_tag(word_tokenize(text2))
# print(wordsWithPOSTag)

#Word Sense Disambiguation
sense1 = lesk(word_tokenize("Sing in a lower tone, along with the bass"), 'bass')
print(sense1, sense1.definition())
sense2 = lesk(word_tokenize("This sea bass was really hard to catch"), 'bass')
print(sense2, sense2.definition())
