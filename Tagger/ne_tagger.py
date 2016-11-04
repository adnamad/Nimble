import nltk
from nltk.tag import StanfordNERTagger
import pandas as pd
import numpy as np
import ner


# df = pd.read_csv("news_data_guardian.csv")

# print(df.head())
# print(df.shape)

# headlines = df["Headlines"][:100]

#print(headlines)

''' NLTK's Named entity tagger

for sent in headlines:

	words_tokenized = nltk.word_tokenize(sent)
	tagged_words = nltk.pos_tag(words_tokenized)
	ne_tags = nltk.ne_chunk(tagged_words, binary=True)
	print(ne_tags.draw())
	print(ne_tags)
	print(type(ne_tags))

'''	
# For nltk's Stanford NE binding

#st = StanfordNERTagger('/Users/cranxter/Documents/toolkits_nltk/english.all.3class.distsim.crf.ser.gz','/Users/cranxter/Documents/toolkits_nltk/stanford-ner.jar', encoding='utf-8')
#sent = "Labour urges David Cameron to come clean over father's tax affairs"

def get_tags(text):

	tagger = ner.SocketNER(host='localhost', port=8081)
	#tok = nltk.word_tokenize(sent)
	ne_tags = tagger.get_entities(text)
	ne_tags= ne_tags.values()
	#print(ne_tags)
	return ne_tags
