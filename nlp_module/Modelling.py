import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_validate
from sklearn.metrics import classification_report, confusion_matrix
import pickle

class Modelevaluator(object):
  def __init__(self, model):
    self.model = model
    
  def fit(self, x, y):
    return self.model.fit(x, y)

  def make_prediction(self, x):
    return self.model.predict(x)

  def classification_report(self,x, y):
    y_pred = self.make_prediction(x)
    return print(classification_report(y, y_pred))

  def confusion_matrix(self,x, y):
    y_pred = self.make_prediction(x)
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(confusion_matrix(y, y_pred), ax=ax, annot=True, fmt='d')
    ax.set(xlabel='Predicted', ylabel='Truth')
    return plt.show()

  def cross_evaluation(self,x, y, cv_int):
    scores_tfidf = cross_validate(self.model, x, y, cv=cv_int,
                              return_train_score=True,
                              return_estimator=False)
    mean_train = round(scores_tfidf['train_score'].mean(),3)
    mean_test = round(scores_tfidf['test_score'].mean(),3)
    if abs(mean_train - mean_test) > 0.05:
      return print('Overfitting',',','mean_train_score:',mean_train,',',
                 'mean_test_score:',mean_test)
    else:
      return print('Not Overfitting',',','mean_train_score:',mean_train,',',
                 'mean_test_score:',mean_test)

  def save_model(self, filename):
       with open(filename, 'wb') as file: 
        return pickle.dump(self.model, file)
