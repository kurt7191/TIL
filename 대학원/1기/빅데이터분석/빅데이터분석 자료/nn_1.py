# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 23:19:11 2021
Decision Tree

@author: USER
"""

# Breast Cancer data
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt 

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import classification_report, confusion_matrix
from keras import models
from keras import layers

cancer = load_breast_cancer()

data_df = pd.DataFrame(cancer.data, columns=cancer.feature_names)

X = np.array(data_df)
y = cancer.target
len(y[y==1])/len(y[y==0])

scaler = preprocessing.MinMaxScaler()
X = scaler.fit_transform(X)

x_train, x_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2 , random_state= 156)

model=models.Sequential()
model.add(layers.Dense(4, activation='relu',input_dim=x_train.shape[1]))
model.add(layers.Dense(4, activation='relu'))
model.add(layers.Dense(1,activation='sigmoid'))
print(model.summary())


model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

history=model.fit(x_train,y_train,
                 epochs=200,batch_size=128,
                 validation_split=0.3, class_weight={0:1.68,1:1})

history_dict=history.history
history_dict.keys()

acc=history.history['accuracy']
val_acc=history.history['val_accuracy']
loss=history.history['loss']
val_loss=history.history['val_loss']
epochs=range(1,len(acc)+1)


plt.plot(epochs,loss,'bo',label='Training loss')
plt.plot(epochs,val_loss,'b',label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.legend()
plt.show()

plt.plot(epochs,acc,'bo',label='Training accuracy')
plt.plot(epochs,val_acc,'b',label='Validation accuracy')
plt.title('Training and validation Accuracy')
plt.xlabel('Epochs')
plt.legend()
plt.show()


predicted_result=model.predict(x_test)
predicted_result.shape
predicted_target=pd.Series([1 if predicted_result[i]> 0.5 \
         else 0 for i in range(0,predicted_result.shape[0])])
print(classification_report(y_test,predicted_target,\
         target_names=['no','yes']))
print(confusion_matrix(y_test,predicted_target))

# Logistic Regression
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(x_train,y_train)
y_pred_lr = lr.predict(x_test)


from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
print (' \n confusion_matrix of logistic regression \n ')
cm = confusion_matrix(y_test, y_pred_lr)
print (cm)
print ('\n Here is the classification report:')
print (classification_report(y_test, y_pred_lr))