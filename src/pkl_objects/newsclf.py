import pandas as pd
import numpy as np
import os
import re
import dill as pickle
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer 
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer


df = pd.read_csv('./news_data_guardian.csv')

print(df.head())
print(df.isnull().sum())
print(df['Category'].unique())

def preprocessor(text):
  text = re.sub('<[^>]*>', '', text)
  emoticons = re.sub('(?::|;|=)(?:-)?(?:\)|\(|D|P)','', text)
  text = re.sub('[\W]+', ' ', text.lower())
  return text

df['Headlines']=df['Headlines'].apply(preprocessor)
stop = stopwords.words('english')
print(df.head())

def tokenizer(text):
  tokenized =word_tokenize(text)
  return tokenized  

porter = PorterStemmer() 
def tokenizer_porter(text):
  return [porter.stem(word) for word in text.split()] 

X_train = df.loc[:45000,'Headlines'].values
y_train = df.loc[:45000,'Category'].values
X_test = df.loc[45000:,'Headlines'].values
y_test = df.loc[45000:,'Category'].values

tfidf = TfidfVectorizer(strip_accents = None, lowercase=False, preprocessor= None)

param_grid = [{'vect__ngram_range': [(1, 1)],
               'vect__stop_words': [stop,None],
               'vect__tokenizer': [tokenizer,tokenizer_porter],
               'clf__penalty': ['l1', 'l2'],
               'clf__C': [1.0, 10.0, 100.0]}]

pipe_tfidf_lr =Pipeline([('vect',tfidf),('clf',LogisticRegression(random_state=0))])

gs_clf = GridSearchCV(pipe_tfidf_lr,param_grid,scoring='accuracy',cv=5,verbose=1,n_jobs=1)
gs_clf.fit(X_train,y_train)

dest = './pkl_2_objects'
if not os.path.exists(dest):
  os.makedirs(dest)
pickle.dump(gs_clf,open(os.path.join(dest, 'news_7.pkl'), 'wb'),protocol=4) 

#gs_clf = pickle.load(open(os.path.join('pkl_objects', 'news.pkl'), 'rb'))

print('Best parameter set: %s ' % gs_clf.best_params_)
print('CV_accuracy: %.3f' % gs_clf.best_score_)
clf= gs_clf.best_estimator_
print("test accuracy: %.3f " % clf.score(X_test,y_test))
n= ["Klopp warns squad over social media after Sakho Snapchat outburst"]
print(clf.predict(n))
print(clf.predict_proba(n))               



