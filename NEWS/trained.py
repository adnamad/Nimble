from sklearn.feature_extraction.text import TfidfVectorizer,HashingVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.grid_search import GridSearchCV
from nltk.stem.porter import PorterStemmer
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split 
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import pyprind,pickle
import nltk,os,re

df = pd.read_table('newsCorpora.csv',header = None,sep='\t')
df.columns = ['ID','TITLE','URL','PUBLISHER','CATEGORY','STORY','HOSTNAME','TIMESTAMP']
df.dropna(inplace=True)
mapping = {'b' :0,'e':1,'m':2,'t':3}
df['CATEGORY'] = df['CATEGORY'].map(mapping) 



X = df['TITLE'][:30000]
y = df['CATEGORY'][:30000]

print(X.shape,y.shape)

X_train,X_test,y_train,y_test = train_test_split(X, y,test_size=0.3,random_state=1)

stop_words = stopwords.words('english')
						
# def tokenizer(text): 
	# return nltk.word_tokenize(text) 
	
def tokenizer(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text.lower())
    text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')
    tokenized = [w for w in text.split() if w not in stop_words]
    return tokenized

porter = PorterStemmer() 
def tokenizer_porter(text):
	return [porter.stem(word) for word in text.split()] 
	"""
vect = HashingVectorizer(decode_error='ignore',
                         n_features=2**21,
                         preprocessor=None,
                         tokenizer=tokenizer)

0
tfidf = TfidfVectorizer(strip_accents=None,lowercase=False,preprocessor=None) 

param_grid = [{'vect__ngram_range': [(1, 1)],
               'vect__stop_words': [stop_words, None],
               'vect__tokenizer': [tokenizer, tokenizer_porter],
               'clf__penalty': ['l1', 'l2'],
               'clf__C': [1.0, 10.0, 100.0]},
              {'vect__ngram_range': [(1, 1)],
               'vect__stop_words': [stop_words, None],
               'vect__tokenizer': [tokenizer, tokenizer_porter],
               'vect__use_idf':[False],
               'vect__norm':[None],
               'clf__penalty': ['l1', 'l2'],
               'clf__C': [1.0, 10.0, 100.0]},
              ]
			  
lr_tfidf = Pipeline([('vect', tfidf),('clf', LogisticRegression(random_state=0))])

gs_lr_tfidf = GridSearchCV(lr_tfidf, param_grid,scoring='accuracy',cv = 5,verbose=1,n_jobs=1)

gs_lr_tfidf.fit(X_train, y_train)


dest = os.path.join('Dataset', 'pkl_objects')
if not os.path.exists(dest):
	os.makedirs(dest)

pickle.dump(gs_lr_tfidf,open(os.path.join(dest, 'news.pkl'), 'wb'),protocol=4) 
"""
gs_lr_tfidf = pickle.load(open(os.path.join('pkl_objects', 'news.pkl'), 'rb')) 
# print('Best parameter set: %s ' % gs_lr_tfidf.best_params_)
print('CV Accuracy: %.3f' % gs_lr_tfidf.best_score_)


# X_test = df['TITLE'][30000:40000]
# y_test = df['CATEGORY'][30000:40000]
# print(X_test[:100])


clf = gs_lr_tfidf.best_estimator_
print('Test Accuracy: %.3f' % clf.score(X_test, y_test))




label = {0:'buisness', 1:'entertainment', 2:'health',3:'tech'}
example = ['tesla sues michigan over ban on selling cars directly to customers']
#Nobody can accurately tell the revenue neutral rate for GST: b
# :tech
prediction = label[clf.predict(example)[0]]
# print(prediction)
probability = np.max(gs_lr_tfidf.predict_proba(example))*100

print('Prediction: %s\nProbability: %.2f%%' % (prediction,probability))