from nltk.stem.porter import PorterStemmer
import nltk,pickle,os

def clf(example):

  def tokenizer(text):
    for c in [',','.','!','?']:
      text = text.replace(c,"")
    return nltk.word_tokenize(text) 

  porter = PorterStemmer() 
  def tokenizer_porter(text):
    return [porter.stem(word) for word in text.split()] 


  gs_lr_tfidf = pickle.load(open(os.path.join('pkl_objects', 'newsclf-e.pkl'), 'rb')) 
  clf = gs_lr_tfidf.best_estimator_      

  label = {0:'politics', 1:'sports', 2:'business',3:'culture',4:'football',5:'tech',6:'world'}
  # example =['Danny Willett fears becoming ‘target’ for Ryder Cup fans after brother’s article']
  prediction = label[clf.predict(example)[0]]
  print(prediction)
  return(prediction)
