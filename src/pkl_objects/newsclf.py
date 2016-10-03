from sklearn.feature_extraction.text import TfidfVectorizer,HashingVectorizer
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.cross_validation import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.grid_search import GridSearchCV
from nltk.stem.porter import PorterStemmer
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords
from sklearn.svm import SVC
import pyprind
import dill as pickle

import pandas as pd
import numpy as np
import nltk,os,re

df = pd.read_csv('news_data_guardian.csv')
df.dropna(inplace=True)

# print(df.head())
X = df['Headlines']
y = df['Category']

print(X.shape,y.shape)
X_train,X_test,y_train,y_test = train_test_split(X, y,test_size=0.2,random_state=1)

stop_words = stopwords.words('english')
"""						
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

# vect = HashingVectorizer(decode_error='ignore',
                         # n_features=2**21,
                         # preprocessor=None,
                         # tokenizer=tokenizer)


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


dest = os.path.join('Dataset', 'pkl_objects')
if not os.path.exists(dest):
	os.makedirs(dest)

pickle.dump(gs_lr_tfidf,open(os.path.join(dest, 'newsclf-e1.pkl'), 'wb'),protocol=4)
""" 
gs_lr_tfidf = pickle.load(open(os.path.join('pkl_objects', 'newsclf-e1.pkl'), 'rb')) 
# print('Best parameter set: %s ' % gs_lr_tfidf.best_params_)
# print('CV Accuracy: %.3f' % gs_lr_tfidf.best_score_)


clf = gs_lr_tfidf.best_estimator_      
# print('Test Accuracy: %.3f' % clf.score(X_test, y_test))


label = {0:'politics', 1:'sports', 2:'business',3:'culture',4:'football',5:'tech',6:'world'}
example =['Ben Duckett debut can lighten mood as England touch down in Bangladesh']
prediction = label[clf.predict(example)[0]]
print(prediction)



#love me Tinder – tales from the frontline of modern dating
#ales from the frontline of modern dating'
#London mayor launches unprecedented inquiry into foreign property ownership- buisness guardianS
#Jenson button/ driver admits ge is getting towards the end of road in F1 - guardian
#Tailor-made pitches bad for Ravichandran Ashwin legacy
#Google doodle celebrates 117th birthday of the inventor of ball point pen
#tesla sues michigan over ban on selling cars directly to customers
#Micromax launches Canvas 5 Lite with 2GB RAM at Rs 6499 :tech
