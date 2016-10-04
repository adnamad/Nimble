import os
import dill as pickle

def clf(example):
	# stop_words = pickle.load(open('./pkl_objects/stopwords.pkl', 'rb'))
	gs_lr_tfidf = pickle.load(open('./pkl_objects/Real_pickle.pkl', 'rb'))
	clf = gs_lr_tfidf.best_estimator_
	label = {0:'politics', 1:'sports', 2:'business',3:'culture',4:'football',5:'tech',6:'world'}
	example1 = [example]
	prediction = label[clf.predict(example1)[0]]
	# print(prediction)
	return(prediction)
