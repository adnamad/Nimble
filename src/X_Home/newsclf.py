from nltk.stem.porter import PorterStemmer
import nltk,pickle,os
from nltk import word_tokenize
import dill as pickle
#from .algo import tokenizer

def clf(example):

  # def tokenizer(text):
  #   for c in [',','.','!','?']:
  #     text = text.replace(c,"")
  #   return word_tokenize(text) 

  # porter = PorterStemmer() 
  # def tokenizer_porter(text):
  #   return [porter.stem(word) for word in text.split()] 

  #print(os.path.abspath(__file__))

  gs_lr_tfidf = pickle.load(open('./pkl_objects/news_plz1.pkl', 'rb')) 
  clf = gs_lr_tfidf.best_estimator_      

  label = {0:'politics', 1:'sports', 2:'business',3:'culture',4:'football',5:'tech',6:'world'}
  example =['Apple launches new iphone']
  prediction = label[clf.predict(example)[0]]
  print("test 1")
  print(prediction)
  print("test 2")
  return(prediction)
