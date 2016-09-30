from sklearn.feature_extraction.text import TfidfVectorizer,HashingVectorizer
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.cross_validation import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.grid_search import GridSearchCV
from nltk.stem.porter import PorterStemmer
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords
from sklearn.svm import SVC
import pyprind,pickle
import pandas as pd
import numpy as np
import nltk,os,re


class Foo(object):
	def __init__(self, name):
	        self.name = name


	def main():
		
		df = pd.read_csv('news_data_guardian.csv')
		df.dropna(inplace=True)

		X = df['Headlines']
		y = df['Category']

		print(X.shape,y.shape)
		X_train,X_test,y_train,y_test = train_test_split(X, y,test_size=0.3,random_state=1)

		stop_words = stopwords.words('english')
								
		def tokenizer(text):
			for c in [',','.','!','?']:
				text = text.replace(c,"")
			return nltk.word_tokenize(text) 

		porter = PorterStemmer() 
		def tokenizer_porter(text):
			return [porter.stem(word) for word in text.split()] 
			
		clf1 = LogisticRegression(random_state=1)
		clf2 = RandomForestClassifier(random_state=1)
		clf3 = SVC()

		eclf = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('svc', clf3)], voting='hard')

		vect = HashingVectorizer(decode_error='ignore',
		                         n_features=2**21,
		                         preprocessor=None,
		                         tokenizer=tokenizer)


		tfidf = TfidfVectorizer(strip_accents=None,lowercase=False,preprocessor=None) 

		param_grid = [{'vect__ngram_range': [(1, 1)],
		               'vect__stop_words': [stop_words, None],
		               'vect__tokenizer': [tokenizer, tokenizer_porter]},
		              {'vect__ngram_range': [(1, 1)],
		               'vect__stop_words': [stop_words, None],
		               'vect__tokenizer': [tokenizer, tokenizer_porter],
		               'vect__use_idf':[False],
		               'vect__norm':[None]},
		              ]
					  
		lr_tfidf = Pipeline([('vect', tfidf),('clf', eclf)])

		gs_lr_tfidf = GridSearchCV(lr_tfidf, param_grid,scoring='accuracy',cv = 5,verbose=1,n_jobs=1)

		gs_lr_tfidf.fit(X_train, y_train)
		save_classifier = open("news.pickle","wb")
		pickle.dump(gs_lr_tfidf, save_classifier)
		save_classifier.close()


		
		print('CV Accuracy: %.3f' % gs_lr_tfidf.best_score_)

	if __name__=='__main__':
		main()